from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'n10', 'p6', 'n2', 'o2', 'n5', 'p7', 'p9', 'o5', 'o8', 'p5', 'o1', 'p4', 'n0', 'p1', 'p8', 'p10', 'n1', 'o3', 'o6', 'n3', 'p3', 'n4', 'o4', 'n6', 'n8', 'o9', 'n9', 'o7', 'p2', 'o10', 'n7'}
rigid.order = {'o3', 'o6', 'o2', 'o4', 'o5', 'o8', 'o9', 'o1', 'o7', 'o10'}
rigid.count = {'n10', 'n1', 'n3', 'n2', 'n4', 'n5', 'n6', 'n8', 'n9', 'n7', 'n0'}
rigid.product = {'p10', 'p6', 'p3', 'p7', 'p9', 'p5', 'p4', 'p2', 'p1', 'p8'}
rigid.goal__shipped = set( [('o3',), ('o7',), ('o10',), ('o5',), ('o6',), ('o2',), ('o8',), ('o4',), ('o1',), ('o9',), ] )
rigid.next__count = set( [('n9', 'n10'), ('n2', 'n3'), ('n4', 'n5'), ('n8', 'n9'), ('n6', 'n7'), ('n3', 'n4'), ('n7', 'n8'), ('n0', 'n1'), ('n1', 'n2'), ('n5', 'n6'), ] )
state.stacks__avail = set( [('n0',), ] )
state.waiting = set( [('o3',), ('o7',), ('o10',), ('o5',), ('o6',), ('o2',), ('o8',), ('o4',), ('o1',), ('o9',), ] )
rigid.includes = set( [('o1', 'p10'), ('o8', 'p3'), ('o7', 'p5'), ('o10', 'p9'), ('o1', 'p6'), ('o1', 'p9'), ('o5', 'p3'), ('o2', 'p10'), ('o3', 'p8'), ('o3', 'p7'), ('o4', 'p4'), ('o3', 'p1'), ('o6', 'p5'), ('o9', 'p1'), ('o2', 'p2'), ] )
state.shipped = set( [] )
state.started = set( [] )
state.made = set( [] )

task_list = [('plan',)]
