# this file allows for hddl file to be read in and converted to python friendly representation
# import io
import importlib
import json
import keyword
import os
import re
import time
from copy import deepcopy
from functools import partial
from pathlib import Path
from typing import Dict, List, Set, Union

import networkx as nx
from ipyhop import IPyHOP

# from multiprocessing import Pool, cpu_count
# import numpy as np
# import matplotlib.pyplot as plt
# import cProfile, pstats, io
# from pstats import SortKey
# from ipyhop.actor import Actor
# from ipyhop.mc_executor import MonteCarloExecutor

# regex for identifying what predicates can be mutated
re_state_collect = re.compile( "rigid\.([\w_]+)\.(?=add|remove)" )
# regex for moving mutable predicates from rigid dict to mutable state
re_state_replace = re.compile( "rigid\.([\w_]+)(?=[\W\.])" )
# regex for replacing constants with literals
re_constant_replace = re.compile( "(\w+)," )


def state_str_replacer( match_obj: re.Match, mutable: Set[ str ] ) -> str:
    """ replace all statements of rigid.<predicate> with state.<predicate> if <predicate> is in mutable

    Parameters
    ----------
    match_obj : re.Match

    mutable :   Set[str]
                Set containing the names of all mutable predicates

    Returns
    -------
    str
                Either original str if predicate is immutable or the string with "rigid" substituted
                with "state" if mutable
    """
    if match_obj.group( 1 ) in mutable:
        return "state." + match_obj.group( 1 )
    else:
        return match_obj.group( 0 )


#
def constant_str_replacer( match_obj: re.Match, constant_set: Set[ str ] ) -> str:
    """ replace all defined constants with equivalent string literals

        Parameters
        ----------
        match_obj : re.Match

        mutable :   Set[str]
                    Set containing the names of all constants

        Returns
        -------
        str
                    Either original str if not constant else original string with string literal of constant
    """
    if match_obj.group( 1 ) in constant_set:
        return "'" + match_obj.group( 1 ) + "',"
    else:
        return match_obj.group( 0 )


def clean_string( input_str: str ) -> str:
    """ takes str and makes them assignable to python variables

    Parameters
    ----------
    input_str : str

    Returns
    -------
    str
                python-friendly version of string

    """
    # ? must be removed
    new_str = input_str.replace( "?", "" )
    # ! must be removed
    new_str = new_str.replace( "!", "" )
    # - must be replaced with _
    new_str = new_str.replace( "-", "__" )
    # PDDL is case insensitive so we are going to make everything lower case
    new_str = new_str.lower()
    # we cannot allow keywords
    if keyword.iskeyword( new_str ):
        new_str += "___"
    # remove leading and trailing
    new_str = new_str.strip()
    return new_str


