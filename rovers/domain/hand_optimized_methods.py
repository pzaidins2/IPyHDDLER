from ipyhop import Methods
import itertools

def achieve__communicated__image__data( state, obj, mode, rover, rigid ):
	for camera in rigid.camera:
		if all( [ ( camera, rover, ) in rigid.on_board, ( camera, mode, ) in rigid.supports, ] ):
			for ( l, lander__loc, ) in rigid.at_lander:
				for photo__loc in rigid.location:
					yield [ ( 'calibrate__camera', rover, camera, ), ( 'get__line__of__sight', rover, obj, photo__loc, ), ( 'take_image', rover, photo__loc, obj, camera, mode, ), ( 'communicate__image', photo__loc, lander__loc, rover, obj, mode, ), ]

def camera__already__calibrated( state, rover, camera, rigid ):
	if all( [ ( camera, rover, ) in state.calibrated, ] ):
		yield [ ]

def calibrate__the__camera( state, rover, camera, rigid ):
	for ( calibration__obj, calibration__loc, ) in rigid.visible_from:
		if all( [ not( ( camera, rover, ) in state.calibrated ), ( camera, calibration__obj, ) in rigid.calibration_target, ] ):
			yield [ ( 'move__to', rover, calibration__loc, ), ( 'calibrate', rover, camera, calibration__obj, calibration__loc, ), ]

def communicate__image__meth( state, rover__loc, lander__loc, rover, obj, mode, rigid ):
	for l in rigid.lander:
		if all( [ ( rover, rover__loc, ) in state.at, ( l, lander__loc, ) in rigid.at_lander, ( rover__loc, lander__loc, ) in rigid.visible, ] ):
			yield [ ( 'communicate_image_data', rover, l, obj, mode, rover__loc, lander__loc, ), ]

def relocate__then__communicate__image( state, rover__loc, lander__loc, rover, obj, mode, rigid ):
	for l in rigid.lander:
		for new__loc in rigid.location:
			if all( [ ( rover, rover__loc, ) in state.at, ( l, lander__loc, ) in rigid.at_lander, not( ( rover__loc, lander__loc, ) in rigid.visible ), ( new__loc, lander__loc, ) in rigid.visible, ] ):
				yield [ ( 'move__to', rover, new__loc, ), ( 'communicate_image_data', rover, l, obj, mode, new__loc, lander__loc, ), ]

def have__line__of__sight__for__photo( state, rover, obj, photo__loc, rigid ):
	if all( [ ( rover, photo__loc, ) in state.at, ( obj, photo__loc, ) in rigid.visible_from, ] ):
		yield [ ]

def need__line__of__sight( state, rover, obj, photo__loc, rigid ):
	for rover__loc in rigid.location:
		if all( [ ( rover, rover__loc, ) in state.at, not( ( obj, rover__loc, ) in rigid.visible_from ), ( obj, photo__loc, ) in rigid.visible_from, ] ):
			yield [ ( 'move__to', rover, photo__loc, ), ]

def achieve__communicated__soil__data( state, goal__loc, rover, rigid ):
	for s in rigid.store:
		if ( s, rover, ) in rigid.store_of:
			for rover__loc in rigid.location:
				yield [ ( 'move__to', rover, goal__loc, ), ( 'empty__store', s, rover, ), ( 'sample_soil', rover, s, goal__loc, ), ( 'transmit__soil', goal__loc, rover__loc, rover, ), ]

def already__there( state, rover, to, rigid ):
	if ( rover, to, ) in state.at:
		yield [ ]

def go__there( state, rover, to, rigid ):
	if not( ( rover, to, ) in state.at ):
		for from___ in rigid.location:
			if ( rover, from___, ) in state.at:
				for one__step in rigid.location:
					if ( rover, from___, one__step, ) in rigid.can_traverse:
						yield [ ( 'navigate', rover, from___, one__step, ), ( 'move__to', rover, to, ), ]

def have__line__of__sight__for__soil( state, analysis__loc, rover__loc, rover, rigid ):
	for ( l, lander__loc, ) in rigid.at_lander:
		if all( [ ( rover, rover__loc, ) in state.at, ( rover__loc, lander__loc, ) in rigid.visible, ] ):
			yield [ ( 'communicate_soil_data', rover, l, analysis__loc, rover__loc, lander__loc, ), ]

def go__to__line__of__sight__for__soil( state, analysis__loc, rover__loc, rover, rigid ):
	if ( rover, rover__loc, ) in state.at:
		for ( l, lander__loc, ) in rigid.at_lander:
			if not( ( rover__loc, lander__loc, ) in rigid.visible):
				for new__loc in rigid.location:
					if ( new__loc, lander__loc, ) in rigid.visible:
						yield [ ( 'move__to', rover, new__loc, ), ( 'communicate_soil_data', rover, l, analysis__loc, new__loc, lander__loc, ), ]

def have__line__of__sight__for__image( state, analysis__loc, rover__loc, rover, rigid ):
	if ( rover, rover__loc, ) in state.at:
		for ( l, lander__loc, ) in rigid.at_lander:
			if ( rover__loc, lander__loc, ) in rigid.visible:
				for mode in rigid.mode:
					if ( rover, analysis__loc, mode, ) in state.have_image:
						yield [ ( 'communicate_image_data', rover, l, analysis__loc, mode, rover__loc, lander__loc, ), ]

