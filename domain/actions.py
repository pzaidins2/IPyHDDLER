from ipyhop import Actions

def drive( state, l1, l2 ):
	if all( [ ( l1, ) in state.at, not( ( l1, ) in state.tollarea ), ( l1, l2, ) in state.road, ] ):
		state.at.remove( ( l1, ) ); state.at.add( ( l2, ) ); 
		return state

def driveta( state, l1, l2 ):
	if all( [ ( l1, ) in state.at, ( l1, ) in state.tollarea, ( l1, l2, ) in state.road, ] ):
		state.at.remove( ( l1, ) ); state.at.add( ( l2, ) ); 
		return state

def paytoll( state, l ):
	if all( [ ( l, ) in state.at, ( l, ) in state.paylocation, ] ):
		return state

actions = Actions()
actions.declare_actions( [ drive, driveta, paytoll, ] )