class HDDL_Parser:
    def __init__( self ):
        self.domain_dict = None
        self.problem_dict = None
        self.mutable = set()
        self.typed_sets = dict()
        self.constant_set = set()

    def parse_domain( self, domain_json_path: str, deviation_possible_predicates: List[ str ] = None ) -> None:
        # read json as dictionary
        with open( domain_json_path ) as f:
            domain_dict = json.load( f )
        self.domain_dict = domain_dict
        actions_str = ""
        # for every action in actions
        for action in domain_dict[ "actions" ]:
            # append action function to actions.py str
            actions_str += make_action_function_str( action )
        # # for ever deviation in deviations
        # deviations_str = ""
        # for deviation in domain_dict["deviations"]:
        #     # append deviations function to deviations.py str
        #     deviations_str += make_deviation_function_str( deviation )

        # note all state components that are never modified in actions or deviations
        self.mutable = set( re_state_collect.findall( actions_str ) )
        # self.mutable |= set( re_state_collect.findall( deviations_str ) )
        if deviation_possible_predicates != None:
            self.mutable |= { *map( lambda x: clean_string( x ), deviation_possible_predicates ) }

        # track domain constants
        # print(domain_dict["constants"])
        constants = domain_dict[ "constants" ]
        typed_sets = self.typed_sets
        constant_set = self.constant_set
        for const in constants:
            name = clean_string( const[ "name" ] )
            type = clean_string( const[ "type" ] )
            constant_set.add( name )
            if type not in typed_sets.keys():
                typed_sets[ type ] = set()
            typed_sets[ type ].add( name )

        # hddl map of cleaned names to original names
        # assumes uniqueness across types
        hddl_map = dict()
        # type hierarchy
        supertype_tuples = [ *map( lambda x: (x[ "supertype" ], x[ "type" ]), domain_dict[ "types" ] ) ]
        # constants
        constant_tuples = map( lambda x: (x[ "type" ], x[ "name" ]), domain_dict[ "constants" ] )
        # tasks
        task_tuples = map( lambda x: ("task", x[ "name" ]), domain_dict[ "tasks" ] )
        # methods
        method_tuples = map( lambda x: ("method", x[ "name" ]), domain_dict[ "methods" ] )
        # actions
        action_tuples = map( lambda x: ("action", x[ "name" ]), domain_dict[ "actions" ] )
        # # deviations
        # deviation_tuples = map( lambda x: ("deviation", x[ "name" ]), domain_dict[ "deviations" ] )
        # predicates
        predicate_tuples = [ *map( lambda x: ("predicate", x[ "name" ]), domain_dict[ "predicates" ] ) ]

        for type_str, name_str in [ *supertype_tuples, *constant_tuples, *task_tuples, *method_tuples, *action_tuples,
                                    *predicate_tuples ]:
            hddl_map[ clean_string( name_str ) ] = name_str
        predicate_set = set()
        for type_str, name_str in predicate_tuples:
            predicate_set.add( clean_string( name_str ) )
        clean_supertype_set = set( map( lambda x: (clean_string( x[ 0 ] ), clean_string( x[ 1 ] )), supertype_tuples ) )
        supertype_tree = nx.DiGraph()
        supertype_tree.add_edges_from( clean_supertype_set )
        self.hddl_map = hddl_map
        self.predicate_set = predicate_set
        self.supertype_tree = supertype_tree
        self.supertype_set = set( map( lambda x: x[ 0 ], clean_supertype_set ) )
        return

    def parse_problem( self, problem_json_path: str ) -> None:
        # read json as dictionary
        with open( problem_json_path ) as f:
            problem_dict = json.load( f )
        # print(problem_dict)
        self.problem_dict = problem_dict
        # hddl map of cleaned names to original names
        # objects
        object_tuples = map( lambda x: (x[ "type" ], x[ "name" ]), problem_dict[ "objects" ] )
        for type_str, name_str in object_tuples:
            self.hddl_map[ clean_string( name_str ) ] = name_str
        # print(self.hddl_map)
        return

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
        domain_path = os.path.join( dir_path, "domain" )
        if not os.path.isdir( domain_path ):
            p = Path( domain_path )
            p.mkdir( parents=True )
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
        # make all constants literals
        actions_str = re_constant_replace.sub( lambda x: constant_str_replacer( x, self.constant_set ), actions_str )
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
                task_method_dict[ clean_string( method[ "task" ][ "taskName" ] ) ] = [ ]
            task_method_dict[ clean_string( method[ "task" ][ "taskName" ] ) ].append(
                clean_string( method[ "name" ] ) )
        # Create a IPyHOP Methods object
        methods_str += "\nmethods = Methods()\n"
        # associate methods to tasks
        for task, method_list in task_method_dict.items():
            methods_str += "methods.declare_task_methods( '" + task + "', [ "
            for method in method_list:
                methods_str += method + ", "
            methods_str += "] )\n"
        # replace rigid with state for mutable
        methods_str = re_state_replace.sub( lambda x: state_str_replacer( x, self.mutable ), methods_str )
        # make all cosntants literals
        methods_str = re_constant_replace.sub( lambda x: constant_str_replacer( x, self.constant_set ), methods_str )

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
        # print( objs )
        typed_sets = self.typed_sets
        # object primitives
        for obj in objs:
            name = clean_string( obj[ "name" ] )
            type = clean_string( obj[ "type" ] )
            if type not in typed_sets.keys():
                typed_sets[ type ] = set()
            typed_sets[ type ].add( name )
        supertype_tree = self.supertype_tree
        # lists all object of type and of subtypes
        for supertype in supertype_tree.nodes:
            init_state_str += "rigid." + supertype + " = "
            desendant_types = { *nx.descendants( supertype_tree, supertype ), supertype }
            supertype_set = set()
            for type in desendant_types:
                if type in typed_sets.keys():
                    supertype_set |= typed_sets[ type ]
            init_state_str += str( supertype_set ) + "\n"

        # group atoms
        atom_arg_dict = dict()
        for atom in problem_dict[ "init" ]:
            name = clean_string( atom[ "predicate" ] )
            args = tuple( map( clean_string, atom[ "args" ] ) )
            if name not in atom_arg_dict.keys():
                atom_arg_dict[ name ] = set()
            atom_arg_dict[ name ].add( args )
        for pred in self.predicate_set - set( atom_arg_dict.keys() ):
            atom_arg_dict[ pred ] = set()
        # write atoms by predicate
        for name in atom_arg_dict.keys():
            init_state_str += "rigid." + name + " = set( ["
            for args in atom_arg_dict[ name ]:
                init_state_str += str( args ) + ", "
            init_state_str += "] )\n"

        # replace rigid with state for mutable
        init_state_str = re_state_replace.sub( lambda x: state_str_replacer( x, self.mutable ), init_state_str )

        with open( output_path, "w" ) as f:
            f.write( init_state_str )

        # write tasks in order as tuples
        task_list_str = ""
        tasks = problem_dict[ "htn" ][ "orderedSubtasks" ]
        task_list = [ (task[ "taskName" ], *task[ "args" ]) for task in tasks ]

        task_list = [ *map( lambda x: tuple( map( clean_string, x ) ), task_list ) ]
        # print( task_list )
        task_list_str += "\ntask_list = "
        task_list_str += str( task_list ) + "\n"

        # replace rigid with state for mutable (this one may uneeded)
        task_list_str = re_state_replace.sub( lambda x: state_str_replacer( x, self.mutable ), task_list_str )
        with open( output_path, "a" ) as f:
            f.write( task_list_str )


