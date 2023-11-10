from ipyhop import Actions
import itertools

def make__product( state, p, rigid ):
	if all( [ not( ( p, ) in state.made ), all( any( [ not( ( o, p, ) in rigid.includes ), not( ( o, ) in state.waiting ), ] ) for ( o, ) in itertools.product( rigid.order, ) ), ] ):
		state.made.add( ( p, ) )
		return state

def start__order( state, o, avail, new__avail, rigid ):
	if all( [ ( o, ) in state.waiting, ( avail, ) in state.stacks__avail, ( new__avail, avail, ) in rigid.next__count, ] ):
		state.waiting.remove( ( o, ) )
		state.started.add( ( o, ) )
		state.stacks__avail.remove( ( avail, ) )
		state.stacks__avail.add( ( new__avail, ) )
		return state

def ship__order( state, o, avail, new__avail, rigid ):
	if all( [ ( o, ) in state.started, all( any( [ not( ( o, p, ) in rigid.includes ), ( p, ) in state.made, ] ) for ( p, ) in itertools.product( rigid.product, ) ), ( avail, ) in state.stacks__avail, ( avail, new__avail, ) in rigid.next__count, ] ):
		state.started.remove( ( o, ) )
		state.shipped.add( ( o, ) )
		state.stacks__avail.remove( ( avail, ) )
		state.stacks__avail.add( ( new__avail, ) )
		return state

def open__new__stack( state, open, new__open, rigid ):
	if all( [ ( open, ) in state.stacks__avail, ( open, new__open, ) in rigid.next__count, ] ):
		state.stacks__avail.remove( ( open, ) )
		state.stacks__avail.add( ( new__open, ) )
		return state

actions = Actions()
actions.declare_actions( [ make__product, start__order, ship__order, open__new__stack, ] )
