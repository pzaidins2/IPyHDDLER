from ipyhop import Actions
import itertools

def turn_to( state, s, d_new, d_prev, rigid ):
	if all( [ ( s, d_prev, ) in state.pointing, not( ( d_new == d_prev ) ), ] ):
		state.pointing.add( ( s, d_new, ) )
		state.pointing.remove( ( s, d_prev, ) )
		return state

def switch_on( state, i, s, rigid ):
	if all( [ ( i, s, ) in rigid.on_board, ( s, ) in state.power_avail, ] ):
		state.power_on.add( ( i, ) )
		state.calibrated.remove( ( i, ) ) if ( i, ) in state.calibrated else None
		state.power_avail.remove( ( s, ) )
		return state

def switch_off( state, i, s, rigid ):
	if all( [ ( i, s, ) in rigid.on_board, ( i, ) in state.power_on, ] ):
		state.power_on.remove( ( i, ) )
		state.power_avail.add( ( s, ) )
		return state

def calibrate( state, s, i, d, rigid ):
	if all( [ ( i, s, ) in rigid.on_board, ( i, d, ) in rigid.calibration_target, ( s, d, ) in state.pointing, ( i, ) in state.power_on, ] ):
		state.calibrated.add( ( i, ) )
		return state

def take_image( state, s, d, i, m, rigid ):
	if all( [ ( i, ) in state.calibrated, ( i, s, ) in rigid.on_board, ( i, m, ) in rigid.supports, ( i, ) in state.power_on, ( s, d, ) in state.pointing, ( i, ) in state.power_on, ] ):
		state.have_image.add( ( d, m, ) ) if not( ( d, m, ) in state.have_image ) else None
		return state

actions = Actions()
actions.declare_actions( [ turn_to, switch_on, switch_off, calibrate, take_image, ] )
