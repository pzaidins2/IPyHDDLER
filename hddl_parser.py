# this file allows for hddl file to be read in and converted to python friendly representation
import io
import re
import json
from copy import deepcopy
import os
from typing import List, Dict, Union, Set, Tuple
from ipyhop import State, IPyHOP

# takes PDDL strings and makes them assignable to python variables
def clean_string( input_str: str ) -> str:
    # ? must be removed
    new_str = input_str.replace( "?", "")
    # - must be replaced with _
    new_str = new_str.replace( "-", "_" )
    # PDDL is case insensitive so we are going to make everything lower case
    new_str = new_str.lower()
    return new_str

class HDDL_Parser:
    def __init__(self):
        self.domain_dict = None
        self.problem_dict = None

    def parse_domain( self, domain_json_path: str ) -> None:
        # read json as dictionary
        with open(domain_json_path) as f:
            domain_dict = json.load(f)
        self.domain_dict = domain_dict
        return

    def parse_problem( self, problem_json_path: str ) -> None:
        # read json as dictionary
        with open( problem_json_path ) as f:
            problem_dict = json.load( f )
        self.problem_dict = problem_dict

    # domain dictionary
    # "$schema": str
    # "constants": List[Constant]
    # Constant: ???
    # "name": str (UNIQUE)
    # "predicates": List[Predicate]
    # Predicate := { "name": str (UNIQUE), "parameters": List[Parameter] }
    # Parameter := { "name": str (UNIQUE), "type": str }
    # "requirements: List[str]
    # "tasks": List[Task]
    # Task := { "name": str (UNIQUE), "parameters": List[Parameter] }
    # "types": List[Type]
    # Type := { "supertype": str, "type": str (UNIQUE) }
    # "actions": List[Action]
    # Action := { "effect": Effect  "name": str (UNIQUE), "parameters": List[Parameter], "precondition": Operation }
    # Effect := { "effects": List[Expression], "op": str }
    # Expression := Operation | TypelessPredicate
    # TypelessPredicate := { "name": str, "args": str }
    # Operation := { "op": str, "operand": List[Expression] }
    # "methods": List[Method]
    # Method := { "name": str (UNIQUE), "parameters": List[Parameter], "precondition": Operation, "task": TypelessTask, ...
    # "taskNetwork": OrderedSubtasks }
    # TypelessTask := { "predicate": str, "args": str }
    # OrderedSubtasks := ???

    def write_domain( self, dir_path: str="." ) -> None:
        # create domain dict copy
        domain_dict = deepcopy( self.domain_dict )
        # create folder
        domain_path = dir_path + "/domain"
        # write actions.py
        actions_str = "from ipyhop import Actions\n"
        # for every action in actions
        for action in domain_dict["actions"]:
            # append action function to actions.py str
            actions_str = append_action_function_str( action, actions_str )
        # Create a IPyHOP Actions object
        # NEED TO RESERVE KEYWORDS: actions, methods
        actions_str += "\nactions = Actions()\n"
        actions_str += "actions.declare_actions( [ "
        for action in domain_dict[ "actions" ]:
            actions_str += clean_string( action[ "name" ] ) + ", "
        actions_str += "] )\n"
        with open( domain_path + "/actions.py", "w" ) as actions_file:
            actions_file.write(actions_str)
        # write methods.py
        methods_str = "from ipyhop import Methods\n"
        # for every method in methods
        task_method_dict = dict()
        for method in domain_dict[ "methods" ]:
            # append method function to methods.py str
            methods_str = append_method_function_str( method, methods_str,domain_dict )
            # build task_method_dict
            if clean_string( method[ "task" ][ "predicate" ] ) not in task_method_dict.keys():
                task_method_dict[ clean_string( method[ "task" ][ "predicate" ] ) ] = set()
            task_method_dict[ clean_string( method[ "task" ][ "predicate" ] ) ].add( clean_string( method[ "name" ] ) )
        # Create a IPyHOP Methods object
        methods_str += "\nmethods = Methods()\n"
        # associate methods to tasks
        for task, method_set in task_method_dict.items():
            methods_str += "methods.declare_task_methods( '" + task + "', [ "
            for method in method_set:
                methods_str += method + ", "
            methods_str += "] )\n"
        with open( domain_path + "/methods.py", "w" ) as methods_file:
            methods_file.write( methods_str )

    def write_problem( self, dir_path: str = "." ) -> None:
        # create dict copies
        problem_dict = deepcopy( self.problem_dict )
        domain_dict = deepcopy( self.domain_dict )
        # make and save state and task network for easy load at runtime
        init_state_str = ""
        init_state_str += "from ipyhop import State\n\n"
        init_state_str += "init_state = State( 'init_state' )\n"
        # make typed sets
        objs = problem_dict[ "objects" ]
        typed_sets = dict()
        for obj in objs:
            name = clean_string( obj[ "name" ] )
            type = clean_string( obj[ "type" ] )
            if type not in typed_sets.keys():
                typed_sets[ type ] = set()
            typed_sets[ type ].add( name )
        for type in typed_sets.keys():
            init_state_str += "init_state." + type + " = "
            init_state_str += str(typed_sets[type]) + "\n"
        # group atoms
        atom_arg_dict = dict()
        for atom in problem_dict[ "init" ]:
            name = clean_string( atom[ "predicate" ] )
            args = tuple( map( clean_string, atom[ "args" ] ) )
            if name not in atom_arg_dict.keys():
                atom_arg_dict[ name ] = set()
            atom_arg_dict[ name ].add( args )
        # write atoms by predicate
        for name in atom_arg_dict.keys():
            init_state_str += "init_state." + name + " = { "
            for args in atom_arg_dict[ name ]:
                init_state_str += str( args ) + ", "
            init_state_str += "}\n"

        with open( "problem.py", "w" ) as f:
            f.write(init_state_str)

        # write tasks in order as tuples
        task_list_str = ""
        tasks = problem_dict[ "htn" ][ "orderedSubtasks" ]
        task_list = [ ( task[ "predicate" ], *task[ "args" ] ) for task in tasks ]
        task_list_str += "\ntask_list = "
        task_list_str += str(task_list) + "\n"

        with open( "problem.py", "a" ) as f:
            f.write(task_list_str)


