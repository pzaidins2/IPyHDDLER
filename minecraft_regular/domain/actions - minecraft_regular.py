from ipyhop import Actions
import itertools

def placeblock( state, location, t, rigid ):
	if all( [ ( location, ) in state.empty, ] ):
		state.empty.remove( ( location, ) )
		state.blockat.add( ( location, t, ) )
		return state

def removeblock( state, location, t, rigid ):
	if all( [ not( ( location, ) in state.empty ), ] ):
		state.empty.add( ( location, ) )
		state.blockat.remove( ( location, t, ) )
		return state

actions = Actions()
actions.declare_actions( [ placeblock, removeblock, ] )
