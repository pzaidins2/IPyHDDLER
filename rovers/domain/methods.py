from ipyhop import Methods
import itertools

def achieve_communicated_image_data( state, obj, mode, rover, rigid ):
	for camera in rigid.camera:
		for l in rigid.lander:
			for lander_loc in rigid.location:
				for photo_loc in rigid.location:
					if all( [ ( camera, rover, ) in rigid.on_board, ( camera, mode, ) in rigid.supports, ( l, lander_loc, ) in rigid.at_lander, ] ):
						yield [ ( 'calibrate_camera', rover, camera, ), ( 'get_line_of_sight', rover, obj, photo_loc, ), ( 'take_image', rover, photo_loc, obj, camera, mode, ), ( 'communicate_image', photo_loc, lander_loc, rover, obj, mode, ), ]

def camera_already_calibrated( state, rover, camera, rigid ):
	if all( [ ( camera, rover, ) in state.calibrated, ] ):
		yield [ ]

def calibrate_the_camera( state, rover, camera, rigid ):
	for calibration_loc in rigid.location:
		for calibration_obj in rigid.objective:
			if all( [ not( ( camera, rover, ) in state.calibrated ), ( camera, calibration_obj, ) in rigid.calibration_target, ( calibration_obj, calibration_loc, ) in rigid.visible_from, ] ):
				yield [ ( 'move_to', rover, calibration_loc, ), ( 'calibrate', rover, camera, calibration_obj, calibration_loc, ), ]

def communicate_image_meth( state, rover_loc, lander_loc, rover, obj, mode, rigid ):
	for l in rigid.lander:
		if all( [ ( rover, rover_loc, ) in state.at, ( l, lander_loc, ) in rigid.at_lander, ( rover_loc, lander_loc, ) in rigid.visible, ] ):
			yield [ ( 'communicate_image_data_a', rover, l, obj, mode, rover_loc, lander_loc, ), ]

def relocate_then_communicate_image( state, rover_loc, lander_loc, rover, obj, mode, rigid ):
	for l in rigid.lander:
		for new_loc in rigid.location:
			if all( [ ( rover, rover_loc, ) in state.at, ( l, lander_loc, ) in rigid.at_lander, not( ( rover_loc, lander_loc, ) in rigid.visible ), ( new_loc, lander_loc, ) in rigid.visible, ] ):
				yield [ ( 'move_to', rover, new_loc, ), ( 'communicate_image_data_a', rover, l, obj, mode, new_loc, lander_loc, ), ]

def have_line_of_sight_for_photo( state, rover, obj, photo_loc, rigid ):
	if all( [ ( rover, photo_loc, ) in state.at, ( obj, photo_loc, ) in rigid.visible_from, ] ):
		yield [ ]

def need_line_of_sight( state, rover, obj, photo_loc, rigid ):
	for rover_loc in rigid.location:
		if all( [ ( rover, rover_loc, ) in state.at, not( ( obj, rover_loc, ) in rigid.visible_from ), ( obj, photo_loc, ) in rigid.visible_from, ] ):
			yield [ ( 'move_to', rover, photo_loc, ), ]

def achieve_communicated_soil_data( state, goal_loc, rover, rigid ):
	for rover_loc in rigid.location:
		for s in rigid.store:
			if ( s, rover, ) in rigid.store_of:
				yield [ ( 'move_to', rover, goal_loc, ), ( 'empty_store', s, rover, ), ( 'sample_soil', rover, s, goal_loc, ), ( 'transmit_soil', goal_loc, rover_loc, rover, ), ]

def already_there( state, rover, to, rigid ):
	if ( rover, to, ) in state.at:
		yield [ ]

def go_there( state, rover, to, rigid ):
	for from___ in rigid.location:
		for one_step in rigid.location:
			if all( [ not( ( rover, to, ) in state.at ), ( rover, from___, ) in state.at, ( rover, from___, one_step, ) in rigid.can_traverse, ] ):
				yield [ ( 'navigate', rover, from___, one_step, ), ( 'move_to', rover, to, ), ]