# add N number of tabs for every line in string
def tabify( input_str: str, N: int ):
    return ( N * '\t' ).join( ("\n" + input_str).splitlines() )

# takes text representation of actions.py and appends action
# act: Dict representing a single action template
# actions_str: text representation of existing actions.py file
def append_action_function_str( action: Dict[str,Union[str,Dict]], actions_str: str) -> str:
    # space out actions
    actions_str += "\n"
    # def <action_name>( state, *parameter_names ):
    actions_str += "def " + clean_string( action["name"] ) + "( state"
    parameters = action["parameters"]
    parameter_names = map( lambda x: clean_string( x["name"] ), parameters )
    for parameter_name in parameter_names:
        actions_str += ", " + parameter_name
    actions_str += " ):\n"
    # if precondition
    # def <op>( *<operands> ) | (*<args>) in state[<predicate>] :
    precondition = action["precondition"]
    actions_str += "\tif " + make_precondition_str( precondition ) + ":\n"
    print( make_precondition_str( precondition ) )
    # effect
    # add and delete from state in order
    effect = action["effect"]
    if effect != None:
        actions_str += "\t\t" + make_effects_str( effect ) + "\n"
    actions_str += "\t\treturn state\n"
    return actions_str

# takes text representation of methods.py and appends method
# method: Dict representing a single method template
# methods_str: text representation of existing methods.py file
def append_method_function_str( method: Dict[str,Union[str,Dict]], methods_str: str, domain_dict: Dict[str,Union[str,Dict]]) -> str:
    # space out methods
    methods_str += "\n"

    parameters = method[ "parameters" ]
    parameter_names = [*map( lambda x: clean_string( x[ "name" ] ), parameters )]

    # iterate over valid parameter groundings
    # parameters from task are fixed, but all other parameters are only limited by preconditions
    # and typing
    task_parameter_names = [*map( lambda x: clean_string( x ), method[ "task" ][ "args" ] )]
    # HOW TO DEAL WITH TASK PARAMETER DUPLICATES???
    parameter_set_diff = {*parameter_names} - {*task_parameter_names}
    parameter_set_diff = list(parameter_set_diff)
    parameter_set_diff.sort()
    # dict to get type with parameter name
    parameter_name_type_dict = {}
    for parameter in parameters:
        parameter_name_type_dict[ clean_string( parameter[ "name" ] ) ] = clean_string( parameter[ "type" ] )

    # def <method_name>( state, *parameter_names ):
    # we cant have variables in the method signature not defined by the task
    methods_str += "def " + clean_string( method[ "name" ] ) + "( state"
    print(task_parameter_names)
    # deal with duplicates
    # relabel all occurrences after first and alter precondition to require equality
    precondition_equalities = set()
    for i in range(len(task_parameter_names)):
        check_name = task_parameter_names[i]
        count = 0
        for j in range(i+1,len(task_parameter_names)):
            curr_name = task_parameter_names[j]
            if check_name == curr_name:
                count += 1
                task_parameter_names[j] = task_parameter_names[j] + "___" + str(count)
                precondition_equalities.add( ( i, j ) )


    for parameter_name in task_parameter_names:
        methods_str += ", " + parameter_name
    methods_str += " ):\n"

    # nesting type iteration loops in alphabetic order
    # CURRENTLY UNTESTED

    for i, parameter_name in enumerate(parameter_set_diff):
        methods_str += "\t" * ( i + 1 )
        methods_str += "for " + parameter_name + " in state." + parameter_name_type_dict[ parameter_name ] + ":\n"
    # print( iteration_optimizer( [*parameter_set_diff], ))

    # if precondition
    # def <op>( *<operands> ) | (*<args>) in state[<predicate>] :
    precondition = method[ "precondition" ]
    # cnf_precondition = make_precondition_cnf(precondition)
    if precondition != None:
        if len( precondition_equalities ) == 0:
            methods_str += ( len(parameter_set_diff) + 1 ) * "\t" + "if " + make_precondition_str( precondition ) + ":\n"
        else:
            methods_str += (len( parameter_set_diff ) + 1) * "\t" + "if " + "all( [" + make_precondition_str(
                precondition ) + ", "
            for t_l, f_l in precondition_equalities:
                methods_str += task_parameter_names[ t_l ] + " == " + task_parameter_names[ f_l ] + ", "
            methods_str += "] ):\n"

        # yield statement with task network
        methods_str += ( len(parameter_set_diff) + 2 ) * "\t" + "yield " + \
                       make_task_network_str( method[ "taskNetwork"][ "orderedSubtasks"]) +"\n"
    else:
        if len(precondition_equalities) == 0:
            # yield statement with task network
            methods_str += (len( parameter_set_diff ) + 1) * "\t" + "yield " + \
                           make_task_network_str( method[ "taskNetwork" ][ "orderedSubtasks" ] ) + "\n"
        else:
            methods_str += (len( parameter_set_diff ) + 1) * "\t" + "if " + "all( [ "
            for t_l, f_l in precondition_equalities:
                methods_str += task_parameter_names[ t_l ] + " == " + task_parameter_names[ f_l ] + ", "
            methods_str += "] ):\n"
            # yield statement with task network
            methods_str += (len( parameter_set_diff ) + 2) * "\t" + "yield " + \
                           make_task_network_str( method[ "taskNetwork" ][ "orderedSubtasks" ] ) + "\n"
    return methods_str

