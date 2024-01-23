from ipyhop import State

from ordered_set import OrderedSet

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = OrderedSet(['n0', 'n1', 'n2', 'n3', 'n4', 'n5', 'o1', 'o2', 'o3', 'o4', 'o5', 'p1', 'p2', 'p3', 'p4', 'p5'])
rigid.order = OrderedSet(['o1', 'o2', 'o3', 'o4', 'o5'])
rigid.product = OrderedSet(['p1', 'p2', 'p3', 'p4', 'p5'])
rigid.count = OrderedSet(['n0', 'n1', 'n2', 'n3', 'n4', 'n5'])
rigid.goal__shipped = OrderedSet( [('o1',), ('o2',), ('o3',), ('o4',), ('o5',), ] )
rigid.next__count = OrderedSet( [('n0', 'n1'), ('n1', 'n2'), ('n2', 'n3'), ('n3', 'n4'), ('n4', 'n5'), ] )
state.stacks__avail = OrderedSet( [('n0',), ] )
state.waiting = OrderedSet( [('o1',), ('o2',), ('o3',), ('o4',), ('o5',), ] )
rigid.includes = OrderedSet( [('o1', 'p1'), ('o1', 'p3'), ('o2', 'p1'), ('o3', 'p2'), ('o3', 'p4'), ('o4', 'p5'), ('o5', 'p1'), ] )
state.started = OrderedSet( [] )
state.shipped = OrderedSet( [] )
state.made = OrderedSet( [] )

task_list = [('plan',)]
