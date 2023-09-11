# this file allows for hddl file to be read in and converted to python friendly representation
import io
import re
import json
from copy import deepcopy
import os
from typing import List, Dict, Union, Set, Tuple
from ipyhop import State, IPyHOP
from functools import partial
import time
import networkx as nx
import importlib
from multiprocessing import Pool, cpu_count
import numpy as np
import matplotlib.pyplot as plt
import cProfile, pstats, io
from pstats import SortKey

# if used an actions will give all mutating states
# we can avoid copying all other state properties
# curry in rigid dictionary
# easy to identify what properties need to be in state (they mutate)
# UNUSED
re_state_collect = re.compile( "rigid\.([\w_]+)\.(?=add|remove)" )
re_state_replace = re.compile( "rigid\.([\w_]+)(?=[\W\.])" )


# replace all statements of rigid.<predicate> with state.<predicate> if
#  <predicate> can mutate
def state_str_replacer( match_obj, mutable ):
    if match_obj.group( 1 ) in mutable:
        return "state." + match_obj.group( 1 )
    else:
        return match_obj.group( 0 )


# takes PDDL strings and makes them assignable to python boundVars
def clean_string( input_str: str ) -> str:
    # ? must be removed
    new_str = input_str.replace( "?", "" )
    # - must be replaced with _
    new_str = new_str.replace( "-", "_" )
    # PDDL is case insensitive so we are going to make everything lower case
    new_str = new_str.lower()
    return new_str


class HDDL_Parser:
    def __init__( self ):
        self.domain_dict = None
        self.problem_dict = None
        self.mutable = set()

    def parse_domain( self, domain_json_path: str ) -> None:
        # read json as dictionary
        with open( domain_json_path ) as f:
            domain_dict = json.load( f )
        self.domain_dict = domain_dict
        actions_str = ""
        # for every action in actions
        for action in domain_dict[ "actions" ]:
            # append action function to actions.py str
            actions_str += make_action_function_str( action )

        # note all state components that are never modified in actions
        self.mutable = set( re_state_collect.findall( actions_str ) )
        return

    def parse_problem( self, problem_json_path: str ) -> None:
        # read json as dictionary
        with open( problem_json_path ) as f:
            problem_dict = json.load( f )
        # print(problem_dict)
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

    def write_domain( self, dir_path: str = "." ) -> None:
        # create domain dict copy
        domain_dict = deepcopy( self.domain_dict )
        # create folder
        domain_path = dir_path + "/domain"
        # write actions.py
        actions_str = "from ipyhop import Actions\nimport itertools\n"

        # for every action in actions
        for action in domain_dict[ "actions" ]:
            # append action function to actions.py str
            actions_str += make_action_function_str( action )
        # Create a IPyHOP Actions object
        # NEED TO RESERVE KEYWORDS: actions, methods

        actions_str += "\nactions = Actions()\n"
        actions_str += "actions.declare_actions( [ "
        for action in domain_dict[ "actions" ]:
            actions_str += clean_string( action[ "name" ] ) + ", "
        actions_str += "] )\n"

        # replace all instances of mutables
        actions_str = re_state_replace.sub( lambda x: state_str_replacer( x, self.mutable ), actions_str )
        with open( domain_path + "/actions.py", "w" ) as actions_file:
            actions_file.write( actions_str )
        # write methods.py
        methods_str = "from ipyhop import Methods\nimport itertools\n"
        # for every method in methods
        task_method_dict = dict()
        for method in domain_dict[ "methods" ]:
            # append method function to methods.py str
            methods_str += make_method_function_str( method, domain_dict )
            # build task_method_dict
            if clean_string( method[ "task" ][ "taskName" ] ) not in task_method_dict.keys():
                task_method_dict[ clean_string( method[ "task" ][ "taskName" ] ) ] = set()
            task_method_dict[ clean_string( method[ "task" ][ "taskName" ] ) ].add( clean_string( method[ "name" ] ) )
        # Create a IPyHOP Methods object
        methods_str += "\nmethods = Methods()\n"
        # associate methods to tasks
        for task, method_set in task_method_dict.items():
            methods_str += "methods.declare_task_methods( '" + task + "', [ "
            for method in method_set:
                methods_str += method + ", "
            methods_str += "] )\n"
        # replace rigid with state for mutable
        methods_str = re_state_replace.sub( lambda x: state_str_replacer( x, self.mutable ), methods_str )
        with open( domain_path + "/methods.py", "w" ) as methods_file:
            methods_file.write( methods_str )

    def write_problem( self, output_path: str = "./problem.py" ) -> None:
        # create dict copies
        problem_dict = deepcopy( self.problem_dict )
        domain_dict = deepcopy( self.domain_dict )
        # make and save state and task network for easy load at runtime
        init_state_str = ""
        init_state_str += "from ipyhop import State\n\n"
        init_state_str += "state = State( 'init_state' )\n"
        init_state_str += "rigid = State( 'rigid' )\n"
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
            init_state_str += "rigid." + type + " = "
            init_state_str += str( typed_sets[ type ] ) + "\n"
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
            init_state_str += "rigid." + name + " = { "
            for args in atom_arg_dict[ name ]:
                init_state_str += str( args ) + ", "
            init_state_str += "}\n"

        # replace rigid with state for mutable
        init_state_str = re_state_replace.sub( lambda x: state_str_replacer( x, self.mutable ), init_state_str )

        with open( output_path, "w" ) as f:
            f.write( init_state_str )

        # write tasks in order as tuples
        task_list_str = ""
        tasks = problem_dict[ "htn" ][ "orderedSubtasks" ]
        task_list = [ (task[ "taskName" ], *task[ "args" ]) for task in tasks ]
        task_list_str += "\ntask_list = "
        task_list_str += str( task_list ) + "\n"

        # replace rigid with state for mutable (this one may uneeded)
        task_list_str = re_state_replace.sub( lambda x: state_str_replacer( x, self.mutable ), task_list_str )
        with open( output_path, "a" ) as f:
            f.write( task_list_str )


