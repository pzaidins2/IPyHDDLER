from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'star2', 'satellite0', 'infrared3', 'star1', 'instrument2', 'star7', 'star10', 'planet4', 'instrument3', 'groundstation3', 'star6', 'phenomenon8', 'instrument1', 'star0', 'planet5', 'satellite2', 'instrument0', 'star9', 'satellite1', 'infrared1', 'instrument4', 'thermograph2', 'spectrograph0'}
rigid.direction = {'star2', 'star6', 'phenomenon8', 'star1', 'star7', 'star0', 'planet5', 'star9', 'star10', 'planet4', 'groundstation3'}
rigid.mode = {'thermograph2', 'spectrograph0', 'infrared1', 'infrared3'}
rigid.instrument = {'instrument4', 'instrument1', 'instrument2', 'instrument3', 'instrument0'}
rigid.satellite = {'satellite2', 'satellite0', 'satellite1'}
rigid.supports = set( [('instrument3', 'infrared1'), ('instrument4', 'infrared3'), ('instrument3', 'spectrograph0'), ('instrument0', 'infrared1'), ('instrument2', 'thermograph2'), ('instrument2', 'infrared3'), ('instrument2', 'infrared1'), ('instrument1', 'infrared3'), ('instrument3', 'infrared3'), ('instrument0', 'spectrograph0'), ] )
rigid.calibration_target = set( [('instrument0', 'star1'), ('instrument2', 'star2'), ('instrument3', 'star2'), ('instrument1', 'star2'), ('instrument4', 'star0'), ] )
rigid.on_board = set( [('instrument1', 'satellite1'), ('instrument0', 'satellite0'), ('instrument4', 'satellite2'), ('instrument2', 'satellite1'), ('instrument3', 'satellite1'), ] )
state.power_avail = set( [('satellite1',), ('satellite0',), ('satellite2',), ] )
state.pointing = set( [('satellite2', 'star6'), ('satellite1', 'star6'), ('satellite0', 'phenomenon8'), ] )
rigid.goal_have_image = set( [('phenomenon8', 'spectrograph0'), ('star7', 'infrared3'), ('planet4', 'thermograph2'), ('star6', 'thermograph2'), ('planet5', 'spectrograph0'), ('star9', 'infrared1'), ('star10', 'infrared3'), ] )
state.calibrated = set( [] )
state.have_image = set( [] )
state.power_on = set( [] )
rigid.goal_pointing = set( [] )

task_list = [('main',)]