# recursively write precondition expressions in equivalent python syntax
def make_precondition_str( precondition: Dict[str,Union[str,Dict]] ) -> str:
    # precondition with operation
    if "op" in precondition.keys():
        op = precondition["op"]

        # all operands must be true
        if op == "and":
            operands = precondition[ "operands" ]
            precondition_str = "all( [ "
            for operand in operands:
                precondition_str += make_precondition_str(operand) + ", "
            precondition_str += "] )"
            return precondition_str
        # operand must be false
        elif op == "not":
            operand = precondition[ "operand" ]
            return "not( " + make_precondition_str( operand ) + " )"
        else:
            raise( op + " is an unsupported op for precondition!" )
    # predicate precondition
    else:
        predicate = precondition["predicate"]
        args = precondition["args"]
        predicate_str = "( "
        for arg in args:
            predicate_str += clean_string( arg ) + ", "
        predicate_str += ") in " + "state." + clean_string(predicate)
        return predicate_str

# recursively write effect expressions in equivalent python syntax
def make_effects_str( effects: Dict[str,Union[str,Dict]] ) -> str:
    # effects with operation
    if "op" in effects.keys():
        op = effects[ "op" ]

        # all operands will occur
        if op == "and":
            operands = effects[ "effects" ]
            effects_str = ""
            for operand in operands:
                effects_str += make_effects_str(operand) + "; "
            return effects_str
        # operand will remove predicate
        elif op == "not":
            operand = effects[ "operand" ]
            if "predicate" not in operand.keys():
                raise( "When used as an effect, 'not' must have single predicate as operand")
            predicate = operand[ "predicate" ]
            args = operand[ "args" ]
            predicate_str = "state." + predicate + ".remove( ( "
            for arg in args:
                predicate_str += clean_string( arg ) + ", "
            predicate_str += ") )"
            return predicate_str
        else:
            raise (op + " is an unsupported op for effects!")
    # predicate effects
    else:
        predicate = effects[ "predicate" ]
        args = effects[ "args" ]
        predicate_str = "state." + predicate + ".add( ( "
        for arg in args:
            predicate_str += clean_string(arg) + ", "
        predicate_str += ") )"
        return predicate_str

