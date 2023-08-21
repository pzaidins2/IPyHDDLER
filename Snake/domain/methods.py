from ipyhop import Methods
import itertools

def hunt_all( state, rigid ):
	for foodpos in rigid.location:
		for pos1 in rigid.location:
			for snake in rigid.snake:
				for snakepos in rigid.location:
					if all( [ ( foodpos, ) in state.mouse_at, ( snake, snakepos, ) in state.head, ( foodpos, pos1, ) in rigid.adjacent, ] ):
						yield [ ( 'move', snake, snakepos, pos1, ), ( 'strike', snake, pos1, foodpos, ), ( 'hunt', ), ]

def hunt_done( state, rigid ):
	if all( not( ( pos, ) in state.mouse_at ) for ( pos, ) in itertools.product( rigid.location, ) ):
		yield [ ]

def move_base( state, snake, snakepos, goalpos, rigid ):
	if ( snakepos == goalpos ):
		yield [ ]

def move_long_snake( state, snake, snakepos, goalpos, rigid ):
	for bodypos in rigid.location:
		for pos2 in rigid.location:
			for tailpos in rigid.location:
				if all( [ ( pos2, snakepos, ) in rigid.adjacent, not( ( pos2, ) in state.occupied ), ( snake, bodypos, tailpos, ) in state.connected, ( snake, tailpos, ) in state.tail, ] ):
					yield [ ( 'move_long', snake, pos2, snakepos, bodypos, tailpos, ), ( 'move', snake, pos2, goalpos, ), ]

def move_short_snake( state, snake, snakepos, goalpos, rigid ):
	for pos2 in rigid.location:
		if all( [ ( pos2, snakepos, ) in rigid.adjacent, not( ( pos2, ) in state.occupied ), ( snake, snakepos, ) in state.tail, ] ):
			yield [ ( 'move_short', snake, pos2, snakepos, ), ( 'move', snake, pos2, goalpos, ), ]

methods = Methods()
methods.declare_task_methods( 'hunt', [ hunt_all, hunt_done, ] )
methods.declare_task_methods( 'move', [ move_short_snake, move_long_snake, move_base, ] )