# add N number of tabs for every line in string
def tabify( input_str: str, N: int ):
    return ("\n" + N * '\t').join( (input_str).splitlines() )


# takes action JSON and outputs IPyHOPPER str representation
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
    actions_str += "\tif " + make_precondition_str( precondition ) + ":\n\t\t"
    # print( make_precondition_str( precondition ) )
    # effect
    # add and delete from state in order
    effect = action[ "effect" ]
    if effect != None:
        actions_str += make_effects_str( effect )
    actions_str += "\n\t\treturn state\n"
    return actions_str


# takes deviation JSON and outputs IPyHOPPER str representation
def make_deviation_function_str( deviation: Dict[ str, Union[ str, Dict ] ] ):
    # space out deviations
    deviations_str = "\n"
    # def <deviation_name>( state, *parameter_names ):
    deviations_str += "def " + clean_string( deviation[ "name" ] ) + "( state"
    parameters = deviation[ "parameters" ]
    parameter_names = map( lambda x: clean_string( x[ "name" ] ), parameters )
    for parameter_name in parameter_names:
        deviations_str += ", " + parameter_name
    deviations_str += ", rigid ):\n"
    # if precondition
    # def <op>( *<operands> ) | (*<args>) in state[<predicate>] :
    precondition = deviation[ "precondition" ]
    deviations_str += "\tif " + make_precondition_str( precondition ) + ":\n\t\t"
    # print( make_precondition_str( precondition ) )
    # effect
    # add and delete from state in order
    effect = deviation[ "effect" ]
    # deviations effect is single and with unforeseenPos as all single predicates and
    # unforeseenNeg as predicates in "not" operators
    unforeseenPos = effect[ "unforeseenPos" ]
    unforeseenNeg = effect[ "unforeseenNeg" ]
    new_operands = [ { "op": "not", "operands": x } for x in unforeseenNeg ]
    new_operands += unforeseenPos
    equiv_action_effect = {
        "op":       "and",
        "operands": new_operands
    }
    if effect != None:
        deviations_str += make_effects_str( equiv_action_effect )
    deviations_str += "\n\t\treturn state\n"
    return deviations_str