# make string for single task
def make_task_str( task: Dict[str,Union[str,Dict]]) -> str:
    predicate = task[ "predicate" ]
    args = task[ "args" ]
    predicate_str = "( '" + clean_string( predicate ) + "', "
    for arg in args:
        predicate_str += clean_string( arg ) + ", "
    predicate_str += ")"
    return predicate_str

# make string for task network
def make_task_network_str( tasks: List[Dict[str,Union[str,Dict]]] ) -> str:
    # string the task tuples together
    task_net_str = "[ "
    for task in tasks:
        task_net_str += make_task_str( task ) + ", "
    task_net_str += "]"
    return task_net_str


# make precondition cnf
def make_precondition_cnf( precondition: Dict[str,Union[str,Dict]] ) -> Dict[str,Union[str,Dict]]:
    # move negations downward until either negation of simple predicate or doubly negated and removed
    # BFS while calling negation helper when we encounter negation
    if precondition != None:
        new_precondition = cnf_negation_helper( precondition )
    else:
        new_precondition = None
        return new_precondition
    # move ors downward until only disjunction of predicates and negations of predicates
    # BFS while calling disjunction helper when we encounter disjunction
    new_precondition = cnf_disjunction_helper( new_precondition )
    return new_precondition

# propagates negation downward
def cnf_negation_helper( precondition: Dict[str,Union[str,Dict]] ):
    if "op" in precondition.keys() and precondition[ "op" ] == "not":
        # do nothing single predicate negation
        if "operand" in precondition.keys() and "predicate" in precondition["operand"].keys():
            return precondition
        # negate negation and continue downward
        elif "operand" in precondition.keys() and precondition["operand"][ "op" ] == "not":
            return cnf_negation_helper( precondition[ "operand" ][ "operand" ] )
        # propagate negation over conjunction
        elif precondition["operand"][ "op" ] == "and":
            return {
                "op": "or",
                "operands": [
                    cnf_negation_helper( {
                        "op": "not",
                        "operand": operand
                    } ) for operand in precondition[ "operands" ]
                ]
            }
        # propagate negation over disjunction
        elif precondition[ "op" ] == "or":
            return {
                "op": "and",
                "operands": [
                    cnf_negation_helper( {
                        "op": "not",
                        "operand": operand
                    } ) for operand in precondition[ "operands" ]
                ]
            }
        else:
            raise( "unsupported precondtion encountered during negation propagation")
    else:
        return precondition


