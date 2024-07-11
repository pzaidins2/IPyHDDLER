from ipyhop import Methods
import itertools

def take__one( state, rigid ):
	goal_need_image = rigid.goal_have_image - state.have_image
	for ( d, m ) in goal_need_image:
		yield [ ( 'have__image', d, m, ), ( 'main', ), ]

def turn__first( state, rigid ):
	for (s,d) in rigid.goal_pointing:
		try:
			d1 = next(filter(lambda x: x[0] == s and x[1] != d, state.pointing ))
		except StopIteration:
			continue
		yield [ ('turn_to', s, d, d1,), ('main',), ]


def all__done( state, rigid ):
	goal_need_image = rigid.goal_have_image - state.have_image
	goal_need_pointing = rigid.goal_pointing - state.pointing
	if all( [ len(goal_need_image) == 0, len( goal_need_pointing ) == 0 ] ):
		yield [ ]

def prepare__then__take( state, d, m, rigid ):
	for ( i, s, ) in rigid.on_board:
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
	for j in state.power_on:
		if not( i==j ):
			yield [ ( 'switch_off', j, s, ), ( 'switch_on', i, s, ), ]

def no__calibration__needed( state, s, i, rigid ):
	if all( [ ( i, ) in state.power_on, ( i, ) in state.calibrated, ] ):
		yield [ ]

def do__calibrate( state, s, i, rigid ):
	if ( i, ) in state.power_on:
		for d in rigid.direction:
			if all( [  ( s, d, ) in state.pointing, ( i, d, ) in rigid.calibration_target, ] ):
				yield [ ( 'calibrate', s, i, d, ), ]

def repoint__then__calibrate( state, s, i, rigid ):
	for d in rigid.direction:
		if ( i, d, ) in rigid.calibration_target:
			for d2 in rigid.direction:
				if all( [ ( s, d2, ) in state.pointing, not( ( d == d2 ) ), ] ):
					yield [ ( 'turn_to', s, d, d2, ), ( 'calibrate', s, i, d, ), ]

def simple__take__image( state, s, i, d, m, rigid ):
	if ( s, d, ) in state.pointing:
		yield [ ( 'take_image', s, d, i, m, ), ]

def turn__then__take( state, s, i, d, m, rigid ):
	if not( ( s, d, ) in state.pointing ):
		for d__prev in rigid.direction:
			if ( s, d__prev, ) in state.pointing:
				yield [ ( 'turn_to', s, d, d__prev, ), ( 'take_image', s, d, i, m, ), ]

methods = Methods()
methods.declare_task_methods( 'main', [ take__one, turn__first, all__done, ] )
methods.declare_task_methods( 'have__image', [ prepare__then__take, ] )
methods.declare_task_methods( 'prepare__instrument', [ prepare, ] )
methods.declare_task_methods( 'turn__on__instrument', [ already__on, turn__on, swap__instruments, ] )
methods.declare_task_methods( 'calibrate__instrument', [ no__calibration__needed, do__calibrate, repoint__then__calibrate, ] )
methods.declare_task_methods( 'take__image', [ simple__take__image, turn__then__take, ] )
