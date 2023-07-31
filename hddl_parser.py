# this file allows for hddl file to be read in and converted to python friendly representation
import re

# domain name
re_domain = re.compile( "\(\W*domain\W+(.+)\W*\)" )

# types
# each type separated by white space with optional parent type
re_type_isolate = re.compile("\(:types([\w\W]+?)\)")
# group 1 is type label and group 2 is parent type or None
re_type = re.compile("(\w+) (?:\- (\w+))?")

# tasks
# task has a name and series of typed parameters
# group 1 is task label and group 2 is parameters string
re_task_isolate = re.compile("\(:task\W+(\w+)\W+\:parameters\W\((.*)\)\W*\)")
# group 1 is parameter name and group 2 is parameter type
re_task = re.compile("(\w+) (?:\- (\w+))?")

# predicates
# determine "shape" of state
# predicates can be seen as a label followed by ordered list of typed parameters
# potentially empty
# not necessarily smartest shape we can have a dictionary with label as key and
# remaining parameters as set of tuples of remaining parameters
re_predicate_isolate = re.compile("\(:predicates([\w\W]+?\))\)")
# grab each individual tuple
re_predicate_seperate = re.compile("\((.+?)\)")
# get label and parameters if any
re_predicate_label = re.compile("^\w+")
# group 1 is parameter name and group 2 is type
re_predicate_parameters = re.compile("\?(\w+)\W+\-\W+(\w+)")
#
# methods
# have parameters, task, preconditions (optional), subtasks
re_method_isolate = \
    re.compile("\(:method\s+(.+)\s+\:parameters\s+\((.*)\)\s+\:task\s+\((.*)\)\s*(?:\:precondition\s+\([\w\W]+?)?\:ordered\-(?:sub)?tasks\s+\((.+)\)\s*\)")
# actions
# have

class HDDL_Parser:
    def __init__(self):
        self.file_name = None
        self.file = None

    def parse_domain( self, file_path: str ) -> None:
        # read file as string

        # domain name

        # requirements CURRENTLY NO INTENTION TO USE
        # types

        # constants

        # predicates

        # tasks

        # methods

        # actions
        pass

    def parse_problem( self, file_path: str ) -> None:
        pass

    def write_file( self, file_path: str ) -> None:
        pass