# add N number of tabs for every line in string
def tabify( input_str: str, N: int ):
    return ("\n" + N * '\t').join( (input_str).splitlines() )


# takes text representation of actions.py and appends action
# act: Dict representing a single action template
# actions_str: text representation of existing actions.py file
def make_action_function_str( action: Dict[ str, Union[ str, Dict ] ] ) -> str:
    # space out actions
    actions_str = "\n"
    # def <action_name>( state, *parameter_names ):
    actions_str += "def " + clean_string( action[ "name" ] ) + "( state"
    parameters = action[ "parameters" ]
    parameter_names = map( lambda x: clean_string( x[ "name" ] ), parameters )
    for parameter_name in parameter_names:
        actions_str += ", " + parameter_name
    actions_str += ", rigid ):\n"
    # if precondition
    # def <op>( *<operands> ) | (*<args>) in state[<predicate>] :
    precondition = action[ "precondition" ]
    actions_str += "\tif " + make_precondition_str( precondition ) + ":"
    # print( make_precondition_str( precondition ) )
    # effect
    # add and delete from state in order
    effect = action[ "effect" ]
    if effect != None:
        actions_str += make_effects_str( effect )
    actions_str += "\n\t\treturn state\n"
    return actions_str


# takes text representation of methods.py and appends method
# method: Dict representing a single method template
# methods_str: text representation of existing methods.py file
def make_method_function_str( method: Dict[ str, Union[ str, Dict ] ],
                              domain_dict: Dict[ str, Union[ str, Dict ] ] ) -> str:
    # space out methods
    methods_str = "\n"

    parameters = method[ "parameters" ]
    parameter_names = [ *map( lambda x: clean_string( x[ "name" ] ), parameters ) ]

    # iterate over valid parameter groundings
    # parameters from task are fixed, but all other parameters are only limited by preconditions
    # and typing
    task_parameter_names = [ *map( lambda x: clean_string( x ), method[ "task" ][ "args" ] ) ]
    parameter_set_diff = { *parameter_names } - { *task_parameter_names }
    parameter_set_diff = list( parameter_set_diff )
    parameter_set_diff.sort()
    # dict to get type with parameter name
    parameter_name_type_dict = { }
    for parameter in parameters:
        parameter_name_type_dict[ clean_string( parameter[ "name" ] ) ] = clean_string( parameter[ "type" ] )

    # def <method_name>( state, *parameter_names ):
    # we cant have boundVars in the method signature not defined by the task
    methods_str += "def " + clean_string( method[ "name" ] ) + "( state"
    # print(task_parameter_names)
    # deal with duplicates
    # relabel all occurrences after first and alter precondition to require equality
    precondition_equalities = set()
    for i in range( len( task_parameter_names ) ):
        check_name = task_parameter_names[ i ]
        count = 0
        for j in range( i + 1, len( task_parameter_names ) ):
            curr_name = task_parameter_names[ j ]
            if check_name == curr_name:
                count += 1
                task_parameter_names[ j ] = task_parameter_names[ j ] + "___" + str( count )
                precondition_equalities.add( (i, j) )

    for parameter_name in task_parameter_names:
        methods_str += ", " + parameter_name
    methods_str += ", rigid ):\n"

    # nesting type iteration loops in alphabetic order

    for i, parameter_name in enumerate( parameter_set_diff ):
        methods_str += "\t" * (i + 1)
        methods_str += "for " + parameter_name + " in rigid." + parameter_name_type_dict[ parameter_name ] + ":\n"
    # print( iteration_optimizer( [*parameter_set_diff], ))

    # if precondition
    # def <op>( *<operands> ) | (*<args>) in state[<predicate>] :
    precondition = method[ "precondition" ]
    # print(precondition)
    # clause_list = make_clause_cnf_list(precondition)
    # print(clause_list)
    # print(iteration_optimizer(parameter_set_diff,clause_list))

    # cnf_precondition = make_precondition_cnf(precondition)
    if precondition != None:
        if len( precondition_equalities ) == 0:
            # print(parameter_set_diff)
            # print(precondition)
            methods_str += (len( parameter_set_diff ) + 1) * "\t" + "if " + make_precondition_str(
                precondition ) + ":\n"
        else:
            methods_str += (len( parameter_set_diff ) + 1) * "\t" + "if " + "all( [" + make_precondition_str(
                precondition ) + ", "
            for t_l, f_l in precondition_equalities:
                methods_str += task_parameter_names[ t_l ] + " == " + task_parameter_names[ f_l ] + ", "
            methods_str += "] ):\n"

        # yield statement with task network
        methods_str += (len( parameter_set_diff ) + 2) * "\t" + "yield " + \
                       make_task_network_str( method[ "taskNetwork" ][ "orderedSubtasks" ] ) + "\n"
    else:
        if len( precondition_equalities ) == 0:
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
def make_precondition_str( precondition: Dict[ str, Union[ str, Dict ] ] ) -> str:
    # print(precondition)
    # precondition with operation
    if "op" in precondition.keys():
        op = precondition[ "op" ]

        # all operands must be true
        if op == "and":
            operands = precondition[ "operands" ]
            precondition_str = "all( [ "
            for operand in operands:
                precondition_str += make_precondition_str( operand ) + ", "
            precondition_str += "] )"
            return precondition_str
        # operand must be false`
        elif op == "not":
            operand = precondition[ "operand" ]
            return "not( " + make_precondition_str( operand ) + " )"
        # universal quantification
        elif op == "forall":
            boundVars = precondition[ "boundVars" ]
            boundVar_tuples = [ (boundVar[ "name" ], boundVar[ "type" ]) for boundVar in boundVars ]
            boundVar_names, boundVar_types = list( zip( *boundVar_tuples ) )
            operand = precondition[ "operand" ]
            forall_str = "all( " + make_precondition_str( operand ) + " for ( "
            for boundVar_name in boundVar_names:
                forall_str += clean_string( boundVar_name ) + ", "
            forall_str += ") in itertools.product( "
            for boundVar_type in boundVar_types:
                forall_str += "rigid." + clean_string( boundVar_type ) + ", "
            forall_str += ") )"
            return forall_str
        else:
            raise (op + " is an unsupported op for precondition!")
    # predicate precondition
    else:
        predicate = precondition[ "predicate" ]
        args = precondition[ "args" ]
        # equality predicate
        if predicate == "=":
            if (len( args ) != 2):
                raise ("only supports binary equality predicate")
            predicate_str = "( " + clean_string( args[ 0 ] ) + " == " + clean_string( args[ 1 ] ) + " )"
        # standard predicate
        else:
            predicate_str = "( "
            for arg in args:
                # print(arg)
                predicate_str += clean_string( arg ) + ", "
            predicate_str += ") in " + "rigid." + clean_string( predicate )
        return predicate_str