def have_line_of_sight_for_soil( state, analysis_loc, rover_loc, rover, rigid ):
	for l in rigid.lander:
		for lander_loc in rigid.location:
			if all( [ ( rover, rover_loc, ) in state.at, ( l, lander_loc, ) in rigid.at_lander, ( rover_loc, lander_loc, ) in rigid.visible, ] ):
				yield [ ( 'communicate_soil_data_a', rover, l, analysis_loc, rover_loc, lander_loc, ), ]

def go_to_line_of_sight_for_soil( state, analysis_loc, rover_loc, rover, rigid ):
	for l in rigid.lander:
		for lander_loc in rigid.location:
			for new_loc in rigid.location:
				if all( [ ( rover, rover_loc, ) in state.at, ( l, lander_loc, ) in rigid.at_lander, not( ( rover_loc, lander_loc, ) in rigid.visible ), ( new_loc, lander_loc, ) in rigid.visible, ] ):
					yield [ ( 'move_to', rover, new_loc, ), ( 'communicate_soil_data_a', rover, l, analysis_loc, new_loc, lander_loc, ), ]

def have_line_of_sight_for_image( state, analysis_loc, rover_loc, rover, rigid ):
	for l in rigid.lander:
		for lander_loc in rigid.location:
			for mode in rigid.mode:
				if all( [ ( rover, rover_loc, ) in state.at, ( rover, analysis_loc, mode, ) in state.have_image, ( l, lander_loc, ) in rigid.at_lander, ( rover_loc, lander_loc, ) in rigid.visible, ] ):
					yield [ ( 'communicate_image_data_a', rover, l, analysis_loc, mode, rover_loc, lander_loc, ), ]

def go_to_line_of_sight_for_image( state, analysis_loc, rover_loc, rover, rigid ):
	for l in rigid.lander:
		for lander_loc in rigid.location:
			for mode in rigid.mode:
				for new_loc in rigid.location:
					if all( [ ( rover, rover_loc, ) in state.at, ( rover, analysis_loc, mode, ) in state.have_image, ( l, lander_loc, ) in rigid.at_lander, not( ( rover_loc, lander_loc, ) in rigid.visible ), ( new_loc, lander_loc, ) in rigid.visible, ] ):
						yield [ ( 'move_to', rover, new_loc, ), ( 'communicate_image_data_a', rover, l, analysis_loc, mode, new_loc, lander_loc, ), ]

def already_empty( state, s, r, rigid ):
	if ( s, ) in state.empty:
		yield [ ]

def drop_to_empty( state, s, rover, rigid ):
	if not( ( s, ) in state.empty ):
		yield [ ( 'drop', rover, s, ), ]

def achieve_communicated_rock_data( state, goal_loc, rover, rigid ):
	for l in rigid.lander:
		for rover_loc in rigid.location:
			for s in rigid.store:
				if ( s, rover, ) in rigid.store_of:
					yield [ ( 'move_to', rover, goal_loc, ), ( 'empty_store', s, rover, ), ( 'sample_rock', rover, s, goal_loc, ), ( 'transmit_rock', goal_loc, rover_loc, rover, ), ]

def have_line_of_sight_for_rock( state, analysis_loc, rover_loc, rover, rigid ):
	for l in rigid.lander:
		for lander_loc in rigid.location:
			if all( [ ( rover, rover_loc, ) in state.at, ( l, lander_loc, ) in rigid.at_lander, ( rover_loc, lander_loc, ) in rigid.visible, ] ):
				yield [ ( 'communicate_rock_data_a', rover, l, analysis_loc, rover_loc, lander_loc, ), ]

