from ipyhop import State

from ordered_set import OrderedSet

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = OrderedSet(['n0', 'n1', 'n10', 'n11', 'n12', 'n13', 'n14', 'n15', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'o1', 'o10', 'o11', 'o12', 'o13', 'o14', 'o15', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7', 'o8', 'o9', 'p1', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9'])
rigid.order = OrderedSet(['o1', 'o10', 'o11', 'o12', 'o13', 'o14', 'o15', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7', 'o8', 'o9'])
rigid.product = OrderedSet(['p1', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9'])
rigid.count = OrderedSet(['n0', 'n1', 'n10', 'n11', 'n12', 'n13', 'n14', 'n15', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9'])
rigid.goal__shipped = OrderedSet( [('o1',), ('o2',), ('o3',), ('o4',), ('o5',), ('o6',), ('o7',), ('o8',), ('o9',), ('o10',), ('o11',), ('o12',), ('o13',), ('o14',), ('o15',), ] )
rigid.next__count = OrderedSet( [('n0', 'n1'), ('n1', 'n2'), ('n2', 'n3'), ('n3', 'n4'), ('n4', 'n5'), ('n5', 'n6'), ('n6', 'n7'), ('n7', 'n8'), ('n8', 'n9'), ('n9', 'n10'), ('n10', 'n11'), ('n11', 'n12'), ('n12', 'n13'), ('n13', 'n14'), ('n14', 'n15'), ] )
state.stacks__avail = OrderedSet( [('n0',), ] )
state.waiting = OrderedSet( [('o1',), ('o2',), ('o3',), ('o4',), ('o5',), ('o6',), ('o7',), ('o8',), ('o9',), ('o10',), ('o11',), ('o12',), ('o13',), ('o14',), ('o15',), ] )
rigid.includes = OrderedSet( [('o1', 'p8'), ('o2', 'p4'), ('o2', 'p13'), ('o3', 'p12'), ('o4', 'p1'), ('o5', 'p8'), ('o6', 'p3'), ('o6', 'p10'), ('o7', 'p9'), ('o8', 'p11'), ('o9', 'p7'), ('o9', 'p15'), ('o10', 'p14'), ('o11', 'p9'), ('o12', 'p1'), ('o12', 'p2'), ('o13', 'p4'), ('o13', 'p6'), ('o13', 'p9'), ('o14', 'p5'), ('o14', 'p9'), ('o15', 'p12'), ] )
state.started = OrderedSet( [] )
state.shipped = OrderedSet( [] )
state.made = OrderedSet( [] )

task_list = [('plan',)]