# recursively write effect expressions in equivalent python syntax
def make_effects_str( effects: Dict[ str, Union[ str, Dict ] ], tab_level=0 ) -> str:
    # effects with operation
    if "op" in effects.keys():
        op = effects[ "op" ]

        # all operands will occur
        if op == "and":
            operands = effects[ "effects" ]
            effects_str = ""
            for operand in operands:
                effects_str += "\n\t\t" + make_effects_str( operand )
            return effects_str
        # operand will remove predicate
        elif op == "not":
            operand = effects[ "effect" ]
            if "predicate" not in operand.keys():
                raise ("When used as an effect, 'not' must have single predicate as operand")
            predicate = operand[ "predicate" ]
            args = operand[ "args" ]
            predicate_str = "rigid." + clean_string( predicate ) + ".remove( ( "
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
        predicate_str = "rigid." + predicate + ".add( ( "
        for arg in args:
            predicate_str += clean_string( arg ) + ", "
        predicate_str += ") )"
        return predicate_str


# make string for single task
def make_task_str( task: Dict[ str, Union[ str, Dict ] ] ) -> str:
    taskName = task[ "taskName" ]
    args = task[ "args" ]
    predicate_str = "( '" + clean_string( taskName ) + "', "
    for arg in args:
        predicate_str += clean_string( arg ) + ", "
    predicate_str += ")"
    return predicate_str


