from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'objective2', 'waypoint3', 'rover2', 'rover0store', 'rover1', 'rover2store', 'high_res', 'camera0', 'objective1', 'waypoint4', 'waypoint0', 'general', 'waypoint2', 'waypoint6', 'rover3', 'objective0', 'rover1store', 'rover0', 'rover3store', 'colour', 'camera3', 'camera4', 'camera2', 'waypoint1', 'low_res', 'camera1', 'waypoint5'}
rigid.lander = {'general'}
rigid.rover = {'rover1', 'rover2', 'rover3', 'rover0'}
rigid.location = {'waypoint2', 'objective2', 'objective0', 'waypoint3', 'objective1', 'waypoint6', 'waypoint1', 'waypoint4', 'waypoint0', 'waypoint5'}
rigid.objective = {'objective2', 'objective0', 'objective1'}
rigid.store = {'rover2store', 'rover0store', 'rover1store', 'rover3store'}
rigid.camera = {'camera0', 'camera4', 'camera2', 'camera3', 'camera1'}
rigid.mode = {'high_res', 'low_res', 'colour'}
rigid.waypoint = {'waypoint2', 'waypoint0', 'waypoint3', 'waypoint1', 'waypoint4', 'waypoint6', 'waypoint5'}
rigid.visible = set( [('waypoint1', 'waypoint3'), ('waypoint4', 'waypoint3'), ('waypoint1', 'waypoint4'), ('waypoint1', 'waypoint0'), ('waypoint5', 'waypoint0'), ('waypoint2', 'waypoint0'), ('waypoint0', 'waypoint2'), ('waypoint6', 'waypoint2'), ('waypoint1', 'waypoint5'), ('waypoint0', 'waypoint3'), ('waypoint2', 'waypoint5'), ('waypoint4', 'waypoint1'), ('waypoint5', 'waypoint1'), ('waypoint2', 'waypoint1'), ('waypoint3', 'waypoint0'), ('waypoint3', 'waypoint4'), ('waypoint6', 'waypoint3'), ('waypoint6', 'waypoint0'), ('waypoint1', 'waypoint6'), ('waypoint4', 'waypoint6'), ('waypoint6', 'waypoint4'), ('waypoint2', 'waypoint6'), ('waypoint5', 'waypoint6'), ('waypoint0', 'waypoint5'), ('waypoint0', 'waypoint1'), ('waypoint6', 'waypoint5'), ('waypoint3', 'waypoint1'), ('waypoint0', 'waypoint6'), ('waypoint1', 'waypoint2'), ('waypoint6', 'waypoint1'), ('waypoint5', 'waypoint2'), ('waypoint3', 'waypoint6'), ] )
state.at_soil_sample = set( [('waypoint6',), ('waypoint4',), ('waypoint0',), ('waypoint5',), ('waypoint1',), ] )
state.at_rock_sample = set( [('waypoint3',), ('waypoint6',), ('waypoint0',), ('waypoint5',), ('waypoint1',), ] )
rigid.at_lander = set( [('general', 'waypoint4'), ] )
rigid.channel_free = set( [('general',), ] )
state.at = set( [('rover1', 'waypoint2'), ('rover0', 'waypoint5'), ('rover3', 'waypoint2'), ('rover2', 'waypoint0'), ] )
rigid.available = set( [('rover1',), ('rover3',), ('rover0',), ('rover2',), ] )
rigid.store_of = set( [('rover0store', 'rover0'), ('rover3store', 'rover3'), ('rover1store', 'rover1'), ('rover2store', 'rover2'), ] )
state.empty = set( [('rover3store',), ('rover0store',), ('rover1store',), ('rover2store',), ] )
rigid.equipped_for_imaging = set( [('rover1',), ('rover3',), ('rover0',), ('rover2',), ] )
rigid.can_traverse = set( [('rover2', 'waypoint5', 'waypoint1'), ('rover0', 'waypoint5', 'waypoint0'), ('rover1', 'waypoint1', 'waypoint2'), ('rover1', 'waypoint5', 'waypoint2'), ('rover2', 'waypoint2', 'waypoint1'), ('rover3', 'waypoint6', 'waypoint2'), ('rover3', 'waypoint0', 'waypoint2'), ('rover3', 'waypoint5', 'waypoint0'), ('rover2', 'waypoint3', 'waypoint0'), ('rover3', 'waypoint2', 'waypoint0'), ('rover1', 'waypoint1', 'waypoint3'), ('rover3', 'waypoint3', 'waypoint0'), ('rover2', 'waypoint0', 'waypoint1'), ('rover0', 'waypoint1', 'waypoint5'), ('rover3', 'waypoint4', 'waypoint1'), ('rover1', 'waypoint1', 'waypoint4'), ('rover3', 'waypoint0', 'waypoint3'), ('rover0', 'waypoint2', 'waypoint5'), ('rover1', 'waypoint2', 'waypoint0'), ('rover0', 'waypoint4', 'waypoint1'), ('rover0', 'waypoint5', 'waypoint1'), ('rover2', 'waypoint0', 'waypoint6'), ('rover1', 'waypoint0', 'waypoint2'), ('rover1', 'waypoint6', 'waypoint2'), ('rover0', 'waypoint0', 'waypoint5'), ('rover3', 'waypoint2', 'waypoint1'), ('rover0', 'waypoint5', 'waypoint6'), ('rover2', 'waypoint4', 'waypoint3'), ('rover2', 'waypoint1', 'waypoint2'), ('rover3', 'waypoint0', 'waypoint5'), ('rover1', 'waypoint2', 'waypoint5'), ('rover0', 'waypoint6', 'waypoint5'), ('rover3', 'waypoint2', 'waypoint6'), ('rover0', 'waypoint3', 'waypoint1'), ('rover1', 'waypoint4', 'waypoint1'), ('rover1', 'waypoint2', 'waypoint1'), ('rover3', 'waypoint1', 'waypoint4'), ('rover2', 'waypoint1', 'waypoint0'), ('rover3', 'waypoint1', 'waypoint2'), ('rover1', 'waypoint2', 'waypoint6'), ('rover2', 'waypoint0', 'waypoint3'), ('rover0', 'waypoint5', 'waypoint2'), ('rover1', 'waypoint3', 'waypoint1'), ('rover2', 'waypoint3', 'waypoint4'), ('rover2', 'waypoint1', 'waypoint5'), ('rover0', 'waypoint1', 'waypoint3'), ('rover0', 'waypoint1', 'waypoint4'), ('rover2', 'waypoint6', 'waypoint0'), ] )
rigid.equipped_for_rock_analysis = set( [('rover1',), ] )
rigid.equipped_for_soil_analysis = set( [('rover3',), ('rover2',), ] )
rigid.on_board = set( [('camera0', 'rover3'), ('camera2', 'rover0'), ('camera1', 'rover0'), ('camera4', 'rover1'), ('camera3', 'rover2'), ] )
rigid.calibration_target = set( [('camera0', 'objective2'), ('camera2', 'objective0'), ('camera3', 'objective0'), ('camera4', 'objective1'), ('camera1', 'objective2'), ] )
rigid.supports = set( [('camera0', 'colour'), ('camera2', 'low_res'), ('camera3', 'low_res'), ('camera4', 'low_res'), ('camera3', 'high_res'), ('camera3', 'colour'), ('camera4', 'colour'), ('camera1', 'colour'), ('camera0', 'low_res'), ] )
rigid.visible_from = set( [('objective0', 'waypoint0'), ('objective1', 'waypoint0'), ('objective1', 'waypoint5'), ('objective2', 'waypoint3'), ('objective1', 'waypoint4'), ('objective2', 'waypoint4'), ('objective0', 'waypoint2'), ('objective0', 'waypoint1'), ('objective2', 'waypoint6'), ('objective1', 'waypoint2'), ('objective1', 'waypoint1'), ('objective2', 'waypoint0'), ('objective2', 'waypoint5'), ('objective2', 'waypoint2'), ('objective2', 'waypoint1'), ('objective1', 'waypoint3'), ] )
rigid.goal_communicated_soil_data = set( [('waypoint0',), ('waypoint6',), ('waypoint4',), ] )
rigid.goal_communicated_rock_data = set( [('waypoint0',), ('waypoint6',), ('waypoint3',), ] )
rigid.goal_communicated_image_data = set( [('objective2', 'colour'), ('objective2', 'low_res'), ] )
state.calibrated = set( [] )
state.have_image = set( [] )
state.communicated_rock_data = set( [] )
state.have_soil_analysis = set( [] )
state.communicated_image_data = set( [] )
state.have_rock_analysis = set( [] )
state.full = set( [] )
state.communicated_soil_data = set( [] )

task_list = [('achieve__goals',)]