# takes method JSON and outputs IPyHOPPER str representation
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
    # print(task_parameter_names)
    # print(parameter_names)
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
    precondition = method[ "precondition" ] if "precondition" in method.keys() else None
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
        # existence
        elif op == "exists":
            boundVars = precondition[ "boundVars" ]
            boundVar_tuples = [ (boundVar[ "name" ], boundVar[ "type" ]) for boundVar in boundVars ]
            boundVar_names, boundVar_types = list( zip( *boundVar_tuples ) )
            operand = precondition[ "operand" ]
            exists_str = "any( " + make_precondition_str( operand ) + " for ( "
            for boundVar_name in boundVar_names:
                exists_str += clean_string( boundVar_name ) + ", "
            exists_str += ") in itertools.product( "
            for boundVar_type in boundVar_types:
                exists_str += "rigid." + clean_string( boundVar_type ) + ", "
            exists_str += ") )"
            return exists_str
        elif op == "imply":
            operand1 = precondition[ "operand1" ]
            operand2 = precondition[ "operand2" ]
            equivalent_precondition = {
                "op":       "or",
                "operands": [
                    {
                        "op":      "not",
                        "operand": operand1
                    },
                    operand2
                ]
            }
            return make_precondition_str( equivalent_precondition )
        # at least 1 operand must be true
        elif op == "or":
            operands = precondition[ "operands" ]
            precondition_str = "any( [ "
            for operand in operands:
                precondition_str += make_precondition_str( operand ) + ", "
            precondition_str += "] )"
            return precondition_str
        else:
            raise ValueError( op + " is an unsupported op for precondition!" )
    # predicate precondition
    else:
        predicate = precondition[ "predicate" ]
        args = precondition[ "args" ]
        # equality predicate
        if predicate == "=":
            if (len( args ) != 2):
                raise ValueError( "only supports binary equality predicate" )
            predicate_str = "( " + clean_string( args[ 0 ] ) + " == " + clean_string( args[ 1 ] ) + " )"
        # inequality predicate
        elif predicate == "different":
            if (len( args ) != 2):
                raise ValueError( "only supports binary inequality predicate" )
            predicate_str = "( " + clean_string( args[ 0 ] ) + " != " + clean_string( args[ 1 ] ) + " )"
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
            effects_str += make_effects_str( operands[ 0 ] )
            for operand in operands[ 1: ]:
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
        # effect only when condition
        elif op == "when":
            condition = effects[ "condition" ]
            effect = effects[ "effect" ]
            return make_effects_str( effect ) + " if " + make_precondition_str( condition ) + " else None"
        else:
            raise ValueError( op + " is an unsupported op for effects!" )
    # predicate effects
    else:
        predicate = clean_string( effects[ "predicate" ] )
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