# propagates disjunction downward
# merge nested ors and propagate over ands
def cnf_disjunction_helper( precondition: Dict[str,Union[str,Dict]] ):
    if "op" in precondition.keys() and precondition[ "op" ] == "or":
        # pull descendant ors to top
        # iterate over operands if or encountered, pop that operand and append to back
        new_or_precondtion = {
            "op": "or",
            "operands": []
        }
        for operand in precondition[ "operands" ]:
            # remove and append operands to top
            if "op" in operand.keys() and operand[ "op" ] == "or":
                new_or_precondtion["operands"] += [ *map( cnf_disjunction_helper, operand[ "operands" ] ) ]
            # do nothing
            else:
                new_or_precondtion["operands"].append( cnf_disjunction_helper( operand ) )

        # merge subordinate ands into single subordinate and

        new_and = {
            "op": "and",
            "operands": [ ]
        }
        if any( map( lambda x: "op" in x.keys() and x[ "op" ] == "and", new_or_precondtion[ "operands" ] ) ):

            new_and_precondtion = {
                "op": "or",
                "operands": [
                    new_and
                ]
            }
            for operand in new_or_precondtion[ "operands" ]:
                # remove and append operands to top
                if "op" in operand.keys() and operand[ "op" ] == "and":
                    new_and[ "operands" ] += [ *map( cnf_disjunction_helper, operand[ "operands" ] ) ]
                # do nothing
                else:
                    new_and_precondtion["operands"].append( cnf_disjunction_helper( operand ) )
        else:
            new_and_precondtion = {
                "op": "or",
                "operands": [
                ]
            }


        # replace current with and where the operands are now or statements with each such statement containing all the
        # non-and original operands with a single operand from the and operands
        new_precondition = {
            "op": "and",
            "operands": [
            ]
        }
        new_and_precondtion[ "operands" ] = [ *filter( lambda x: "op" in x.keys() and x[ "op" ] != "and",
                                                   new_and_precondtion[ "operands" ] ) ]
        for operand in new_and[ "operands" ]:
            new_precondition[ "operands" ].append(
                {
                    "op": "or",
                    "operands": [
                        operand,
                        *map( cnf_disjunction_helper, new_and_precondtion[ "operands" ] )
                    ]
                }
            )
        return new_precondition
    else:
        return precondition

