from ipyhop import State

from ordered_set import OrderedSet

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.location = OrderedSet(['objective0', 'objective1', 'objective2', 'waypoint0', 'waypoint1', 'waypoint2', 'waypoint3', 'waypoint4', 'waypoint5'])
rigid.objective = OrderedSet(['objective0', 'objective1', 'objective2'])
rigid.waypoint = OrderedSet(['waypoint0', 'waypoint1', 'waypoint2', 'waypoint3', 'waypoint4', 'waypoint5'])
rigid.object = OrderedSet(['general', 'waypoint0', 'waypoint1', 'waypoint2', 'waypoint3', 'waypoint4', 'waypoint5', 'rover0', 'rover1', 'rover2', 'rover3', 'rover0store', 'rover1store', 'rover2store', 'rover3store', 'objective0', 'objective1', 'objective2', 'colour', 'high_res', 'low_res', 'camera0', 'camera1', 'camera2', 'camera3'])
rigid.camera = OrderedSet(['camera0', 'camera1', 'camera2', 'camera3'])
rigid.lander = OrderedSet(['general'])
rigid.mode = OrderedSet(['colour', 'high_res', 'low_res'])
rigid.rover = OrderedSet(['rover0', 'rover1', 'rover2', 'rover3'])
rigid.store = OrderedSet(['rover0store', 'rover1store', 'rover2store', 'rover3store'])
rigid.visible = OrderedSet( [('waypoint0', 'waypoint1'), ('waypoint1', 'waypoint0'), ('waypoint0', 'waypoint3'), ('waypoint3', 'waypoint0'), ('waypoint1', 'waypoint5'), ('waypoint5', 'waypoint1'), ('waypoint2', 'waypoint0'), ('waypoint0', 'waypoint2'), ('waypoint2', 'waypoint1'), ('waypoint1', 'waypoint2'), ('waypoint2', 'waypoint3'), ('waypoint3', 'waypoint2'), ('waypoint2', 'waypoint4'), ('waypoint4', 'waypoint2'), ('waypoint3', 'waypoint4'), ('waypoint4', 'waypoint3'), ('waypoint3', 'waypoint5'), ('waypoint5', 'waypoint3'), ('waypoint4', 'waypoint0'), ('waypoint0', 'waypoint4'), ('waypoint4', 'waypoint1'), ('waypoint1', 'waypoint4'), ('waypoint5', 'waypoint2'), ('waypoint2', 'waypoint5'), ('waypoint5', 'waypoint4'), ('waypoint4', 'waypoint5'), ] )
state.at_soil_sample = OrderedSet( [('waypoint1',), ('waypoint3',), ('waypoint4',), ] )
state.at_rock_sample = OrderedSet( [('waypoint2',), ('waypoint3',), ('waypoint4',), ('waypoint5',), ] )
rigid.at_lander = OrderedSet( [('general', 'waypoint0'), ] )
rigid.channel_free = OrderedSet( [('general',), ] )
state.at = OrderedSet( [('rover0', 'waypoint2'), ('rover1', 'waypoint2'), ('rover2', 'waypoint2'), ('rover3', 'waypoint3'), ] )
rigid.available = OrderedSet( [('rover0',), ('rover1',), ('rover2',), ('rover3',), ] )
rigid.store_of = OrderedSet( [('rover0store', 'rover0'), ('rover1store', 'rover1'), ('rover2store', 'rover2'), ('rover3store', 'rover3'), ] )
state.empty = OrderedSet( [('rover0store',), ('rover1store',), ('rover2store',), ('rover3store',), ] )
rigid.equipped_for_soil_analysis = OrderedSet( [('rover0',), ('rover3',), ] )
rigid.equipped_for_rock_analysis = OrderedSet( [('rover0',), ('rover1',), ('rover2',), ('rover3',), ] )
rigid.can_traverse = OrderedSet( [('rover0', 'waypoint2', 'waypoint0'), ('rover0', 'waypoint0', 'waypoint2'), ('rover0', 'waypoint2', 'waypoint3'), ('rover0', 'waypoint3', 'waypoint2'), ('rover0', 'waypoint2', 'waypoint4'), ('rover0', 'waypoint4', 'waypoint2'), ('rover0', 'waypoint0', 'waypoint1'), ('rover0', 'waypoint1', 'waypoint0'), ('rover0', 'waypoint3', 'waypoint5'), ('rover0', 'waypoint5', 'waypoint3'), ('rover1', 'waypoint2', 'waypoint0'), ('rover1', 'waypoint0', 'waypoint2'), ('rover1', 'waypoint2', 'waypoint3'), ('rover1', 'waypoint3', 'waypoint2'), ('rover1', 'waypoint2', 'waypoint5'), ('rover1', 'waypoint5', 'waypoint2'), ('rover1', 'waypoint0', 'waypoint1'), ('rover1', 'waypoint1', 'waypoint0'), ('rover1', 'waypoint3', 'waypoint4'), ('rover1', 'waypoint4', 'waypoint3'), ('rover2', 'waypoint2', 'waypoint0'), ('rover2', 'waypoint0', 'waypoint2'), ('rover2', 'waypoint2', 'waypoint1'), ('rover2', 'waypoint1', 'waypoint2'), ('rover2', 'waypoint2', 'waypoint4'), ('rover2', 'waypoint4', 'waypoint2'), ('rover2', 'waypoint2', 'waypoint5'), ('rover2', 'waypoint5', 'waypoint2'), ('rover2', 'waypoint0', 'waypoint3'), ('rover2', 'waypoint3', 'waypoint0'), ('rover3', 'waypoint3', 'waypoint0'), ('rover3', 'waypoint0', 'waypoint3'), ('rover3', 'waypoint3', 'waypoint2'), ('rover3', 'waypoint2', 'waypoint3'), ('rover3', 'waypoint3', 'waypoint4'), ('rover3', 'waypoint4', 'waypoint3'), ('rover3', 'waypoint0', 'waypoint1'), ('rover3', 'waypoint1', 'waypoint0'), ('rover3', 'waypoint2', 'waypoint5'), ('rover3', 'waypoint5', 'waypoint2'), ] )
rigid.equipped_for_imaging = OrderedSet( [('rover1',), ('rover2',), ('rover3',), ] )
rigid.on_board = OrderedSet( [('camera0', 'rover3'), ('camera1', 'rover3'), ('camera2', 'rover1'), ('camera3', 'rover2'), ] )
rigid.calibration_target = OrderedSet( [('camera0', 'objective1'), ('camera1', 'objective0'), ('camera2', 'objective0'), ('camera3', 'objective1'), ] )
rigid.supports = OrderedSet( [('camera0', 'colour'), ('camera0', 'high_res'), ('camera0', 'low_res'), ('camera1', 'colour'), ('camera1', 'high_res'), ('camera2', 'colour'), ('camera2', 'high_res'), ('camera2', 'low_res'), ('camera3', 'colour'), ('camera3', 'low_res'), ] )
rigid.visible_from = OrderedSet( [('objective0', 'waypoint0'), ('objective0', 'waypoint1'), ('objective0', 'waypoint2'), ('objective1', 'waypoint0'), ('objective2', 'waypoint0'), ('objective2', 'waypoint1'), ('objective2', 'waypoint2'), ] )
rigid.goal_communicated_soil_data = OrderedSet( [('waypoint1',), ('waypoint3',), ('waypoint4',), ] )
rigid.goal_communicated_rock_data = OrderedSet( [('waypoint5',), ('waypoint4',), ] )
rigid.goal_communicated_image_data = OrderedSet( [('objective0', 'low_res'), ('objective0', 'high_res'), ('objective2', 'low_res'), ] )
state.full = OrderedSet( [] )
state.have_rock_analysis = OrderedSet( [] )
state.have_soil_analysis = OrderedSet( [] )
state.calibrated = OrderedSet( [] )
state.have_image = OrderedSet( [] )
state.communicated_soil_data = OrderedSet( [] )
state.communicated_rock_data = OrderedSet( [] )
state.communicated_image_data = OrderedSet( [] )

task_list = [('achieve__goals',)]
