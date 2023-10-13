from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.direction = {'n', 'w', 's', 'e'}
rigid.location = {'l_3_3_0', 'l_1_3_3', 'l_2_3_0', 'l_3_0_2', 'l_2_3_1', 'l_4_1_3', 'l_0_1_0', 'l_1_1_0', 'l_4_0_2', 'l_0_0_2', 'l_4_0_1', 'l_1_1_2', 'l_1_2_3', 'l_2_3_2', 'l_0_0_0', 'l_3_1_1', 'l_0_0_3', 'l_3_2_0', 'l_4_3_3', 'l_1_2_1', 'l_1_3_0', 'l_4_3_0', 'l_3_1_3', 'l_0_3_2', 'l_2_0_0', 'l_0_2_2', 'l_2_0_2', 'l_4_2_0', 'l_4_0_3', 'l_2_1_2', 'l_3_0_3', 'l_3_1_0', 'l_4_1_2', 'l_4_3_2', 'l_0_1_2', 'l_3_0_1', 'l_0_2_0', 'l_2_2_3', 'l_1_3_1', 'l_0_3_1', 'l_0_3_3', 'l_0_2_3', 'l_4_1_0', 'l_4_2_3', 'l_4_2_2', 'l_3_2_3', 'l_2_0_3', 'l_2_2_0', 'l_0_2_1', 'l_2_2_1', 'l_2_1_0', 'l_0_1_3', 'l_1_0_0', 'l_1_2_0', 'l_0_1_1', 'l_4_1_1', 'l_4_2_1', 'l_2_2_2', 'l_4_0_0', 'l_1_0_3', 'l_1_0_2', 'l_2_0_1', 'l_2_1_1', 'l_1_2_2', 'l_3_2_1', 'l_3_3_1', 'l_3_1_2', 'l_3_3_3', 'l_1_1_1', 'l_4_3_1', 'l_2_3_3', 'l_1_0_1', 'l_3_0_0', 'l_0_0_1', 'l_0_3_0', 'l_1_3_2', 'l_3_2_2', 'l_2_1_3', 'l_3_3_2', 'l_1_1_3'}
rigid.blocktype = {'earth', 'stone', 'wood'}
rigid.numbers = {'n0', 'n1', 'n3', 'n2'}
rigid.neighbour = { ('l_1_0_1', 'l_1_0_2', 'e'), ('l_2_2_0', 'l_2_1_0', 's'), ('l_1_2_2', 'l_1_3_2', 'n'), ('l_2_2_3', 'l_2_1_3', 's'), ('l_0_1_0', 'l_0_1_1', 'e'), ('l_0_1_1', 'l_0_1_0', 'w'), ('l_1_1_2', 'l_1_2_2', 'n'), ('l_1_0_3', 'l_1_0_2', 'w'), ('l_4_0_2', 'l_4_0_1', 'w'), ('l_4_2_3', 'l_4_1_3', 's'), ('l_3_0_0', 'l_3_0_1', 'e'), ('l_2_0_3', 'l_2_1_3', 'n'), ('l_1_2_0', 'l_1_2_1', 'e'), ('l_0_0_1', 'l_0_0_2', 'e'), ('l_1_0_2', 'l_1_0_1', 'w'), ('l_0_0_2', 'l_0_0_3', 'e'), ('l_3_3_1', 'l_3_3_2', 'e'), ('l_1_3_3', 'l_1_2_3', 's'), ('l_1_1_0', 'l_1_1_1', 'e'), ('l_3_3_1', 'l_3_3_0', 'w'), ('l_1_3_2', 'l_1_3_1', 'w'), ('l_4_3_1', 'l_4_3_2', 'e'), ('l_3_0_2', 'l_3_1_2', 'n'), ('l_2_2_3', 'l_2_2_2', 'w'), ('l_1_1_3', 'l_1_1_2', 'w'), ('l_1_1_0', 'l_1_2_0', 'n'), ('l_3_3_2', 'l_3_2_2', 's'), ('l_0_0_0', 'l_0_1_0', 'n'), ('l_1_2_3', 'l_1_3_3', 'n'), ('l_1_0_2', 'l_1_1_2', 'n'), ('l_4_0_2', 'l_4_0_3', 'e'), ('l_0_1_1', 'l_0_0_1', 's'), ('l_3_3_0', 'l_3_2_0', 's'), ('l_2_1_3', 'l_2_1_2', 'w'), ('l_0_0_1', 'l_0_0_0', 'w'), ('l_2_3_0', 'l_2_2_0', 's'), ('l_4_1_3', 'l_4_2_3', 'n'), ('l_1_3_0', 'l_1_2_0', 's'), ('l_3_3_3', 'l_3_2_3', 's'), ('l_3_3_2', 'l_3_3_3', 'e'), ('l_4_2_3', 'l_4_2_2', 'w'), ('l_4_0_1', 'l_4_0_0', 'w'), ('l_0_3_3', 'l_0_2_3', 's'), ('l_2_2_2', 'l_2_1_2', 's'), ('l_2_2_1', 'l_2_2_0', 'w'), ('l_1_1_1', 'l_1_2_1', 'n'), ('l_3_3_3', 'l_3_3_2', 'w'), ('l_0_1_2', 'l_0_0_2', 's'), ('l_4_2_1', 'l_4_2_0', 'w'), ('l_2_1_0', 'l_2_2_0', 'n'), ('l_1_2_2', 'l_1_2_3', 'e'), ('l_1_2_1', 'l_1_2_0', 'w'), ('l_4_2_1', 'l_4_3_1', 'n'), ('l_3_0_3', 'l_3_0_2', 'w'), ('l_2_2_1', 'l_2_1_1', 's'), ('l_3_1_2', 'l_3_0_2', 's'), ('l_2_3_1', 'l_2_3_0', 'w'), ('l_3_1_1', 'l_3_2_1', 'n'), ('l_4_2_1', 'l_4_1_1', 's'), ('l_4_3_1', 'l_4_2_1', 's'), ('l_0_3_1', 'l_0_3_2', 'e'), ('l_4_1_1', 'l_4_0_1', 's'), ('l_3_3_2', 'l_3_3_1', 'w'), ('l_3_1_0', 'l_3_2_0', 'n'), ('l_1_3_2', 'l_1_2_2', 's'), ('l_2_1_1', 'l_2_1_2', 'e'), ('l_0_0_3', 'l_0_0_2', 'w'), ('l_2_3_1', 'l_2_2_1', 's'), ('l_1_2_0', 'l_1_3_0', 'n'), ('l_4_3_2', 'l_4_3_3', 'e'), ('l_3_1_0', 'l_3_1_1', 'e'), ('l_3_2_3', 'l_3_2_2', 'w'), ('l_3_0_1', 'l_3_1_1', 'n'), ('l_4_0_3', 'l_4_1_3', 'n'), ('l_3_2_2', 'l_3_1_2', 's'), ('l_3_1_3', 'l_3_1_2', 'w'), ('l_2_1_1', 'l_2_0_1', 's'), ('l_3_2_2', 'l_3_2_1', 'w'), ('l_2_1_2', 'l_2_2_2', 'n'), ('l_2_0_0', 'l_2_1_0', 'n'), ('l_3_1_2', 'l_3_2_2', 'n'), ('l_2_2_1', 'l_2_3_1', 'n'), ('l_4_2_1', 'l_4_2_2', 'e'), ('l_3_2_3', 'l_3_3_3', 'n'), ('l_0_3_1', 'l_0_2_1', 's'), ('l_1_1_0', 'l_1_0_0', 's'), ('l_0_2_0', 'l_0_2_1', 'e'), ('l_1_3_2', 'l_1_3_3', 'e'), ('l_4_0_2', 'l_4_1_2', 'n'), ('l_1_2_0', 'l_1_1_0', 's'), ('l_0_1_2', 'l_0_1_1', 'w'), ('l_0_2_1', 'l_0_2_0', 'w'), ('l_3_1_3', 'l_3_0_3', 's'), ('l_4_1_3', 'l_4_0_3', 's'), ('l_0_2_3', 'l_0_1_3', 's'), ('l_3_0_2', 'l_3_0_1', 'w'), ('l_1_1_1', 'l_1_0_1', 's'), ('l_3_2_1', 'l_3_1_1', 's'), ('l_3_1_3', 'l_3_2_3', 'n'), ('l_4_1_1', 'l_4_2_1', 'n'), ('l_0_0_0', 'l_0_0_1', 'e'), ('l_1_0_0', 'l_1_1_0', 'n'), ('l_4_0_0', 'l_4_0_1', 'e'), ('l_3_0_3', 'l_3_1_3', 'n'), ('l_2_0_2', 'l_2_0_1', 'w'), ('l_2_3_2', 'l_2_2_2', 's'), ('l_4_0_1', 'l_4_0_2', 'e'), ('l_2_3_3', 'l_2_3_2', 'w'), ('l_2_0_1', 'l_2_0_2', 'e'), ('l_2_0_1', 'l_2_0_0', 'w'), ('l_1_1_3', 'l_1_0_3', 's'), ('l_2_1_0', 'l_2_1_1', 'e'), ('l_0_2_1', 'l_0_2_2', 'e'), ('l_2_1_2', 'l_2_1_3', 'e'), ('l_1_2_3', 'l_1_2_2', 'w'), ('l_1_1_2', 'l_1_1_1', 'w'), ('l_0_1_0', 'l_0_0_0', 's'), ('l_2_1_1', 'l_2_1_0', 'w'), ('l_0_2_1', 'l_0_1_1', 's'), ('l_2_1_2', 'l_2_0_2', 's'), ('l_1_0_1', 'l_1_0_0', 'w'), ('l_2_2_0', 'l_2_2_1', 'e'), ('l_4_3_3', 'l_4_2_3', 's'), ('l_3_1_1', 'l_3_0_1', 's'), ('l_1_2_1', 'l_1_3_1', 'n'), ('l_2_2_1', 'l_2_2_2', 'e'), ('l_4_3_0', 'l_4_3_1', 'e'), ('l_0_1_3', 'l_0_1_2', 'w'), ('l_4_3_1', 'l_4_3_0', 'w'), ('l_4_1_2', 'l_4_1_3', 'e'), ('l_1_1_2', 'l_1_0_2', 's'), ('l_0_3_2', 'l_0_2_2', 's'), ('l_0_0_2', 'l_0_0_1', 'w'), ('l_1_3_1', 'l_1_2_1', 's'), ('l_0_3_0', 'l_0_3_1', 'e'), ('l_3_1_1', 'l_3_1_0', 'w'), ('l_3_2_2', 'l_3_3_2', 'n'), ('l_0_2_3', 'l_0_2_2', 'w'), ('l_3_0_0', 'l_3_1_0', 'n'), ('l_2_2_3', 'l_2_3_3', 'n'), ('l_4_3_0', 'l_4_2_0', 's'), ('l_3_2_1', 'l_3_2_2', 'e'), ('l_1_0_0', 'l_1_0_1', 'e'), ('l_2_1_2', 'l_2_1_1', 'w'), ('l_0_2_2', 'l_0_3_2', 'n'), ('l_4_2_2', 'l_4_2_3', 'e'), ('l_0_0_3', 'l_0_1_3', 'n'), ('l_3_2_0', 'l_3_2_1', 'e'), ('l_4_1_0', 'l_4_0_0', 's'), ('l_1_1_2', 'l_1_1_3', 'e'), ('l_0_2_1', 'l_0_3_1', 'n'), ('l_3_0_2', 'l_3_0_3', 'e'), ('l_4_0_0', 'l_4_1_0', 'n'), ('l_0_1_2', 'l_0_2_2', 'n'), ('l_4_1_3', 'l_4_1_2', 'w'), ('l_3_1_1', 'l_3_1_2', 'e'), ('l_2_0_2', 'l_2_0_3', 'e'), ('l_0_3_2', 'l_0_3_3', 'e'), ('l_4_2_0', 'l_4_1_0', 's'), ('l_0_3_0', 'l_0_2_0', 's'), ('l_0_3_2', 'l_0_3_1', 'w'), ('l_0_2_2', 'l_0_2_1', 'w'), ('l_1_2_2', 'l_1_2_1', 'w'), ('l_0_0_1', 'l_0_1_1', 'n'), ('l_0_2_3', 'l_0_3_3', 'n'), ('l_3_2_3', 'l_3_1_3', 's'), ('l_1_0_2', 'l_1_0_3', 'e'), ('l_0_2_0', 'l_0_1_0', 's'), ('l_0_2_2', 'l_0_1_2', 's'), ('l_4_1_2', 'l_4_1_1', 'w'), ('l_2_0_3', 'l_2_0_2', 'w'), ('l_4_1_1', 'l_4_1_0', 'w'), ('l_0_1_3', 'l_0_2_3', 'n'), ('l_0_1_1', 'l_0_1_2', 'e'), ('l_3_2_2', 'l_3_2_3', 'e'), ('l_1_2_2', 'l_1_1_2', 's'), ('l_0_1_0', 'l_0_2_0', 'n'), ('l_4_3_2', 'l_4_2_2', 's'), ('l_0_1_1', 'l_0_2_1', 'n'), ('l_2_2_2', 'l_2_2_3', 'e'), ('l_4_2_2', 'l_4_3_2', 'n'), ('l_2_3_2', 'l_2_3_1', 'w'), ('l_4_1_2', 'l_4_0_2', 's'), ('l_3_3_0', 'l_3_3_1', 'e'), ('l_3_2_0', 'l_3_3_0', 'n'), ('l_3_2_1', 'l_3_3_1', 'n'), ('l_2_0_0', 'l_2_0_1', 'e'), ('l_2_3_0', 'l_2_3_1', 'e'), ('l_4_0_3', 'l_4_0_2', 'w'), ('l_1_1_1', 'l_1_1_0', 'w'), ('l_2_1_1', 'l_2_2_1', 'n'), ('l_1_1_1', 'l_1_1_2', 'e'), ('l_1_1_3', 'l_1_2_3', 'n'), ('l_4_1_0', 'l_4_2_0', 'n'), ('l_1_3_3', 'l_1_3_2', 'w'), ('l_0_2_2', 'l_0_2_3', 'e'), ('l_3_2_1', 'l_3_2_0', 'w'), ('l_2_3_1', 'l_2_3_2', 'e'), ('l_1_2_3', 'l_1_1_3', 's'), ('l_0_3_1', 'l_0_3_0', 'w'), ('l_1_3_1', 'l_1_3_2', 'e'), ('l_3_0_1', 'l_3_0_2', 'e'), ('l_1_3_1', 'l_1_3_0', 'w'), ('l_4_1_0', 'l_4_1_1', 'e'), ('l_1_0_3', 'l_1_1_3', 'n'), ('l_4_3_3', 'l_4_3_2', 'w'), ('l_4_2_3', 'l_4_3_3', 'n'), ('l_2_1_0', 'l_2_0_0', 's'), ('l_4_2_0', 'l_4_2_1', 'e'), ('l_2_0_1', 'l_2_1_1', 'n'), ('l_3_0_1', 'l_3_0_0', 'w'), ('l_4_1_1', 'l_4_1_2', 'e'), ('l_2_1_3', 'l_2_0_3', 's'), ('l_2_3_3', 'l_2_2_3', 's'), ('l_2_3_2', 'l_2_3_3', 'e'), ('l_0_3_3', 'l_0_3_2', 'w'), ('l_2_2_2', 'l_2_2_1', 'w'), ('l_4_2_0', 'l_4_3_0', 'n'), ('l_4_2_2', 'l_4_1_2', 's'), ('l_4_3_2', 'l_4_3_1', 'w'), ('l_0_2_0', 'l_0_3_0', 'n'), ('l_3_3_1', 'l_3_2_1', 's'), ('l_0_1_3', 'l_0_0_3', 's'), ('l_4_1_2', 'l_4_2_2', 'n'), ('l_2_2_2', 'l_2_3_2', 'n'), ('l_3_1_0', 'l_3_0_0', 's'), ('l_4_0_1', 'l_4_1_1', 'n'), ('l_4_2_2', 'l_4_2_1', 'w'), ('l_0_0_2', 'l_0_1_2', 'n'), ('l_3_1_2', 'l_3_1_1', 'w'), ('l_2_2_0', 'l_2_3_0', 'n'), ('l_1_0_1', 'l_1_1_1', 'n'), ('l_1_3_0', 'l_1_3_1', 'e'), ('l_1_2_1', 'l_1_2_2', 'e'), ('l_1_2_1', 'l_1_1_1', 's'), ('l_2_0_2', 'l_2_1_2', 'n'), ('l_3_1_2', 'l_3_1_3', 'e'), ('l_3_2_0', 'l_3_1_0', 's'), ('l_2_1_3', 'l_2_2_3', 'n'), ('l_0_1_2', 'l_0_1_3', 'e'), }
rigid.on_top = { ('l_2_2_0', 'l_3_2_0'), ('l_3_2_1', 'l_4_2_1'), ('l_3_0_3', 'l_4_0_3'), ('l_3_2_2', 'l_4_2_2'), ('l_2_3_1', 'l_3_3_1'), ('l_1_2_1', 'l_2_2_1'), ('l_3_1_1', 'l_4_1_1'), ('l_1_1_2', 'l_2_1_2'), ('l_2_3_2', 'l_3_3_2'), ('l_1_0_2', 'l_2_0_2'), ('l_1_0_1', 'l_2_0_1'), ('l_2_0_1', 'l_3_0_1'), ('l_3_0_0', 'l_4_0_0'), ('l_1_2_2', 'l_2_2_2'), ('l_2_3_3', 'l_3_3_3'), ('l_0_3_2', 'l_1_3_2'), ('l_0_2_1', 'l_1_2_1'), ('l_1_3_1', 'l_2_3_1'), ('l_3_1_0', 'l_4_1_0'), ('l_0_0_2', 'l_1_0_2'), ('l_0_1_2', 'l_1_1_2'), ('l_0_1_1', 'l_1_1_1'), ('l_2_3_0', 'l_3_3_0'), ('l_1_1_0', 'l_2_1_0'), ('l_0_3_0', 'l_1_3_0'), ('l_3_0_2', 'l_4_0_2'), ('l_0_1_0', 'l_1_1_0'), ('l_1_1_3', 'l_2_1_3'), ('l_0_0_1', 'l_1_0_1'), ('l_1_2_3', 'l_2_2_3'), ('l_3_1_3', 'l_4_1_3'), ('l_0_2_2', 'l_1_2_2'), ('l_0_0_0', 'l_1_0_0'), ('l_3_0_1', 'l_4_0_1'), ('l_0_3_3', 'l_1_3_3'), ('l_2_0_0', 'l_3_0_0'), ('l_3_3_2', 'l_4_3_2'), ('l_3_2_3', 'l_4_2_3'), ('l_3_1_2', 'l_4_1_2'), ('l_3_3_1', 'l_4_3_1'), ('l_0_1_3', 'l_1_1_3'), ('l_0_0_3', 'l_1_0_3'), ('l_3_2_0', 'l_4_2_0'), ('l_2_2_2', 'l_3_2_2'), ('l_0_2_3', 'l_1_2_3'), ('l_0_2_0', 'l_1_2_0'), ('l_0_3_1', 'l_1_3_1'), ('l_1_2_0', 'l_2_2_0'), ('l_2_2_1', 'l_3_2_1'), ('l_2_0_3', 'l_3_0_3'), ('l_2_2_3', 'l_3_2_3'), ('l_3_3_0', 'l_4_3_0'), ('l_1_3_2', 'l_2_3_2'), ('l_1_0_0', 'l_2_0_0'), ('l_1_3_0', 'l_2_3_0'), ('l_1_1_1', 'l_2_1_1'), ('l_1_3_3', 'l_2_3_3'), ('l_3_3_3', 'l_4_3_3'), ('l_2_1_0', 'l_3_1_0'), ('l_2_0_2', 'l_3_0_2'), ('l_1_0_3', 'l_2_0_3'), ('l_2_1_2', 'l_3_1_2'), ('l_2_1_1', 'l_3_1_1'), ('l_2_1_3', 'l_3_1_3'), }
state.blockat = { ('l_0_1_2', 'earth'), ('l_0_0_2', 'earth'), ('l_0_2_3', 'earth'), ('l_0_3_1', 'earth'), ('l_0_2_0', 'earth'), ('l_0_2_2', 'earth'), ('l_0_3_0', 'earth'), ('l_0_3_3', 'earth'), ('l_0_3_2', 'earth'), ('l_0_1_1', 'earth'), ('l_0_0_0', 'earth'), ('l_0_0_3', 'earth'), ('l_0_2_1', 'earth'), ('l_0_1_3', 'earth'), ('l_0_1_0', 'earth'), ('l_0_0_1', 'earth'), }
state.empty = { ('l_3_2_1',), ('l_2_1_0',), ('l_4_0_2',), ('l_3_1_0',), ('l_4_2_0',), ('l_1_0_0',), ('l_1_3_1',), ('l_2_0_0',), ('l_1_1_1',), ('l_4_0_1',), ('l_3_0_0',), ('l_3_0_1',), ('l_2_3_1',), ('l_1_1_2',), ('l_4_3_2',), ('l_2_2_3',), ('l_1_0_2',), ('l_4_3_3',), ('l_4_1_2',), ('l_2_3_3',), ('l_1_2_0',), ('l_3_2_0',), ('l_4_2_2',), ('l_1_1_0',), ('l_1_0_1',), ('l_1_0_3',), ('l_2_2_0',), ('l_3_3_1',), ('l_1_2_3',), ('l_3_0_2',), ('l_2_0_3',), ('l_4_1_0',), ('l_2_0_2',), ('l_4_1_1',), ('l_3_1_1',), ('l_3_1_2',), ('l_1_3_2',), ('l_3_2_3',), ('l_2_0_1',), ('l_4_3_0',), ('l_2_2_1',), ('l_3_3_0',), ('l_2_3_2',), ('l_1_3_0',), ('l_1_2_1',), ('l_4_1_3',), ('l_4_0_3',), ('l_4_3_1',), ('l_2_1_2',), ('l_2_2_2',), ('l_1_1_3',), ('l_4_0_0',), ('l_4_2_1',), ('l_3_2_2',), ('l_1_3_3',), ('l_3_3_3',), ('l_1_2_2',), ('l_2_3_0',), ('l_2_1_3',), ('l_4_2_3',), ('l_2_1_1',), ('l_3_0_3',), ('l_3_3_2',), ('l_3_1_3',), }
rigid.isone = { ('n1',), }
rigid.prev = { ('n1', 'n0'), ('n3', 'n2'), ('n2', 'n1'), }

task_list = [('buildhouse', 'l_1_0_0', 'l_1_0_2', 'l_1_2_2', 'l_1_2_0', 'l_1_1_0', 'l_4_0_0', 'n3', 'n3', 'n3', 'stone')]