# make string for task network
def make_task_network_str( tasks: List[ Dict[ str, Union[ str, Dict ] ] ] ) -> str:
    # empty
    if len( tasks ) == 1 and tasks[ 0 ][ "taskName" ] == "nil":
        return "[ ]"
    # string the task tuples together
    task_net_str = "[ "
    for task in tasks:
        task_net_str += make_task_str( task ) + ", "
    task_net_str += "]"
    return task_net_str


# # make precondition cnf
# def make_precondition_cnf( precondition: Dict[str,Union[str,Dict]] ) -> Dict[str,Union[str,Dict]]:
#     # move negations downward until either negation of simple predicate or doubly negated and removed
#     # BFS while calling negation helper when we encounter negation
#     if precondition != None:
#         new_precondition = cnf_negation_helper( precondition )
#     else:
#         new_precondition = None
#         return new_precondition
#     # move ors downward until only disjunction of predicates and negations of predicates
#     # BFS while calling disjunction helper when we encounter disjunction
#     new_precondition = cnf_disjunction_helper( new_precondition )
#     return new_precondition
#
# # propagates negation downward
# def cnf_negation_helper( precondition: Dict[str,Union[str,Dict]] ):
#     if "op" in precondition.keys() and precondition[ "op" ] == "not":
#         # do nothing single predicate negation
#         if "operand" in precondition.keys() and "predicate" in precondition["operand"].keys():
#             return precondition
#         # negate negation and continue downward
#         elif "operand" in precondition.keys() and precondition["operand"][ "op" ] == "not":
#             return cnf_negation_helper( precondition[ "operand" ][ "operand" ] )
#         # propagate negation over conjunction
#         elif precondition["operand"][ "op" ] == "and":
#             return {
#                 "op": "or",
#                 "operands": [
#                     cnf_negation_helper( {
#                         "op": "not",
#                         "operand": operand
#                     } ) for operand in precondition[ "operands" ]
#                 ]
#             }
#         # propagate negation over disjunction
#         elif precondition[ "op" ] == "or":
#             return {
#                 "op": "and",
#                 "operands": [
#                     cnf_negation_helper( {
#                         "op": "not",
#                         "operand": operand
#                     } ) for operand in precondition[ "operands" ]
#                 ]
#             }
#         else:
#             raise( "unsupported precondition encountered during negation propagation")
#     else:
#         return precondition
#
#
# # propagates disjunction downward
# # merge nested ors and propagate over ands
# def cnf_disjunction_helper( precondition: Dict[str,Union[str,Dict]] ):
#     if "op" in precondition.keys() and precondition[ "op" ] == "or":
#         # pull descendant ors to top
#         # iterate over operands if or encountered, pop that operand and append to back
#         new_or_precondition = {
#             "op": "or",
#             "operands": []
#         }
#         for operand in precondition[ "operands" ]:
#             # remove and append operands to top
#             if "op" in operand.keys() and operand[ "op" ] == "or":
#                 new_or_precondition["operands"] += [ *map( cnf_disjunction_helper, operand[ "operands" ] ) ]
#             # do nothing
#             else:
#                 new_or_precondition["operands"].append( cnf_disjunction_helper( operand ) )
#
#         # merge subordinate ands into single subordinate and
#
#         new_and = {
#             "op": "and",
#             "operands": [ ]
#         }
#         if any( map( lambda x: "op" in x.keys() and x[ "op" ] == "and", new_or_precondition[ "operands" ] ) ):
#
#             new_and_precondition = {
#                 "op": "or",
#                 "operands": [
#                     new_and
#                 ]
#             }
#             for operand in new_or_precondition[ "operands" ]:
#                 # remove and append operands to top
#                 if "op" in operand.keys() and operand[ "op" ] == "and":
#                     new_and[ "operands" ] += [ *map( cnf_disjunction_helper, operand[ "operands" ] ) ]
#                 # do nothing
#                 else:
#                     new_and_precondition["operands"].append( cnf_disjunction_helper( operand ) )
#         else:
#             new_and_precondition = {
#                 "op": "or",
#                 "operands": [
#                 ]
#             }
#
#
#         # replace current with and where the operands are now or statements with each such statement containing all the
#         # non-and original operands with a single operand from the and operands
#         new_precondition = {
#             "op": "and",
#             "operands": [
#             ]
#         }
#         new_and_precondition[ "operands" ] = [ *filter( lambda x: "op" in x.keys() and x[ "op" ] != "and",
#                                                    new_and_precondition[ "operands" ] ) ]
#         for operand in new_and[ "operands" ]:
#             new_precondition[ "operands" ].append(
#                 {
#                     "op": "or",
#                     "operands": [
#                         operand,
#                         *map( cnf_disjunction_helper, new_and_precondition[ "operands" ] )
#                     ]
#                 }
#             )
#         return new_precondition
#     else:
#         return precondition

