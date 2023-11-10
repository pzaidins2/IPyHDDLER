from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'star3', 'star7', 'satellite1', 'instrument9', 'star4', 'instrument5', 'satellite3', 'phenomenon8', 'satellite2', 'planet11', 'spectrograph3', 'instrument8', 'thermograph2', 'groundstation1', 'phenomenon12', 'star6', 'star10', 'phenomenon13', 'phenomenon5', 'satellite0', 'instrument6', 'instrument4', 'image0', 'thermograph1', 'star2', 'instrument0', 'phenomenon9', 'phenomenon14', 'instrument7', 'instrument3', 'instrument2', 'instrument1', 'star0'}
rigid.mode = {'thermograph1', 'thermograph2', 'spectrograph3', 'image0'}
rigid.satellite = {'satellite1', 'satellite0', 'satellite3', 'satellite2'}
rigid.direction = {'star3', 'star7', 'star4', 'phenomenon8', 'star2', 'planet11', 'phenomenon9', 'groundstation1', 'phenomenon12', 'star6', 'phenomenon14', 'star10', 'phenomenon13', 'phenomenon5', 'star0'}
rigid.instrument = {'instrument9', 'instrument5', 'instrument0', 'instrument8', 'instrument6', 'instrument7', 'instrument3', 'instrument4', 'instrument2', 'instrument1'}
rigid.supports = set( [('instrument5', 'spectrograph3'), ('instrument9', 'thermograph1'), ('instrument9', 'spectrograph3'), ('instrument3', 'image0'), ('instrument8', 'image0'), ('instrument6', 'thermograph1'), ('instrument0', 'image0'), ('instrument6', 'thermograph2'), ('instrument2', 'spectrograph3'), ('instrument3', 'thermograph2'), ('instrument7', 'image0'), ('instrument0', 'thermograph1'), ('instrument7', 'thermograph1'), ('instrument7', 'thermograph2'), ('instrument1', 'thermograph1'), ('instrument1', 'thermograph2'), ('instrument5', 'thermograph1'), ('instrument9', 'image0'), ('instrument4', 'thermograph1'), ('instrument5', 'thermograph2'), ('instrument1', 'spectrograph3'), ] )
rigid.calibration_target = set( [('instrument8', 'star3'), ('instrument2', 'star4'), ('instrument7', 'star0'), ('instrument1', 'star2'), ('instrument9', 'star4'), ('instrument3', 'groundstation1'), ('instrument0', 'star3'), ('instrument6', 'star3'), ('instrument5', 'star0'), ('instrument4', 'star4'), ] )
rigid.on_board = set( [('instrument0', 'satellite0'), ('instrument4', 'satellite1'), ('instrument1', 'satellite0'), ('instrument3', 'satellite1'), ('instrument2', 'satellite0'), ('instrument8', 'satellite3'), ('instrument9', 'satellite3'), ('instrument5', 'satellite1'), ('instrument7', 'satellite2'), ('instrument6', 'satellite2'), ] )
state.power_avail = set( [('satellite3',), ('satellite1',), ('satellite2',), ('satellite0',), ] )
state.pointing = set( [('satellite1', 'star4'), ('satellite0', 'phenomenon14'), ('satellite3', 'phenomenon5'), ('satellite2', 'star6'), ] )
rigid.goal_have_image = set( [('phenomenon12', 'image0'), ('star10', 'spectrograph3'), ('star6', 'thermograph1'), ('phenomenon14', 'thermograph2'), ('phenomenon13', 'thermograph1'), ('phenomenon9', 'image0'), ('phenomenon5', 'thermograph1'), ('phenomenon8', 'image0'), ('planet11', 'thermograph2'), ('star7', 'spectrograph3'), ] )
state.power_on = set( [] )
state.have_image = set( [] )
state.calibrated = set( [] )
rigid.goal_pointing = set( [] )

task_list = [('main',)]
