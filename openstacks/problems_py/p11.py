from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'o4', 'n15', 'p16', 'o14', 'o10', 'o16', 'n13', 'p10', 'o8', 'o18', 'p14', 'p18', 'p3', 'n7', 'n11', 'p5', 'o13', 'n8', 'n17', 'o9', 'p17', 'n10', 'n1', 'n20', 'n12', 'n2', 'n18', 'n19', 'p6', 'n4', 'o17', 'p1', 'p13', 'p19', 'p12', 'o3', 'p2', 'p4', 'p8', 'o12', 'o1', 'o7', 'p7', 'o5', 'p11', 'o20', 'o19', 'p15', 'n5', 'p9', 'n6', 'o2', 'o6', 'n16', 'o11', 'n9', 'o15', 'p20', 'n3', 'n0', 'n14'}
rigid.product = {'p19', 'p12', 'p2', 'p4', 'p16', 'p8', 'p10', 'p20', 'p14', 'p18', 'p3', 'p7', 'p11', 'p5', 'p15', 'p17', 'p9', 'p1', 'p13', 'p6'}
rigid.count = {'n15', 'n13', 'n7', 'n11', 'n8', 'n17', 'n5', 'n10', 'n1', 'n20', 'n12', 'n2', 'n18', 'n19', 'n6', 'n16', 'n9', 'n4', 'n3', 'n0', 'n14'}
rigid.order = {'o4', 'o3', 'o14', 'o10', 'o16', 'o12', 'o1', 'o8', 'o7', 'o18', 'o5', 'o20', 'o19', 'o13', 'o9', 'o2', 'o6', 'o17', 'o15', 'o11'}
rigid.goal__shipped = set( [('o15',), ('o17',), ('o2',), ('o18',), ('o5',), ('o4',), ('o16',), ('o14',), ('o9',), ('o20',), ('o11',), ('o19',), ('o1',), ('o3',), ('o8',), ('o13',), ('o10',), ('o7',), ('o12',), ('o6',), ] )
rigid.next__count = set( [('n14', 'n15'), ('n17', 'n18'), ('n19', 'n20'), ('n9', 'n10'), ('n15', 'n16'), ('n16', 'n17'), ('n8', 'n9'), ('n0', 'n1'), ('n4', 'n5'), ('n6', 'n7'), ('n1', 'n2'), ('n12', 'n13'), ('n10', 'n11'), ('n2', 'n3'), ('n11', 'n12'), ('n3', 'n4'), ('n13', 'n14'), ('n5', 'n6'), ('n18', 'n19'), ('n7', 'n8'), ] )
state.stacks__avail = set( [('n0',), ] )
state.waiting = set( [('o15',), ('o17',), ('o2',), ('o18',), ('o5',), ('o4',), ('o16',), ('o14',), ('o9',), ('o20',), ('o11',), ('o19',), ('o1',), ('o3',), ('o8',), ('o13',), ('o10',), ('o7',), ('o12',), ('o6',), ] )
rigid.includes = set( [('o7', 'p11'), ('o17', 'p2'), ('o9', 'p12'), ('o13', 'p9'), ('o20', 'p9'), ('o18', 'p17'), ('o8', 'p17'), ('o7', 'p17'), ('o18', 'p20'), ('o9', 'p17'), ('o14', 'p14'), ('o19', 'p19'), ('o11', 'p18'), ('o15', 'p14'), ('o2', 'p13'), ('o12', 'p2'), ('o16', 'p7'), ('o13', 'p15'), ('o5', 'p8'), ('o12', 'p3'), ('o10', 'p5'), ('o2', 'p11'), ('o16', 'p11'), ('o4', 'p9'), ('o6', 'p4'), ('o13', 'p14'), ('o12', 'p1'), ('o15', 'p19'), ('o19', 'p17'), ('o18', 'p11'), ('o8', 'p10'), ('o15', 'p18'), ('o6', 'p5'), ('o7', 'p6'), ('o3', 'p8'), ('o5', 'p16'), ('o16', 'p20'), ('o1', 'p9'), ] )
state.shipped = set( [] )
state.started = set( [] )
state.made = set( [] )

task_list = [('plan',)]