def go_to_line_of_sight_for_rock( state, analysis_loc, rover_loc, rover, rigid ):
	for l in rigid.lander:
		for lander_loc in rigid.location:
			for new_loc in rigid.location:
				if all( [ ( rover, rover_loc, ) in state.at, ( l, lander_loc, ) in rigid.at_lander, not( ( rover_loc, lander_loc, ) in rigid.visible ), ( new_loc, lander_loc, ) in rigid.visible, ] ):
					yield [ ( 'move_to', rover, new_loc, ), ( 'communicate_rock_data_a', rover, l, analysis_loc, new_loc, lander_loc, ), ]

def check_for_all_goals_done( state, rigid ):
	if all( [ all( any( [ not( ( w, ) in rigid.goal_communicated_soil_data ), ( w, ) in state.communicated_soil_data, ] ) for ( w, ) in itertools.product( rigid.waypoint, ) ), all( any( [ not( ( w, ) in rigid.goal_communicated_rock_data ), ( w, ) in state.communicated_rock_data, ] ) for ( w, ) in itertools.product( rigid.waypoint, ) ), all( any( [ not( ( o, m, ) in rigid.goal_communicated_image_data ), ( o, m, ) in state.communicated_image_data, ] ) for ( m, o, ) in itertools.product( rigid.mode, rigid.objective, ) ), ] ):
		yield [ ]

def communicate_one_soil_data( state, rigid ):
	for goal_loc in rigid.location:
		for r in rigid.rover:
			if all( [ ( goal_loc, ) in rigid.goal_communicated_soil_data, not( ( goal_loc, ) in state.communicated_soil_data ), ] ):
				yield [ ( 'communicate_soil_data_t', goal_loc, r, ), ( 'achieve_goals', ), ]

def communicate_one_rock_data( state, rigid ):
	for goal_loc in rigid.location:
		for r in rigid.rover:
			if all( [ ( goal_loc, ) in rigid.goal_communicated_rock_data, not( ( goal_loc, ) in state.communicated_rock_data ), ] ):
				yield [ ( 'communicate_rock_data_t', goal_loc, r, ), ( 'achieve_goals', ), ]

def communicate_one_image_data( state, rigid ):
	for mode in rigid.mode:
		for obj in rigid.objective:
			for r in rigid.rover:
				if all( [ ( obj, mode, ) in rigid.goal_communicated_image_data, not( ( obj, mode, ) in state.communicated_image_data ), ] ):
					yield [ ( 'communicate_image_data_t', obj, mode, r, ), ( 'achieve_goals', ), ]

methods = Methods()
methods.declare_task_methods( 'communicate_image_data_t', [ achieve_communicated_image_data, ] )
methods.declare_task_methods( 'calibrate_camera', [ camera_already_calibrated, calibrate_the_camera, ] )
methods.declare_task_methods( 'communicate_image', [ communicate_image_meth, relocate_then_communicate_image, ] )
methods.declare_task_methods( 'get_line_of_sight', [ have_line_of_sight_for_photo, need_line_of_sight, ] )
methods.declare_task_methods( 'communicate_soil_data_t', [ achieve_communicated_soil_data, ] )
methods.declare_task_methods( 'move_to', [ already_there, go_there, ] )
methods.declare_task_methods( 'transmit_soil', [ have_line_of_sight_for_soil, go_to_line_of_sight_for_soil, ] )
methods.declare_task_methods( 'transmit_image', [ have_line_of_sight_for_image, go_to_line_of_sight_for_image, ] )
methods.declare_task_methods( 'empty_store', [ already_empty, drop_to_empty, ] )
methods.declare_task_methods( 'communicate_rock_data_t', [ achieve_communicated_rock_data, ] )
methods.declare_task_methods( 'transmit_rock', [ have_line_of_sight_for_rock, go_to_line_of_sight_for_rock, ] )
methods.declare_task_methods( 'achieve_goals', [ check_for_all_goals_done, communicate_one_soil_data, communicate_one_rock_data, communicate_one_image_data, ] )
