from ipyhop import State

init_state = State( 'init_state' )
init_state.location = {'g', 'd', 'h', 'b', 'e', 'f', 'i', 'c', 'a'}
init_state.at = { ('a',), }
init_state.road = { ('g', 'f'), ('d', 'e'), ('c', 'd'), ('g', 'i'), ('c', 'e'), ('a', 'c'), ('e', 'g'), ('d', 'f'), ('e', 'f'), ('f', 'h'), ('b', 'c'), ('c', 'g'), }
init_state.paylocation = { ('a',), ('i',), ('b',), ('h',), }
init_state.tollarea = { ('d',), ('e',), ('c',), ('g',), ('f',), }

task_list = [('move', 'a', 'h')]
