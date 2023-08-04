from ipyhop import State

init_state = State( 'init_state' )
init_state.location = {'d', 'e', 'f', 'h', 'b', 'c', 'i', 'a', 'g'}
init_state.at = { ('a',), }
init_state.road = { ('c', 'e'), ('c', 'd'), ('a', 'c'), ('d', 'f'), ('g', 'i'), ('b', 'c'), ('c', 'g'), ('d', 'e'), ('e', 'g'), ('g', 'f'), ('f', 'h'), ('e', 'f'), }
init_state.paylocation = { ('i',), ('a',), ('b',), ('h',), }
init_state.tollarea = { ('e',), ('d',), ('g',), ('c',), ('f',), }

task_list = [('move', 'a', 'h')]
