from ipyhop import State

init_state = State( 'init_state' )
init_state.location = {'d', 'f', 'e', 'i', 'c', 'a', 'b', 'h', 'g'}
init_state.at = { ('a',), }
init_state.road = { ('g', 'i'), ('e', 'g'), ('g', 'f'), ('c', 'g'), ('a', 'c'), ('b', 'c'), ('c', 'e'), ('d', 'e'), ('d', 'f'), ('e', 'f'), ('c', 'd'), ('f', 'h'), }
init_state.paylocation = { ('h',), ('b',), ('i',), ('a',), }
init_state.tollarea = { ('d',), ('c',), ('g',), ('e',), ('f',), }

task_list = [('move', 'a', 'h')]
