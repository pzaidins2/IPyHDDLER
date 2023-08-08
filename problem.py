from ipyhop import State

init_state = State( 'init_state' )
init_state.location = {'g', 'f', 'a', 'i', 'c', 'b', 'd', 'e', 'h'}
init_state.at = { ('a',), }
init_state.road = { ('g', 'i'), ('b', 'c'), ('a', 'c'), ('e', 'f'), ('c', 'd'), ('d', 'e'), ('e', 'g'), ('f', 'h'), ('c', 'g'), ('d', 'f'), ('c', 'e'), ('g', 'f'), }
init_state.paylocation = { ('h',), ('i',), ('a',), ('b',), }
init_state.tollarea = { ('f',), ('d',), ('g',), ('e',), ('c',), }

task_list = [('move', 'a', 'h')]
