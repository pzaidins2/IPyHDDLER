from ipyhop import Actions
import itertools

def strike( state, snake, headpos, foodpos, rigid ):
	if all( [ ( snake, headpos, ) in state.head, ( foodpos, ) in state.mouse_at, ( foodpos, headpos, ) in rigid.adjacent, not( ( headpos == foodpos ) ), ] ):
		state.mouse_at.remove( ( foodpos, ) )
		state.head.remove( ( snake, headpos, ) )
		state.connected.add( ( snake, foodpos, headpos, ) )
		state.head.add( ( snake, foodpos, ) )
		return state

def move_short( state, snake, nextpos, snakepos, rigid ):
	if all( [ ( snake, snakepos, ) in state.head, ( snake, snakepos, ) in state.tail, ( nextpos, snakepos, ) in rigid.adjacent, not( ( nextpos, ) in state.occupied ), ] ):
		state.head.remove( ( snake, snakepos, ) )
		state.tail.remove( ( snake, snakepos, ) )
		state.occupied.add( ( nextpos, ) )
		state.head.add( ( snake, nextpos, ) )
		state.tail.add( ( snake, nextpos, ) )
		state.occupied.remove( ( snakepos, ) )
		return state

def move_long( state, snake, nextpos, headpos, bodypos, tailpos, rigid ):
	if all( [ ( snake, headpos, ) in state.head, ( snake, bodypos, tailpos, ) in state.connected, ( snake, tailpos, ) in state.tail, ( nextpos, headpos, ) in rigid.adjacent, ( bodypos, tailpos, ) in rigid.adjacent, not( ( nextpos, ) in state.occupied ), not( ( bodypos == nextpos ) ), not( ( tailpos == nextpos ) ), not( ( headpos == tailpos ) ), ] ):
		# print( state.occupied )
		# print( state.head )
		# print( state.tail )
		# print( tailpos )
		# print( (snake, tailpos,) in state.tail )
		state.head.remove( ( snake, headpos, ) )
		state.head.add( ( snake, nextpos, ) )
		state.tail.remove( ( snake, tailpos, ) )
		state.tail.add( ( snake, bodypos, ) )
		state.connected.remove( ( snake, bodypos, tailpos, ) )
		state.connected.add( ( snake, nextpos, headpos, ) )
		state.occupied.add( ( nextpos, ) )

		state.occupied.remove( ( tailpos, ) )
		return state

actions = Actions()
actions.declare_actions( [ strike, move_short, move_long, ] )
