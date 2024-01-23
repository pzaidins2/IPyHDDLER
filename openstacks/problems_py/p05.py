from ipyhop import State

from ordered_set import OrderedSet

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = OrderedSet(['n0', 'n1', 'n10', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'o1', 'o10', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7', 'o8', 'o9', 'p1', 'p10', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9'])
rigid.order = OrderedSet(['o1', 'o10', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7', 'o8', 'o9'])
rigid.product = OrderedSet(['p1', 'p10', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9'])
rigid.count = OrderedSet(['n0', 'n1', 'n10', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9'])
rigid.goal__shipped = OrderedSet( [('o1',), ('o2',), ('o3',), ('o4',), ('o5',), ('o6',), ('o7',), ('o8',), ('o9',), ('o10',), ] )
rigid.next__count = OrderedSet( [('n0', 'n1'), ('n1', 'n2'), ('n2', 'n3'), ('n3', 'n4'), ('n4', 'n5'), ('n5', 'n6'), ('n6', 'n7'), ('n7', 'n8'), ('n8', 'n9'), ('n9', 'n10'), ] )
state.stacks__avail = OrderedSet( [('n0',), ] )
state.waiting = OrderedSet( [('o1',), ('o2',), ('o3',), ('o4',), ('o5',), ('o6',), ('o7',), ('o8',), ('o9',), ('o10',), ] )
rigid.includes = OrderedSet( [('o1', 'p3'), ('o1', 'p4'), ('o2', 'p1'), ('o2', 'p6'), ('o3', 'p8'), ('o4', 'p3'), ('o5', 'p4'), ('o6', 'p5'), ('o6', 'p10'), ('o7', 'p9'), ('o8', 'p2'), ('o9', 'p7'), ('o9', 'p10'), ('o10', 'p2'), ] )
state.started = OrderedSet( [] )
state.shipped = OrderedSet( [] )
state.made = OrderedSet( [] )

task_list = [('plan',)]