# # take predicate tree and return CNF as list of clauses
# # clauses dictate how predicates are evaluated together
# # IN PROGRESS
# def make_clause_cnf_list( precondition: Dict[ str, Union[ str, Dict ] ] ) -> List[ Tuple[ List, List ] ]:
#     # simplify to CNF
#     # cnf_precondition = make_precondition_cnf( deepcopy( precondition ) )
#     cnf_precondition = deepcopy( precondition )
#     # make into list
#     clause_list = [ ]
#     # PREDICATE
#     # NOT PREDICATE
#     # AND [ UNION[ PREDICATE, NOT PREDICATE, OR ] ]
#     # OR [ UNION[ PREDICATE, NOT PREDICATE ] ]
#     # form
#     # [ AND [ OR ( [IS], [NOT] ), ] ]
#     # NOTE THERE MUST BE A CLEANER WAY
#     # single predicate
#     if "predicate" in cnf_precondition.keys():
#         clause_list = [ ([ (clean_string( cnf_precondition[ "predicate" ] ),
#                             *map( clean_string, cnf_precondition[ "args" ] ),), ], [ ]) ]
#     # negation of predicate
#     elif cnf_precondition[ "op" ] == "not":
#         clause_list = [ ([ ], [ (clean_string( cnf_precondition[ "operand" ][ "predicate" ] ),
#                                  *map( clean_string, cnf_precondition[ "operand" ][ "args" ] ),), ]) ]
#     # conjunction
#     elif cnf_precondition[ "op" ] == "and":
#         clause_list = [ ]
#         for conjunct in cnf_precondition[ "operands" ]:
#             clause = ([ ], [ ])
#             if "predicate" in conjunct.keys():
#                 clause[ 0 ].append(
#                     (clean_string( conjunct[ "predicate" ] ), *map( clean_string, conjunct[ "args" ] ),) )
#             # negation of predicate
#             elif conjunct[ "op" ] == "not":
#                 clause[ 1 ].append( (clean_string( conjunct[ "operand" ][ "predicate" ] ),
#                                      *map( clean_string, conjunct[ "operand" ][ "args" ] ),) )
#             # disjunction of predicates annd negations
#             elif conjunct[ "op" ] == "or":
#                 for conjunct_disjunct in conjunct[ "operands" ]:
#                     if "predicate" in conjunct_disjunct.keys():
#                         clause[ 0 ].append( (clean_string( conjunct_disjunct[ "predicate" ] ),
#                                              *map( clean_string, conjunct_disjunct[ "args" ] ),) )
#                     # negation of predicate
#                     elif conjunct_disjunct[ "op" ] == "not":
#                         clause[ 1 ].append(
#                             (clean_string( conjunct_disjunct[ "operand" ][ "predicate" ] ),
#                              *map( clean_string, conjunct_disjunct[ "operand" ][ "args" ] ),) )
#             else:
#                 raise (Exception( "not CNF form" ))
#             clause_list.append( (tuple( clause[ 0 ] ), tuple( clause[ 1 ] )) )
#     # disjunction
#     elif cnf_precondition[ "op" ] == "or":
#         clause = ([ ], [ ])
#         for disjunct in cnf_precondition[ "operands" ]:
#             if "predicate" in disjunct.keys():
#                 clause[ 0 ].append(
#                     (clean_string( disjunct[ "predicate" ] ), *map( clean_string, disjunct[ "args" ] ),) )
#             # negation of predicate
#             elif disjunct[ "op" ] == "not":
#                 clause[ 1 ].append(
#                     (clean_string( disjunct[ "operand" ][ "predicate" ] ),
#                      *map( clean_string, disjunct[ "operand" ][ "args" ] ),) )
#         clause_list = [ clause ]
#     else:
#         raise (Exception( "unsupport op found while making clause list: " + cnf_precondition[ "op" ] ))
#
#     return clause_list


# iteration optimizer
# NEEDS INTEGRATION AND TESTING
# NEED WAY TO CONVERT PREDICATES INTO CNF
predicate_to_boundVar_set = lambda x: { *x[ 1: ] }
clause_to_boundVar_set_list = lambda x: [ predicate_to_boundVar_set( predicate ) for predicate in x ]
boundVar_set_list_flatten = lambda x: set().union( *x )
clause_to_boundVar_set = lambda x: boundVar_set_list_flatten( clause_to_boundVar_set_list( x ) )
count_intersection_size = lambda x, y: len( y.intersection( clause_to_boundVar_set( x ) ) )


# def iteration_optimizer( unboundVars: List[ str ], clauses: List[ Tuple[ List, List ] ] ):
#     # need iteration for all unbound boundVars
#     ordering = [ ]
#     while len( unboundVars ) > 0:
#         # get clauses with each unbound boundVar
#         boundVar_clause_dict = dict()
#         for unboundVar in unboundVars:
#             boundVar_clause_dict[ unboundVar ] = set()
#             for clause in clauses:
#                 # print( clause )
#                 # if boundVar in any predicate of clause associate clause with boundVar
#                 if any( map( lambda x: unboundVar in x, [ *clause[ 0 ], *clause[ 1 ] ] ) ):
#                     boundVar_clause_dict[ unboundVar ].update( clause )
#         # print( boundVar_clause_dict )
#         # sort unbound boundVars by number of associated predicates
#         # sort by size of union set of all unique unbound boundVar for all predicates associated with each boundVar
#         # graph version: minimize increase in frontier size, pick vertex with smallest neighborhood discounting
#         # for vertices that have already been picked or neighbor a pick
#         unboundVars.sort( key=lambda x: count_intersection_size( x, set( unboundVars ) ) )
#
#         # bind boundVar with fewest untouched neighbors
#         bindingVar = unboundVars.pop( 0 )
#         # get predicates that only have binding boundVar as unbound
#         # these predicates are safe to check now as all boundVars will be grounded
#         for unboundVar in unboundVars:
#             boundVar_clause_dict[ bindingVar ] -= boundVar_clause_dict[ unboundVar ]
#         ordering.append( (bindingVar, [ *boundVar_clause_dict[ bindingVar ] ]) )
#         # remove these predicates from list
#         # dont do duplicate checks
#         for boundClause in boundVar_clause_dict[ bindingVar ]:
#             clauses.remove( boundClause )
#     return ordering


