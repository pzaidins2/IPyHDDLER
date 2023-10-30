from ipyhop import Actions
import itertools

def make_product( state, p, rigid ):
	if all( [ not( ( p, ) in state.made ), all( any( [ not( ( o, p, ) in rigid.includes ), not( ( o, ) in state.waiting ), ] ) for ( o, ) in itertools.product( rigid.order, ) ), ] ):
		state.made.add( ( p, ) )
		return state

def start_order( state, o, avail, new_avail, rigid ):
	if all( [ ( o, ) in state.waiting, ( avail, ) in state.stacks_avail, ( new_avail, avail, ) in rigid.next_count, ] ):
		state.waiting.remove( ( o, ) )
		state.started.add( ( o, ) )
		state.stacks_avail.remove( ( avail, ) )
		state.stacks_avail.add( ( new_avail, ) )
		return state

def ship_order( state, o, avail, new_avail, rigid ):
	if all( [ ( o, ) in state.started, all( any( [ not( ( o, p, ) in rigid.includes ), ( p, ) in state.made, ] ) for ( p, ) in itertools.product( rigid.product, ) ), ( avail, ) in state.stacks_avail, ( avail, new_avail, ) in rigid.next_count, ] ):
		state.started.remove( ( o, ) )
		state.shipped.add( ( o, ) )
		state.stacks_avail.remove( ( avail, ) )
		state.stacks_avail.add( ( new_avail, ) )
		return state

def open_new_stack( state, open, new_open, rigid ):
	if all( [ ( open, ) in state.stacks_avail, ( open, new_open, ) in rigid.next_count, ] ):
		state.stacks_avail.remove( ( open, ) )
		state.stacks_avail.add( ( new_open, ) )
		return state

def reset( state, o, rigid ):
	if all( [ ( o, ) in state.started, not( ( o, ) in state.shipped ), not( ( o, ) in state.waiting ), ] ):
		state.waiting.add( ( o, ) )
		state.started.remove( ( o, ) )
		return state

actions = Actions()
actions.declare_actions( [ make_product, start_order, ship_order, open_new_stack, reset, ] )