def go__to__line__of__sight__for__image( state, analysis__loc, rover__loc, rover, rigid ):
	if ( rover, rover__loc, ) in state.at:
		for ( l, lander__loc, ) in rigid.at_lander:
			if not( ( rover__loc, lander__loc, ) in rigid.visible ):
				for mode in rigid.mode:
					if ( rover, analysis__loc, mode, ) in state.have_image:
						for new__loc in rigid.location:
							if ( new__loc, lander__loc, ) in rigid.visible:
								yield [ ( 'move__to', rover, new__loc, ), ( 'communicate_image_data', rover, l, analysis__loc, mode, new__loc, lander__loc, ), ]

def already__empty( state, s, r, rigid ):
	if ( s, ) in state.empty:
		yield [ ]

def drop__to__empty( state, s, rover, rigid ):
	if not( ( s, ) in state.empty ):
		yield [ ( 'drop', rover, s, ), ]

def achieve__communicated__rock__data( state, goal__loc, rover, rigid ):
	for s in rigid.store:
		if ( s, rover, ) in rigid.store_of:
			for rover__loc in rigid.location:
				yield [ ( 'move__to', rover, goal__loc, ), ( 'empty__store', s, rover, ), ( 'sample_rock', rover, s, goal__loc, ), ( 'transmit__rock', goal__loc, rover__loc, rover, ), ]

def have__line__of__sight__for__rock( state, analysis__loc, rover__loc, rover, rigid ):
	if ( rover, rover__loc, ) in state.at:
		for ( l, lander__loc, ) in rigid.at_lander:
			if ( rover__loc, lander__loc, ) in rigid.visible:
				yield [ ( 'communicate_rock_data', rover, l, analysis__loc, rover__loc, lander__loc, ), ]

def go__to__line__of__sight__for__rock( state, analysis__loc, rover__loc, rover, rigid ):
	if ( rover, rover__loc, ) in state.at:
		for ( l, lander__loc, ) in rigid.at_lander:
			if not( ( rover__loc, lander__loc, ) in rigid.visible ):
				for new__loc in rigid.location:
					if ( new__loc, lander__loc, ) in rigid.visible:
						yield [ ( 'move__to', rover, new__loc, ), ( 'communicate_rock_data', rover, l, analysis__loc, new__loc, lander__loc, ), ]

def check__for__all__goals__done( state, rigid ):
	uncommunicated_soil_data = rigid.goal_communicated_soil_data - state.communicated_soil_data
	uncommunicated_rock_data = rigid.goal_communicated_rock_data - state.communicated_rock_data
	uncommunicated_image_data = rigid.goal_communicated_image_data - state.communicated_image_data
	if ( len(uncommunicated_soil_data) + len(uncommunicated_rock_data) + len(uncommunicated_image_data) ) == 0:
		yield [ ]

def communicate__one__soil__data( state, rigid ):
	uncommunicated_soil_data = rigid.goal_communicated_soil_data - state.communicated_soil_data
	for goal__loc in uncommunicated_soil_data:
		for r in rigid.rover:
			yield [ ( 'communicate__soil__data', goal__loc, r, ), ( 'achieve__goals', ), ]

def communicate__one__rock__data( state, rigid ):
	uncommunicated_rock_data = rigid.goal_communicated_rock_data - state.communicated_rock_data
	for goal__loc in uncommunicated_rock_data:
		for r in rigid.rover:
			yield [ ( 'communicate__rock__data', goal__loc, r, ), ( 'achieve__goals', ), ]

def communicate__one__image__data( state, rigid ):
	uncommunicated_image_data = rigid.goal_communicated_image_data - state.communicated_image_data
	for (obj, mode) in uncommunicated_image_data:
		for r in rigid.rover:
			yield [ ( 'communicate__image__data', obj, mode, r, ), ( 'achieve__goals', ), ]

methods = Methods()
methods.declare_task_methods( 'communicate__image__data', [ achieve__communicated__image__data, ] )
methods.declare_task_methods( 'calibrate__camera', [ camera__already__calibrated, calibrate__the__camera, ] )
methods.declare_task_methods( 'communicate__image', [ communicate__image__meth, relocate__then__communicate__image, ] )
methods.declare_task_methods( 'get__line__of__sight', [ have__line__of__sight__for__photo, need__line__of__sight, ] )
methods.declare_task_methods( 'communicate__soil__data', [ achieve__communicated__soil__data, ] )
methods.declare_task_methods( 'move__to', [ already__there, go__there, ] )
methods.declare_task_methods( 'transmit__soil', [ have__line__of__sight__for__soil, go__to__line__of__sight__for__soil, ] )
methods.declare_task_methods( 'transmit__image', [ have__line__of__sight__for__image, go__to__line__of__sight__for__image, ] )
methods.declare_task_methods( 'empty__store', [ already__empty, drop__to__empty, ] )
methods.declare_task_methods( 'communicate__rock__data', [ achieve__communicated__rock__data, ] )
methods.declare_task_methods( 'transmit__rock', [ have__line__of__sight__for__rock, go__to__line__of__sight__for__rock, ] )
methods.declare_task_methods( 'achieve__goals', [ check__for__all__goals__done, communicate__one__soil__data, communicate__one__rock__data, communicate__one__image__data, ] )
