from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'n5', 'o1', 'o4', 'o3', 'o6', 'p10', 'n2', 'n7', 'n0', 'o5', 'n3', 'o2', 'o8', 'n9', 'p9', 'o9', 'p2', 'o10', 'n4', 'p8', 'p1', 'n1', 'n8', 'n10', 'p5', 'p6', 'p7', 'n6', 'o7', 'p3', 'p4'}
rigid.product = {'p8', 'p1', 'p10', 'p5', 'p6', 'p7', 'p9', 'p2', 'p3', 'p4'}
rigid.order = {'o1', 'o4', 'o3', 'o6', 'o5', 'o2', 'o8', 'o9', 'o7', 'o10'}
rigid.count = {'n5', 'n4', 'n1', 'n2', 'n8', 'n7', 'n10', 'n0', 'n3', 'n9', 'n6'}
rigid.goal__shipped = set( [('o10',), ('o1',), ('o3',), ('o7',), ('o2',), ('o8',), ('o5',), ('o9',), ('o4',), ('o6',), ] )
rigid.next__count = set( [('n5', 'n6'), ('n6', 'n7'), ('n8', 'n9'), ('n1', 'n2'), ('n2', 'n3'), ('n0', 'n1'), ('n3', 'n4'), ('n4', 'n5'), ('n7', 'n8'), ('n9', 'n10'), ] )
state.stacks__avail = set( [('n0',), ] )
state.waiting = set( [('o10',), ('o1',), ('o3',), ('o7',), ('o2',), ('o8',), ('o5',), ('o9',), ('o4',), ('o6',), ] )
rigid.includes = set( [('o1', 'p6'), ('o7', 'p9'), ('o2', 'p2'), ('o10', 'p6'), ('o3', 'p10'), ('o5', 'p6'), ('o2', 'p3'), ('o4', 'p4'), ('o7', 'p6'), ('o9', 'p7'), ('o8', 'p1'), ('o7', 'p5'), ('o8', 'p4'), ('o6', 'p9'), ('o4', 'p8'), ] )
state.shipped = set( [] )
state.made = set( [] )
state.started = set( [] )

task_list = [('plan',)]
