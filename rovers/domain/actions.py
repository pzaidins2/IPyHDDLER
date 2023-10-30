from ipyhop import Actions
import itertools

def navigate( state, x, y, z, rigid ):
	if all( [ ( x, y, z, ) in rigid.can_traverse, ( x, ) in rigid.available, ( x, y, ) in state.at, ( y, z, ) in rigid.visible, ] ):
		state.at.remove( ( x, y, ) )
		state.at.add( ( x, z, ) )
		return state

def sample_soil( state, x, s, p, rigid ):
	if all( [ ( x, p, ) in state.at, ( p, ) in state.at_soil_sample, ( x, ) in rigid.equipped_for_soil_analysis, ( s, x, ) in rigid.store_of, ( s, ) in state.empty, ] ):
		state.empty.remove( ( s, ) )
		state.full.add( ( s, ) )
		state.have_soil_analysis.add( ( x, p, ) )
		state.at_soil_sample.remove( ( p, ) )
		return state

def sample_rock( state, x, s, p, rigid ):
	if all( [ ( x, p, ) in state.at, ( p, ) in state.at_rock_sample, ( x, ) in rigid.equipped_for_rock_analysis, ( s, x, ) in rigid.store_of, ( s, ) in state.empty, ] ):
		state.empty.remove( ( s, ) )
		state.full.add( ( s, ) )
		state.have_rock_analysis.add( ( x, p, ) )
		state.at_rock_sample.remove( ( p, ) )
		return state

def drop( state, x, y, rigid ):
	if all( [ ( y, x, ) in rigid.store_of, ( y, ) in state.full, ] ):
		state.full.remove( ( y, ) )
		state.empty.add( ( y, ) )
		return state

def calibrate( state, r, i, t, w, rigid ):
	if all( [ ( r, ) in rigid.equipped_for_imaging, ( i, t, ) in rigid.calibration_target, ( r, w, ) in state.at, ( t, w, ) in rigid.visible_from, ( i, r, ) in rigid.on_board, ] ):
		state.calibrated.add( ( i, r, ) )
		return state

def take_image( state, r, p, o, i, m, rigid ):
	if all( [ ( i, r, ) in state.calibrated, ( i, r, ) in rigid.on_board, ( r, ) in rigid.equipped_for_imaging, ( i, m, ) in rigid.supports, ( o, p, ) in rigid.visible_from, ( r, p, ) in state.at, ] ):
		state.have_image.add( ( r, o, m, ) )
		state.calibrated.remove( ( i, r, ) )
		return state

def communicate_soil_data_a( state, r, l, p, x, y, rigid ):
	if all( [ ( r, x, ) in state.at, ( l, y, ) in rigid.at_lander, ( r, p, ) in state.have_soil_analysis, ( x, y, ) in rigid.visible, ( r, ) in rigid.available, ( l, ) in rigid.channel_free, ] ):
		state.communicated_soil_data.add( ( p, ) )
		return state

def communicate_rock_data_a( state, r, l, p, x, y, rigid ):
	if all( [ ( r, x, ) in state.at, ( l, y, ) in rigid.at_lander, ( r, p, ) in state.have_rock_analysis, ( x, y, ) in rigid.visible, ( r, ) in rigid.available, ( l, ) in rigid.channel_free, ] ):
		state.communicated_rock_data.add( ( p, ) )
		return state

def communicate_image_data_a( state, r, l, o, m, x, y, rigid ):
	if all( [ ( r, x, ) in state.at, ( l, y, ) in rigid.at_lander, ( r, o, m, ) in state.have_image, ( x, y, ) in rigid.visible, ( r, ) in rigid.available, ( l, ) in rigid.channel_free, ] ):
		state.communicated_image_data.add( ( o, m, ) )
		return state

actions = Actions()
actions.declare_actions( [ navigate, sample_soil, sample_rock, drop, calibrate, take_image, communicate_soil_data_a, communicate_rock_data_a, communicate_image_data_a, ] )
