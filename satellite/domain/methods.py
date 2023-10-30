from ipyhop import Methods
import itertools

def take_one( state, rigid ):
	for d in rigid.direction:
		for m in rigid.mode:
			if all( [ ( d, m, ) in rigid.goal_have_image, not( ( d, m, ) in state.have_image ), ] ):
				yield [ ( 'have_image', d, m, ), ( 'main', ), ]

def turn_first( state, rigid ):
	for d in rigid.direction:
		for d1 in rigid.direction:
			for s in rigid.satellite:
				if all( [ ( s, d, ) in rigid.goal_pointing, ( s, d1, ) in state.pointing, not( ( d == d1 ) ), ] ):
					yield [ ( 'turn_to', s, d, d1, ), ( 'main', ), ]

def all_done( state, rigid ):
	if all( [ all( any( [ not( ( d, m, ) in rigid.goal_have_image ), ( d, m, ) in state.have_image, ] ) for ( d, m, ) in itertools.product( rigid.direction, rigid.mode, ) ), all( any( [ not( ( s, d, ) in rigid.goal_pointing ), ( s, d, ) in state.pointing, ] ) for ( s, d, ) in itertools.product( rigid.satellite, rigid.direction, ) ), ] ):
		yield [ ]

def prepare_then_take( state, d, m, rigid ):
	for i in rigid.instrument:
		for s in rigid.satellite:
			if ( i, s, ) in rigid.on_board:
				yield [ ( 'prepare_instrument', s, i, ), ( 'take_image_t', s, i, d, m, ), ]

def prepare( state, s, i, rigid ):
	yield [ ( 'turn_on_instrument', s, i, ), ( 'calibrate_instrument', s, i, ), ]

def already_on( state, s, i, rigid ):
	if ( i, ) in state.power_on:
		yield [ ]

def turn_on( state, s, i, rigid ):
	if ( s, ) in state.power_avail:
		yield [ ( 'switch_on', i, s, ), ]

def swap_instruments( state, s, i, rigid ):
	for j in rigid.instrument:
		if all( [ ( j, ) in state.power_on, not( ( i == j ) ), ] ):
			yield [ ( 'switch_off', j, s, ), ( 'switch_on', i, s, ), ]

def no_calibration_needed( state, s, i, rigid ):
	if all( [ ( i, ) in state.power_on, ( i, ) in state.calibrated, ] ):
		yield [ ]

def do_calibrate( state, s, i, rigid ):
	for d in rigid.direction:
		if all( [ ( i, ) in state.power_on, ( s, d, ) in state.pointing, ( i, d, ) in rigid.calibration_target, ] ):
			yield [ ( 'calibrate', s, i, d, ), ]

def repoint_then_calibrate( state, s, i, rigid ):
	for d in rigid.direction:
		for d2 in rigid.direction:
			if all( [ ( s, d2, ) in state.pointing, ( i, d, ) in rigid.calibration_target, not( ( d == d2 ) ), ] ):
				yield [ ( 'turn_to', s, d, d2, ), ( 'calibrate', s, i, d, ), ]

def turn_then_take( state, s, i, d, m, rigid ):
	for d_prev in rigid.direction:
		if all( [ ( s, d_prev, ) in state.pointing, ( d_prev != d ), ] ):
			yield [ ( 'turn_to', s, d, d_prev, ), ( 'take_image_a', s, d, i, m, ), ]

methods = Methods()
methods.declare_task_methods( 'main', [ take_one, turn_first, all_done, ] )
methods.declare_task_methods( 'have_image', [ prepare_then_take, ] )
methods.declare_task_methods( 'prepare_instrument', [ prepare, ] )
methods.declare_task_methods( 'turn_on_instrument', [ already_on, turn_on, swap_instruments, ] )
methods.declare_task_methods( 'calibrate_instrument', [ no_calibration_needed, do_calibrate, repoint_then_calibrate, ] )
methods.declare_task_methods( 'take_image_t', [ turn_then_take, ] )