# take predicate tree and return CNF as list of clauses
# clauses dictate how predicates are evaluated together
# IN PROGRESS
def make_clause_cnf_list( precondition: Dict[ str, Union[ str, Dict ] ] ) -> List[ Tuple[ List, List ] ]:
    # simplify to CNF
    # cnf_precondition = make_precondition_cnf( deepcopy( precondition ) )
    cnf_precondition = deepcopy( precondition )
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
        clause_list = [ ([ (clean_string( cnf_precondition[ "predicate" ] ),
                            *map( clean_string, cnf_precondition[ "args" ] ),), ], [ ]) ]
    # negation of predicate
    elif cnf_precondition[ "op" ] == "not":
        clause_list = [ ([ ], [ (clean_string( cnf_precondition[ "operand" ][ "predicate" ] ),
                                 *map( clean_string, cnf_precondition[ "operand" ][ "args" ] ),), ]) ]
    # conjunction
    elif cnf_precondition[ "op" ] == "and":
        clause_list = [ ]
        for conjunct in cnf_precondition[ "operands" ]:
            clause = ([ ], [ ])
            if "predicate" in conjunct.keys():
                clause[ 0 ].append(
                    (clean_string( conjunct[ "predicate" ] ), *map( clean_string, conjunct[ "args" ] ),) )
            # negation of predicate
            elif conjunct[ "op" ] == "not":
                clause[ 1 ].append( (clean_string( conjunct[ "operand" ][ "predicate" ] ),
                                     *map( clean_string, conjunct[ "operand" ][ "args" ] ),) )
            # disjunction of predicates annd negations
            elif conjunct[ "op" ] == "or":
                for conjunct_disjunct in conjunct[ "operands" ]:
                    if "predicate" in conjunct_disjunct.keys():
                        clause[ 0 ].append( (clean_string( conjunct_disjunct[ "predicate" ] ),
                                             *map( clean_string, conjunct_disjunct[ "args" ] ),) )
                    # negation of predicate
                    elif conjunct_disjunct[ "op" ] == "not":
                        clause[ 1 ].append(
                            (clean_string( conjunct_disjunct[ "operand" ][ "predicate" ] ),
                             *map( clean_string, conjunct_disjunct[ "operand" ][ "args" ] ),) )
            else:
                raise (Exception( "not CNF form" ))
            clause_list.append( (tuple( clause[ 0 ] ), tuple( clause[ 1 ] )) )
    # disjunction
    elif cnf_precondition[ "op" ] == "or":
        clause = ([ ], [ ])
        for disjunct in cnf_precondition[ "operands" ]:
            if "predicate" in disjunct.keys():
                clause[ 0 ].append(
                    (clean_string( disjunct[ "predicate" ] ), *map( clean_string, disjunct[ "args" ] ),) )
            # negation of predicate
            elif disjunct[ "op" ] == "not":
                clause[ 1 ].append(
                    (clean_string( disjunct[ "operand" ][ "predicate" ] ),
                     *map( clean_string, disjunct[ "operand" ][ "args" ] ),) )
        clause_list = [ clause ]
    else:
        raise (Exception( "unsupport op found while making clause list: " + cnf_precondition[ "op" ] ))

    return clause_list


