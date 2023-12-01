from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'waypoint6', 'camera4', 'rover3', 'objective0', 'rover3store', 'camera0', 'objective3', 'objective1', 'camera2', 'camera1', 'waypoint5', 'general', 'waypoint0', 'waypoint1', 'rover1', 'waypoint2', 'waypoint3', 'camera3', 'rover0', 'rover2store', 'high_res', 'rover2', 'rover0store', 'rover1store', 'objective2', 'colour', 'low_res', 'camera5', 'waypoint4'}
rigid.lander = {'general'}
rigid.mode = {'colour', 'high_res', 'low_res'}
rigid.camera = {'camera4', 'camera2', 'camera3', 'camera1', 'camera0', 'camera5'}
rigid.location = {'waypoint3', 'waypoint6', 'objective0', 'objective1', 'objective3', 'objective2', 'waypoint5', 'waypoint0', 'waypoint1', 'waypoint2', 'waypoint4'}
rigid.objective = {'objective0', 'objective2', 'objective3', 'objective1'}
rigid.store = {'rover1store', 'rover2store', 'rover3store', 'rover0store'}
rigid.waypoint = {'waypoint3', 'waypoint6', 'waypoint5', 'waypoint0', 'waypoint1', 'waypoint2', 'waypoint4'}
rigid.rover = {'rover0', 'rover3', 'rover1', 'rover2'}
rigid.visible = set( [('waypoint5', 'waypoint0'), ('waypoint0', 'waypoint5'), ('waypoint4', 'waypoint0'), ('waypoint5', 'waypoint6'), ('waypoint0', 'waypoint6'), ('waypoint0', 'waypoint2'), ('waypoint5', 'waypoint3'), ('waypoint4', 'waypoint6'), ('waypoint6', 'waypoint4'), ('waypoint4', 'waypoint2'), ('waypoint1', 'waypoint4'), ('waypoint4', 'waypoint3'), ('waypoint1', 'waypoint5'), ('waypoint1', 'waypoint0'), ('waypoint6', 'waypoint5'), ('waypoint6', 'waypoint0'), ('waypoint2', 'waypoint1'), ('waypoint1', 'waypoint2'), ('waypoint3', 'waypoint4'), ('waypoint6', 'waypoint2'), ('waypoint3', 'waypoint5'), ('waypoint2', 'waypoint4'), ('waypoint2', 'waypoint0'), ('waypoint5', 'waypoint1'), ('waypoint0', 'waypoint1'), ('waypoint0', 'waypoint4'), ('waypoint2', 'waypoint6'), ('waypoint4', 'waypoint1'), ] )
state.at_soil_sample = set( [('waypoint3',), ('waypoint4',), ('waypoint0',), ('waypoint6',), ] )
state.at_rock_sample = set( [('waypoint1',), ('waypoint4',), ('waypoint6',), ('waypoint3',), ('waypoint0',), ] )
rigid.at_lander = set( [('general', 'waypoint1'), ] )
rigid.channel_free = set( [('general',), ] )
state.at = set( [('rover0', 'waypoint4'), ('rover2', 'waypoint3'), ('rover3', 'waypoint1'), ('rover1', 'waypoint0'), ] )
rigid.available = set( [('rover2',), ('rover3',), ('rover0',), ('rover1',), ] )
rigid.store_of = set( [('rover2store', 'rover2'), ('rover0store', 'rover0'), ('rover1store', 'rover1'), ('rover3store', 'rover3'), ] )
state.empty = set( [('rover3store',), ('rover0store',), ('rover2store',), ('rover1store',), ] )
rigid.equipped_for_soil_analysis = set( [('rover3',), ('rover0',), ('rover1',), ] )
rigid.equipped_for_rock_analysis = set( [('rover2',), ('rover3',), ('rover0',), ] )
rigid.can_traverse = set( [('rover0', 'waypoint4', 'waypoint3'), ('rover0', 'waypoint1', 'waypoint5'), ('rover2', 'waypoint4', 'waypoint1'), ('rover3', 'waypoint5', 'waypoint6'), ('rover2', 'waypoint0', 'waypoint4'), ('rover1', 'waypoint1', 'waypoint0'), ('rover2', 'waypoint5', 'waypoint3'), ('rover3', 'waypoint4', 'waypoint0'), ('rover2', 'waypoint4', 'waypoint0'), ('rover3', 'waypoint0', 'waypoint6'), ('rover3', 'waypoint0', 'waypoint2'), ('rover0', 'waypoint3', 'waypoint4'), ('rover3', 'waypoint6', 'waypoint5'), ('rover3', 'waypoint6', 'waypoint0'), ('rover0', 'waypoint2', 'waypoint4'), ('rover3', 'waypoint4', 'waypoint3'), ('rover2', 'waypoint4', 'waypoint2'), ('rover2', 'waypoint4', 'waypoint3'), ('rover1', 'waypoint2', 'waypoint0'), ('rover0', 'waypoint5', 'waypoint1'), ('rover1', 'waypoint0', 'waypoint1'), ('rover2', 'waypoint1', 'waypoint4'), ('rover3', 'waypoint1', 'waypoint0'), ('rover0', 'waypoint4', 'waypoint1'), ('rover0', 'waypoint0', 'waypoint4'), ('rover3', 'waypoint3', 'waypoint4'), ('rover3', 'waypoint0', 'waypoint4'), ('rover2', 'waypoint2', 'waypoint4'), ('rover0', 'waypoint4', 'waypoint0'), ('rover2', 'waypoint3', 'waypoint4'), ('rover3', 'waypoint2', 'waypoint0'), ('rover2', 'waypoint3', 'waypoint5'), ('rover1', 'waypoint0', 'waypoint6'), ('rover1', 'waypoint0', 'waypoint2'), ('rover3', 'waypoint0', 'waypoint1'), ('rover1', 'waypoint6', 'waypoint0'), ('rover0', 'waypoint4', 'waypoint6'), ('rover0', 'waypoint6', 'waypoint4'), ('rover0', 'waypoint4', 'waypoint2'), ('rover0', 'waypoint1', 'waypoint4'), ] )
rigid.equipped_for_imaging = set( [('rover3',), ('rover2',), ('rover1',), ] )
rigid.on_board = set( [('camera3', 'rover1'), ('camera1', 'rover1'), ('camera0', 'rover1'), ('camera5', 'rover3'), ('camera2', 'rover1'), ('camera4', 'rover2'), ] )
rigid.calibration_target = set( [('camera2', 'objective1'), ('camera5', 'objective0'), ('camera0', 'objective2'), ('camera1', 'objective3'), ('camera3', 'objective2'), ('camera4', 'objective0'), ] )
rigid.supports = set( [('camera5', 'high_res'), ('camera4', 'colour'), ('camera0', 'low_res'), ('camera3', 'low_res'), ('camera1', 'colour'), ('camera5', 'low_res'), ('camera5', 'colour'), ('camera2', 'low_res'), ('camera3', 'high_res'), ('camera2', 'colour'), ] )
rigid.visible_from = set( [('objective0', 'waypoint0'), ('objective1', 'waypoint1'), ('objective3', 'waypoint3'), ('objective3', 'waypoint4'), ('objective3', 'waypoint2'), ('objective2', 'waypoint2'), ('objective2', 'waypoint3'), ('objective3', 'waypoint0'), ('objective3', 'waypoint5'), ('objective1', 'waypoint2'), ('objective2', 'waypoint0'), ('objective1', 'waypoint3'), ('objective1', 'waypoint0'), ('objective3', 'waypoint1'), ('objective2', 'waypoint1'), ] )
rigid.goal_communicated_soil_data = set( [('waypoint3',), ('waypoint4',), ('waypoint0',), ('waypoint6',), ] )
rigid.goal_communicated_rock_data = set( [('waypoint1',), ('waypoint3',), ('waypoint4',), ('waypoint0',), ] )
rigid.goal_communicated_image_data = set( [('objective2', 'colour'), ('objective3', 'low_res'), ('objective3', 'colour'), ] )
state.have_soil_analysis = set( [] )
state.communicated_rock_data = set( [] )
state.communicated_image_data = set( [] )
state.communicated_soil_data = set( [] )
state.calibrated = set( [] )
state.full = set( [] )
state.have_image = set( [] )
state.have_rock_analysis = set( [] )

task_list = [('achieve__goals',)]