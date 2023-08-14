from ipyhop import State

init_state = State( 'init_state' )
init_state.location = {'i', 'f', 'a', 'e', 'd', 'g', 'b', 'h', 'c'}
init_state.at = { ('a',), }
init_state.road = { ('d', 'f'), ('g', 'i'), ('f', 'h'), ('e', 'g'), ('c', 'e'), ('c', 'd'), ('c', 'g'), ('a', 'c'), ('d', 'e'), ('e', 'f'), ('b', 'c'), ('g', 'f'), }
init_state.paylocation = { ('i',), ('a',), ('h',), ('b',), }
init_state.tollarea = { ('f',), ('c',), ('e',), ('d',), ('g',), }

task_list = [('move', 'a', 'h')]
