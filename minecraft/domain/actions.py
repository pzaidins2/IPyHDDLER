from ipyhop import Actions
import itertools

def walk( state, locp, locn, rigid ):
	print( [ ( locp, ) in state.player_at, ( locn, ) in state.empty, ] )
	if all( [ ( locp, ) in state.player_at, ( locn, ) in state.empty, ] ):
		state.player_at.add( ( locn, ) )
		state.player_at.remove( ( locp, ) )
		return state

def placeblock( state, location, t, rigid ):
	print([ ( location, ) in state.empty, ])
	if all( [ ( location, ) in state.empty, ] ):
		state.empty.remove( ( location, ) )
		state.blockat.add( ( location, t, ) )
		return state

def removeblock( state, location, t, rigid ):
	print( not( ( location, ) in state.empty ) )
	if all( [ not( ( location, ) in state.empty ), ] ):
		state.empty.add( ( location, ) )
		state.blockat.remove( ( location, t, ) )
		return state

actions = Actions()
actions.declare_actions( [ walk, placeblock, removeblock, ] )
