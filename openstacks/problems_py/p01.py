from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'n2', 'n3', 'p5', 'o1', 'p2', 'o2', 'p1', 'o5', 'p4', 'p3', 'o4', 'n4', 'n5', 'o3', 'n1', 'n0'}
rigid.count = {'n2', 'n4', 'n5', 'n3', 'n1', 'n0'}
rigid.order = {'o4', 'o1', 'o2', 'o3', 'o5'}
rigid.product = {'p4', 'p3', 'p5', 'p2', 'p1'}
rigid.goal__shipped = set( [('o4',), ('o2',), ('o1',), ('o3',), ('o5',), ] )
rigid.next__count = set( [('n4', 'n5'), ('n2', 'n3'), ('n3', 'n4'), ('n1', 'n2'), ('n0', 'n1'), ] )
state.stacks__avail = set( [('n0',), ] )
state.waiting = set( [('o4',), ('o2',), ('o1',), ('o3',), ('o5',), ] )
rigid.includes = set( [('o2', 'p2'), ('o3', 'p3'), ('o1', 'p2'), ('o2', 'p1'), ('o5', 'p5'), ('o4', 'p4'), ('o4', 'p3'), ] )
state.started = set( [] )
state.shipped = set( [] )
state.made = set( [] )

task_list = [('plan',)]
