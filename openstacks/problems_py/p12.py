from ipyhop import State

from ordered_set import OrderedSet

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = OrderedSet(['n0', 'n1', 'n10', 'n11', 'n12', 'n13', 'n14', 'n15', 'n16', 'n17', 'n18', 'n19', 'n2', 'n20', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'o1', 'o10', 'o11', 'o12', 'o13', 'o14', 'o15', 'o16', 'o17', 'o18', 'o19', 'o2', 'o20', 'o3', 'o4', 'o5', 'o6', 'o7', 'o8', 'o9', 'p1', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p2', 'p20', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9'])
rigid.order = OrderedSet(['o1', 'o10', 'o11', 'o12', 'o13', 'o14', 'o15', 'o16', 'o17', 'o18', 'o19', 'o2', 'o20', 'o3', 'o4', 'o5', 'o6', 'o7', 'o8', 'o9'])
rigid.product = OrderedSet(['p1', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p2', 'p20', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9'])
rigid.count = OrderedSet(['n0', 'n1', 'n10', 'n11', 'n12', 'n13', 'n14', 'n15', 'n16', 'n17', 'n18', 'n19', 'n2', 'n20', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9'])
rigid.goal__shipped = OrderedSet( [('o1',), ('o2',), ('o3',), ('o4',), ('o5',), ('o6',), ('o7',), ('o8',), ('o9',), ('o10',), ('o11',), ('o12',), ('o13',), ('o14',), ('o15',), ('o16',), ('o17',), ('o18',), ('o19',), ('o20',), ] )
rigid.next__count = OrderedSet( [('n0', 'n1'), ('n1', 'n2'), ('n2', 'n3'), ('n3', 'n4'), ('n4', 'n5'), ('n5', 'n6'), ('n6', 'n7'), ('n7', 'n8'), ('n8', 'n9'), ('n9', 'n10'), ('n10', 'n11'), ('n11', 'n12'), ('n12', 'n13'), ('n13', 'n14'), ('n14', 'n15'), ('n15', 'n16'), ('n16', 'n17'), ('n17', 'n18'), ('n18', 'n19'), ('n19', 'n20'), ] )
state.stacks__avail = OrderedSet( [('n0',), ] )
state.waiting = OrderedSet( [('o1',), ('o2',), ('o3',), ('o4',), ('o5',), ('o6',), ('o7',), ('o8',), ('o9',), ('o10',), ('o11',), ('o12',), ('o13',), ('o14',), ('o15',), ('o16',), ('o17',), ('o18',), ('o19',), ('o20',), ] )
rigid.includes = OrderedSet( [('o1', 'p4'), ('o2', 'p1'), ('o3', 'p4'), ('o4', 'p2'), ('o4', 'p3'), ('o4', 'p11'), ('o5', 'p17'), ('o5', 'p20'), ('o6', 'p9'), ('o7', 'p6'), ('o7', 'p11'), ('o8', 'p14'), ('o9', 'p15'), ('o10', 'p12'), ('o11', 'p19'), ('o12', 'p1'), ('o12', 'p3'), ('o13', 'p11'), ('o13', 'p12'), ('o13', 'p18'), ('o14', 'p7'), ('o14', 'p9'), ('o15', 'p10'), ('o15', 'p12'), ('o15', 'p13'), ('o15', 'p14'), ('o16', 'p5'), ('o17', 'p16'), ('o18', 'p8'), ('o18', 'p16'), ('o19', 'p4'), ('o19', 'p10'), ('o19', 'p14'), ('o20', 'p19'), ] )
state.started = OrderedSet( [] )
state.shipped = OrderedSet( [] )
state.made = OrderedSet( [] )

task_list = [('plan',)]
