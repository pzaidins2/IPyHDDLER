from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'o4', 'o3', 'p2', 'p4', 'p8', 'o10', 'o1', 'p10', 'o8', 'o7', 'p3', 'p7', 'n7', 'o5', 'p5', 'n8', 'n5', 'o9', 'n10', 'n1', 'p9', 'n2', 'n6', 'p6', 'o2', 'o6', 'n9', 'n4', 'p1', 'n3', 'n0'}
rigid.product = {'p5', 'p2', 'p4', 'p8', 'p9', 'p10', 'p3', 'p7', 'p1', 'p6'}
rigid.count = {'n8', 'n5', 'n10', 'n1', 'n2', 'n6', 'n9', 'n4', 'n7', 'n3', 'n0'}
rigid.order = {'o4', 'o3', 'o9', 'o10', 'o1', 'o2', 'o6', 'o8', 'o7', 'o5'}
rigid.goal__shipped = set( [('o1',), ('o10',), ('o7',), ('o2',), ('o3',), ('o6',), ('o9',), ('o5',), ('o4',), ('o8',), ] )
rigid.next__count = set( [('n4', 'n5'), ('n2', 'n3'), ('n8', 'n9'), ('n9', 'n10'), ('n6', 'n7'), ('n3', 'n4'), ('n1', 'n2'), ('n5', 'n6'), ('n0', 'n1'), ('n7', 'n8'), ] )
state.stacks__avail = set( [('n0',), ] )
state.waiting = set( [('o1',), ('o10',), ('o7',), ('o2',), ('o3',), ('o6',), ('o9',), ('o5',), ('o4',), ('o8',), ] )
rigid.includes = set( [('o2', 'p6'), ('o2', 'p1'), ('o1', 'p4'), ('o4', 'p3'), ('o8', 'p2'), ('o9', 'p10'), ('o5', 'p4'), ('o7', 'p9'), ('o9', 'p7'), ('o6', 'p5'), ('o6', 'p10'), ('o3', 'p8'), ('o10', 'p2'), ('o1', 'p3'), ] )
state.shipped = set( [] )
state.started = set( [] )
state.made = set( [] )

task_list = [('plan',)]
