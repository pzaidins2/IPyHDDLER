from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'o3', 'p5', 'n2', 'p2', 'p3', 'n1', 'o4', 'n5', 'o1', 'p1', 'n0', 'o5', 'o2', 'n3', 'n4', 'p4'}
rigid.order = {'o3', 'o5', 'o2', 'o4', 'o1'}
rigid.count = {'n0', 'n2', 'n3', 'n5', 'n1', 'n4'}
rigid.product = {'p1', 'p5', 'p2', 'p3', 'p4'}
rigid.goal__shipped = set( [('o3',), ('o1',), ('o5',), ('o4',), ('o2',), ] )
rigid.next__count = set( [('n1', 'n2'), ('n3', 'n4'), ('n4', 'n5'), ('n2', 'n3'), ('n0', 'n1'), ] )
state.stacks__avail = set( [('n0',), ] )
state.waiting = set( [('o3',), ('o1',), ('o5',), ('o4',), ('o2',), ] )
rigid.includes = set( [('o3', 'p2'), ('o5', 'p1'), ('o1', 'p3'), ('o1', 'p1'), ('o2', 'p1'), ('o4', 'p5'), ('o3', 'p4'), ] )
state.started = set( [] )
state.shipped = set( [] )
state.made = set( [] )

task_list = [('plan',)]