# take predicate tree and return CNF as list of clauses
# clauses dictate how predicates are evaluated together
# IN PROGRESS
def make_clause_cnf_list( precondition: Dict[ str, Union[ str, Dict ] ] ) -> List[Tuple[List,List]]:
    # simplify to CNF
    cnf_precondition = make_precondition_cnf( deepcopy( precondition ) )
    # make into list
    clause_list = [ ]
    # PREDICATE
    # NOT PREDICATE
    # AND [ UNION[ PREDICATE, NOT PREDICATE, OR ] ]
    # OR [ UNION[ PREDICATE, NOT PREDICATE ] ]
    # form
    # [ AND [ OR ( [IS], [NOT] ), ] ]
    # NOTE THERE MUST BE A CLEANER WAY
    # single predicate
    if "predicate" in cnf_precondition.keys():
        clause_list = [ ( [ ( cnf_precondition[ "predicate" ], *cnf_precondition[ "args" ], ), ], [ ] ) ]
    # negation of predicate
    elif cnf_precondition[ "op" ] == "not":
        clause_list = [ ( [ ], [ ( cnf_precondition["operand"][ "predicate" ], *cnf_precondition["operand"][ "args" ], ), ] ) ]
    # conjunction
    elif cnf_precondition[ "op" ] == "and":
        clause_list = []
        for conjunct in cnf_precondition[ "operands" ]:
            clause = ( [], [] )
            if "predicate" in conjunct.keys():
                clause[0].append( ( conjunct[ "predicate" ], *conjunct[ "args" ], ) )
            # negation of predicate
            elif conjunct[ "op" ] == "not":
                clause[1].append( ( conjunct["operand"][ "predicate" ], *conjunct["operand"][ "args" ], ) )
            # disjunction of predicates annd negations
            elif conjunct[ "op" ] == "or":
                for conjunct_disjunct in conjunct[ "operands" ]:
                    if "predicate" in conjunct_disjunct.keys():
                        clause[ 0 ].append( (conjunct_disjunct[ "predicate" ], *conjunct_disjunct[ "args" ],) )
                    # negation of predicate
                    elif conjunct_disjunct[ "op" ] == "not":
                        clause[ 1 ].append(
                            (conjunct_disjunct[ "operand" ][ "predicate" ], *conjunct_disjunct[ "operand" ][ "args" ],) )
            else:
                raise( "not CNF form")
            clause_list.append( clause )
    # disjunction
    elif cnf_precondition[ "op" ] == "or":
        clause = ([ ], [ ])
        for disjunct in cnf_precondition[ "operands" ]:
            if "predicate" in disjunct.keys():
                clause[ 0 ].append( (disjunct[ "predicate" ], *disjunct[ "args" ],) )
            # negation of predicate
            elif disjunct[ "op" ] == "not":
                clause[ 1 ].append(
                    (disjunct[ "operand" ][ "predicate" ], *disjunct[ "operand" ][ "args" ],) )
        clause_list = [ clause ]
    else:
        raise( "unsupport op found while making clause list")
    return clause_list

# iteration optimizer
# NEEDS INTEGRATION AND TESTING
# NEED WAY TO CONVERT PREDICATES INTO CNF
predicate_to_var_set = lambda x: { *x[ 1: ] }
clause_to_var_set_set = lambda x: { predicate_to_var_set( predicate ) for predicate in x }
var_set_set_flatten = lambda x: set().update( *x )
clause_to_var_set = lambda x: var_set_set_flatten( clause_to_var_set_set( x ) )
count_intersection_size = lambda x, y: len( y.intersect_update( clause_to_var_set( x ) ) )

def iteration_optimizer( unbound_vars: List[str], clauses: List[Tuple[List,List]] ):
    # need iteration for all unbound vars
    ordering = []
    while len( unbound_vars > 0 ):
        # get clauses with each unbound var
        var_clause_dict = dict()
        for var in unbound_vars:
            var_clause_dict[var] = set()
            for clause in clauses:
                # if variable in any predicate of clause associate clause with var
                if any( map( lambda x: var in x, [ *clause[0], *clause[ 1 ] ] ) ):
                    var_clause_dict.add( clause )
        # sort unbound variables by number of associated predicates
        # sort by size of union set of all unique unbound variable for all predicates associated with each variable
        # graph version: minimize increase in frontier size, pick vertex with smallest neighborhood discounting
        # for vertices that have already been picked or neighbor a pick
        unbound_vars.sort( key=lambda x: count_intersection_size( x, unbound_vars ) )

        # bind variable with fewest untouched neighbors
        binding_var = unbound_vars.pop(0)
        # get predicates that only have binding variable as unbound
        # these predicates are safe to check now as all variables will be grounded
        for var in unbound_vars:
            var_clause_dict[binding_var] -= var_clause_dict[var]
        ordering.append( ( binding_var, [*var_clause_dict[binding_var]] ) )
        # remove these predicates from list
        # dont do duplicate checks
        for clause in var_clause_dict[binding_var]:
            clauses.remove( clause )
    return ordering






if __name__ == '__main__':
    parser = HDDL_Parser()
    parser.parse_domain("domain.json")
    parser.write_domain()
    parser.parse_problem( "problem.json" )
    parser.write_problem()
    from domain.actions import actions
    from domain.methods import methods
    from problem import init_state, task_list
    planner = IPyHOP(methods, actions)
    plan = planner.plan( init_state, task_list, verbose=3 )
    print(plan)