def run_experiment( problem_dir, problem_json, output_dir ):
    # print( problem_json )

    # load parser
    parser = HDDL_Parser()
    parser.parse_domain( problem_dir + "domain.json" )

    # used for file names
    # output_py = problem_json.replace( ".snake.json", ".py" )
    # output_txt = problem_json.replace( ".snake.json", ".txt" )
    output_py = problem_json.replace( ".json", ".py" )
    output_txt = problem_json.replace( ".json", ".txt" )

    # read in actions and methods as moduless
    actions_mod = importlib.import_module( output_dir[ :-1 ] + ".domain.actions" )
    actions = actions_mod.actions
    methods_mod = importlib.import_module( output_dir[ :-1 ] + ".domain.methods" )
    methods = methods_mod.methods

    # parse and write problem
    parser.parse_problem( problem_dir + problem_json )
    parser.write_problem( output_dir + "problems_py/" + output_py )

    # read in initial state, task list, and rigid
    state_mod = importlib.import_module( output_dir[ :-1 ] + ".problems_py." + output_py[ :-3 ] )
    init_state = state_mod.state
    task_list = state_mod.task_list
    rigid = state_mod.rigid

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
        print( "Something went wrong for " + problem_json )
    # print(init_state)

    start_time = time.process_time_ns()
    plan = planner.plan( init_state, task_list, verbose=0 )
    end_time = time.process_time_ns()
    total_time = (end_time - start_time) / 1E9
    # write problem and plan to file (name should be the same as the original json file with .py extension)
    hddl_plan_str = planner.hddl_plan_str( parser.hddl_map )
    with open( output_dir + "solutions/" + output_txt, "w" ) as f:
        f.write( hddl_plan_str )
    # print( (problem_json, total_time, plan) )
    return (problem_json, total_time, plan)


if __name__ == '__main__':

    # parsing (CURRENTLY READ, BUT CAN DYNAMICALLY MAKE ACTION/METHODS)
    parser = HDDL_Parser()
    problem_json = "p01.json"
    input_domain_dir = "../../../domains/rovers/"
    output_py = problem_json.replace( "json", "py" )
    output_txt = problem_json.replace( "json", "txt" )
    output_dir = "../rovers/"
    parser.parse_domain( input_domain_dir + "domain.json" )
    # make pythonic representation of state and constants
    parser.parse_problem( input_domain_dir + problem_json )

    # READ IN SHOP TREE
    from IPyHDDLER.rovers.domain.actions import actions
    from IPyHDDLER.rovers.domain.methods import methods

    temp_mod = importlib.import_module( output_dir[ :2 ] + output_dir[ 3:-1 ] + ".problems_py." + output_py[ :-3 ],
                                        package="IPyHDDLER.ipyhddler" )
    init_state = temp_mod.state
    task_list = temp_mod.task_list
    rigid = temp_mod.rigid
    # pass constants using rigid
    local_methods = deepcopy( methods )
    local_actions = deepcopy( actions )
    local_methods.goal_method_dict.update(
        { l: [ partial( m, rigid=rigid ) for m in ms ] for l, ms in local_methods.goal_method_dict.items() } )
    local_methods.task_method_dict.update(
        { l: [ partial( m, rigid=rigid ) for m in ms ] for l, ms in local_methods.task_method_dict.items() } )
    local_methods.multigoal_method_dict.update(
        { l: [ partial( m, rigid=rigid ) for m in ms ] for l, ms in local_methods.multigoal_method_dict.items() } )
    local_actions.action_dict.update( { l: partial( a, rigid=rigid ) for l, a in local_actions.action_dict.items() } )
    # make planner
    planner = IPyHOP( local_methods, local_actions )
    # print(local_methods.task_method_dict)
    # print(local_actions.action_dict)
    planner.read_SHOP( "../sample_shop_output", init_state )
    # get back in hddl format
    # print(planner.hddl_plan_str(parser.hddl_map))
