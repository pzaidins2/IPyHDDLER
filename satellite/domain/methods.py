from ipyhop import Methods
import itertools

def take__one( state, rigid ):
	for d in rigid.direction:
		for m in rigid.mode:
			if all( [ ( d, m, ) in rigid.goal_have_image, not( ( d, m, ) in state.have_image ), ] ):
				yield [ ( 'have__image', d, m, ), ( 'main', ), ]

def turn__first( state, rigid ):
	for d in rigid.direction:
		for d1 in rigid.direction:
			for s in rigid.satellite:
				if all( [ ( s, d, ) in rigid.goal_pointing, ( s, d1, ) in state.pointing, not( ( d == d1 ) ), ] ):
					yield [ ( 'turn_to', s, d, d1, ), ( 'main', ), ]

def all__done( state, rigid ):
	if all( [ all( any( [ not( ( d, m, ) in rigid.goal_have_image ), ( d, m, ) in state.have_image, ] ) for ( d, m, ) in itertools.product( rigid.direction, rigid.mode, ) ), all( any( [ not( ( s, d, ) in rigid.goal_pointing ), ( s, d, ) in state.pointing, ] ) for ( s, d, ) in itertools.product( rigid.satellite, rigid.direction, ) ), ] ):
		yield [ ]

def prepare__then__take( state, d, m, rigid ):
	for i in rigid.instrument:
		for s in rigid.satellite:
			if ( i, s, ) in rigid.on_board:
				yield [ ( 'prepare__instrument', s, i, ), ( 'take__image', s, i, d, m, ), ]

def prepare( state, s, i, rigid ):
	yield [ ( 'turn__on__instrument', s, i, ), ( 'calibrate__instrument', s, i, ), ]

def already__on( state, s, i, rigid ):
	if ( i, ) in state.power_on:
		yield [ ]

def turn__on( state, s, i, rigid ):
	if ( s, ) in state.power_avail:
		yield [ ( 'switch_on', i, s, ), ]

def swap__instruments( state, s, i, rigid ):
	for j in rigid.instrument:
		if all( [ ( j, ) in state.power_on, not( ( i == j ) ), ] ):
			yield [ ( 'switch_off', j, s, ), ( 'switch_on', i, s, ), ]

def no__calibration__needed( state, s, i, rigid ):
	if all( [ ( i, ) in state.power_on, ( i, ) in state.calibrated, ] ):
		yield [ ]

def do__calibrate( state, s, i, rigid ):
	for d in rigid.direction:
		if all( [ ( i, ) in state.power_on, ( s, d, ) in state.pointing, ( i, d, ) in rigid.calibration_target, ] ):
			yield [ ( 'calibrate', s, i, d, ), ]

def repoint__then__calibrate( state, s, i, rigid ):
	for d in rigid.direction:
		for d2 in rigid.direction:
			if all( [ ( s, d2, ) in state.pointing, ( i, d, ) in rigid.calibration_target, not( ( d == d2 ) ), ] ):
				yield [ ( 'turn_to', s, d, d2, ), ( 'calibrate', s, i, d, ), ]

def simple__take__image( state, s, i, d, m, rigid ):
	for d__prev in rigid.direction:
		if all( [ ( s, d, ) in state.pointing, ] ):
			yield [ ( 'take_image', s, d, i, m, ), ]

def turn__then__take( state, s, i, d, m, rigid ):
	for d__prev in rigid.direction:
		if all( [ ( s, d__prev, ) in state.pointing, not( ( s, d, ) in state.pointing ), ] ):
			yield [ ( 'turn_to', s, d, d__prev, ), ( 'take_image', s, d, i, m, ), ]

methods = Methods()
methods.declare_task_methods( 'main', [ take__one, turn__first, all__done, ] )
methods.declare_task_methods( 'have__image', [ prepare__then__take, ] )
methods.declare_task_methods( 'prepare__instrument', [ prepare, ] )
methods.declare_task_methods( 'turn__on__instrument', [ already__on, turn__on, swap__instruments, ] )
methods.declare_task_methods( 'calibrate__instrument', [ no__calibration__needed, do__calibrate, repoint__then__calibrate, ] )
methods.declare_task_methods( 'take__image', [ simple__take__image, turn__then__take, ] )