# iteration optimizer
# NEEDS INTEGRATION AND TESTING
# NEED WAY TO CONVERT PREDICATES INTO CNF
predicate_to_boundVar_set = lambda x: { *x[ 1: ] }
clause_to_boundVar_set_list = lambda x: [ predicate_to_boundVar_set( predicate ) for predicate in x ]
boundVar_set_list_flatten = lambda x: set().union( *x )
clause_to_boundVar_set = lambda x: boundVar_set_list_flatten( clause_to_boundVar_set_list( x ) )
count_intersection_size = lambda x, y: len( y.intersection( clause_to_boundVar_set( x ) ) )


def iteration_optimizer( unboundVars: List[ str ], clauses: List[ Tuple[ List, List ] ] ):
    # need iteration for all unbound boundVars
    ordering = [ ]
    while len( unboundVars ) > 0:
        # get clauses with each unbound boundVar
        boundVar_clause_dict = dict()
        for unboundVar in unboundVars:
            boundVar_clause_dict[ unboundVar ] = set()
            for clause in clauses:
                print( clause )
                # if boundVar in any predicate of clause associate clause with boundVar
                if any( map( lambda x: unboundVar in x, [ *clause[ 0 ], *clause[ 1 ] ] ) ):
                    boundVar_clause_dict[ unboundVar ].update( clause )
        print( boundVar_clause_dict )
        # sort unbound boundVars by number of associated predicates
        # sort by size of union set of all unique unbound boundVar for all predicates associated with each boundVar
        # graph version: minimize increase in frontier size, pick vertex with smallest neighborhood discounting
        # for vertices that have already been picked or neighbor a pick
        unboundVars.sort( key=lambda x: count_intersection_size( x, set( unboundVars ) ) )

        # bind boundVar with fewest untouched neighbors
        bindingVar = unboundVars.pop( 0 )
        # get predicates that only have binding boundVar as unbound
        # these predicates are safe to check now as all boundVars will be grounded
        for unboundVar in unboundVars:
            boundVar_clause_dict[ bindingVar ] -= boundVar_clause_dict[ unboundVar ]
        ordering.append( (bindingVar, [ *boundVar_clause_dict[ bindingVar ] ]) )
        # remove these predicates from list
        # dont do duplicate checks
        for boundClause in boundVar_clause_dict[ bindingVar ]:
            clauses.remove( boundClause )
    return ordering


def run_experiment( problem_json ):
    print( problem_json )

    parser = HDDL_Parser()
    parser.parse_domain( "Snake/domain/domain.json" )
    from Snake.domain.actions import actions
    from Snake.domain.methods import methods
    parser.parse_problem( "Snake/problems/" + problem_json )
    output_py = problem_json.replace( "snake.json", "py" )
    output_txt = problem_json.replace( "snake.json", "txt" )
    parser.write_problem( "Snake/problems_py/" + output_py )
    # read in initial state, task list, and rigid
    temp_mod = importlib.import_module( "Snake.problems_py." + output_py[ :-3 ] )
    init_state = temp_mod.state
    task_list = temp_mod.task_list
    rigid = temp_mod.rigid
    # print(init_state)
    # print(task_list)
    # print(rigid)
    # update methods and actions to use rigid
    local_methods = deepcopy( methods )
    local_actions = deepcopy( actions )

    local_methods.goal_method_dict.update(
        { l: [ partial( m, rigid=rigid ) for m in ms ] for l, ms in local_methods.goal_method_dict.items() } )
    local_methods.task_method_dict.update(
        { l: [ partial( m, rigid=rigid ) for m in ms ] for l, ms in local_methods.task_method_dict.items() } )
    local_methods.multigoal_method_dict.update(
        { l: [ partial( m, rigid=rigid ) for m in ms ] for l, ms in local_methods.multigoal_method_dict.items() } )
    local_actions.action_dict.update( { l: partial( a, rigid=rigid ) for l, a in local_actions.action_dict.items() } )

    # get plan
    try:
        planner = IPyHOP( local_methods, local_actions )
    except:
        print("Something went wrong for " + problem_json)
    # print(init_state)

    start_time = time.process_time_ns()
    plan = planner.plan( init_state, task_list, verbose=0 )
    end_time = time.process_time_ns()
    total_time = (end_time - start_time) / 1E9
    # write problem and plan to file (name should be the same as the original json file with .py extension)
    with open( "Snake/solutions/" + output_txt, "w" ) as f:
        f.write( str( plan ) )
    print( (problem_json, total_time, plan) )
    return (problem_json, total_time, plan)


