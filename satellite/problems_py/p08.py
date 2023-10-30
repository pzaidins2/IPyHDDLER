from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'star3', 'satellite3', 'instrument8', 'planet11', 'groundstation1', 'thermograph2', 'phenomenon14', 'instrument6', 'thermograph1', 'instrument9', 'instrument2', 'instrument4', 'instrument5', 'satellite0', 'star4', 'star10', 'star0', 'satellite2', 'instrument3', 'image0', 'instrument1', 'star2', 'phenomenon12', 'spectrograph3', 'phenomenon5', 'star6', 'instrument7', 'instrument0', 'phenomenon9', 'phenomenon8', 'satellite1', 'star7', 'phenomenon13'}
rigid.mode = {'thermograph1', 'image0', 'thermograph2', 'spectrograph3'}
rigid.instrument = {'instrument8', 'instrument3', 'instrument1', 'instrument9', 'instrument2', 'instrument4', 'instrument5', 'instrument7', 'instrument0', 'instrument6'}
rigid.direction = {'planet11', 'groundstation1', 'phenomenon14', 'star10', 'star2', 'phenomenon12', 'phenomenon5', 'star6', 'star4', 'phenomenon9', 'star0', 'phenomenon8', 'star7', 'star3', 'phenomenon13'}
rigid.satellite = {'satellite2', 'satellite3', 'satellite0', 'satellite1'}
rigid.supports = set( [('instrument1', 'thermograph1'), ('instrument1', 'spectrograph3'), ('instrument3', 'image0'), ('instrument6', 'thermograph1'), ('instrument1', 'thermograph2'), ('instrument6', 'thermograph2'), ('instrument7', 'image0'), ('instrument4', 'thermograph1'), ('instrument3', 'thermograph2'), ('instrument7', 'thermograph1'), ('instrument7', 'thermograph2'), ('instrument0', 'image0'), ('instrument9', 'image0'), ('instrument5', 'spectrograph3'), ('instrument5', 'thermograph1'), ('instrument0', 'thermograph1'), ('instrument9', 'spectrograph3'), ('instrument9', 'thermograph1'), ('instrument2', 'spectrograph3'), ('instrument8', 'image0'), ('instrument5', 'thermograph2'), ] )
rigid.calibration_target = set( [('instrument6', 'star3'), ('instrument9', 'star4'), ('instrument7', 'star0'), ('instrument2', 'star4'), ('instrument8', 'star3'), ('instrument1', 'star2'), ('instrument5', 'star0'), ('instrument0', 'star3'), ('instrument3', 'groundstation1'), ('instrument4', 'star4'), ] )
rigid.on_board = set( [('instrument8', 'satellite3'), ('instrument9', 'satellite3'), ('instrument6', 'satellite2'), ('instrument4', 'satellite1'), ('instrument0', 'satellite0'), ('instrument7', 'satellite2'), ('instrument2', 'satellite0'), ('instrument3', 'satellite1'), ('instrument1', 'satellite0'), ('instrument5', 'satellite1'), ] )
state.power_avail = set( [('satellite2',), ('satellite3',), ('satellite1',), ('satellite0',), ] )
state.pointing = set( [('satellite3', 'phenomenon5'), ('satellite1', 'star4'), ('satellite0', 'phenomenon14'), ('satellite2', 'star6'), ] )
rigid.goal_have_image = set( [('phenomenon12', 'image0'), ('star7', 'spectrograph3'), ('star6', 'thermograph1'), ('phenomenon14', 'thermograph2'), ('planet11', 'thermograph2'), ('phenomenon13', 'thermograph1'), ('phenomenon8', 'image0'), ('star10', 'spectrograph3'), ('phenomenon5', 'thermograph1'), ('phenomenon9', 'image0'), ] )
state.power_on = set( [] )
state.calibrated = set( [] )
state.have_image = set( [] )
rigid.goal_pointing = set( [] )

task_list = [('main',)]