if __name__ == '__main__':
    problem_json="pb-32slots-seed1.snake.json"
    output_py = problem_json.replace( "snake.json", "py" )
    output_txt = problem_json.replace( "snake.json", "txt" )
    # test domain
    parser = HDDL_Parser()
    parser.parse_domain("Snake/domain/domain.json")
    # parser.write_domain()
    parser.parse_problem( "Snake/problems/" + problem_json )
    parser.write_problem("Snake/problems_py/" + output_py)
    from Snake.domain.actions import actions
    from Snake.domain.methods import methods

    temp_mod = importlib.import_module( "Snake.problems_py." + output_py[ :-3 ] )
    init_state = temp_mod.state
    task_list = temp_mod.task_list
    rigid = temp_mod.rigid
    local_methods = deepcopy( methods )
    local_actions = deepcopy( actions )

    local_methods.goal_method_dict.update(
        { l: [ partial( m, rigid=rigid ) for m in ms ] for l, ms in local_methods.goal_method_dict.items() } )
    local_methods.task_method_dict.update(
        { l: [ partial( m, rigid=rigid ) for m in ms ] for l, ms in local_methods.task_method_dict.items() } )
    local_methods.multigoal_method_dict.update(
        { l: [ partial( m, rigid=rigid ) for m in ms ] for l, ms in local_methods.multigoal_method_dict.items() } )
    local_actions.action_dict.update( { l: partial( a, rigid=rigid ) for l, a in local_actions.action_dict.items() } )
    planner = IPyHOP(local_methods, local_actions)
    # start_time = time.perf_counter_ns()
    #############################################################################
    pr = cProfile.Profile()
    pr.enable()
    ################################################################################
    plan = planner.plan( init_state, task_list, verbose=0)
    ###################################################################################
    pr.disable()
    s = io.StringIO()
    sortby = "tottime"
    ps = pstats.Stats( pr, stream=s ).sort_stats( sortby )
    ps.print_stats()
    print( s.getvalue() )
    #################################################################################
    # end_time = time.perf_counter_ns()
    # total_time = (end_time - start_time) / 1E9
    print(plan)
    # print(total_time)

    with open( "Snake/solutions/" + output_txt, "w") as f:
        f.write(str(plan))
    # args = [ *filter( lambda x: "1.snake.json" in x, os.listdir( "Snake/problems" ) ) ]
    # args_dict = dict()
    # for arg in args:
    #     try:
    #         args_dict[arg] = int(arg[3:5])
    #     except:
    #         args_dict[ arg ] = int( arg[ 3 ] )
    # args.sort(key=lambda x: args_dict[x])
    # print(args)
    # time_arr = np.ndarray( len( args ), dtype=float )
    # plan_len_arr = np.empty_like( time_arr, dtype=int )
    # with Pool( processes=cpu_count() // 2 ) as pool:
    #     output = pool.map_async( run_experiment, args, chunksize=1 )
    #     while True:
    #         if output.ready():
    #             break
    #         print( str( round( 100 - 100 * output._number_left / len( args ), 3 ) ) + " %" )
    #         time.sleep( 60 )
    # i = 0
    # for exp in output.get():
    #     time_arr[ i ] = exp[ 1 ]
    #     plan_len_arr[ i ] = exp[ 2 ]
    #     i += 1
    # print(time_arr)
    # print(plan_len_arr)
    # plt.scatter(time_arr,plan_len_arr)
    # plt.show()