from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'star0', 'star10', 'planet5', 'instrument0', 'star2', 'thermograph2', 'infrared1', 'satellite0', 'star9', 'star7', 'star1', 'phenomenon8', 'instrument1', 'instrument2', 'satellite2', 'instrument3', 'instrument4', 'planet4', 'spectrograph0', 'infrared3', 'groundstation3', 'satellite1', 'star6'}
rigid.mode = {'infrared1', 'spectrograph0', 'infrared3', 'thermograph2'}
rigid.instrument = {'instrument4', 'instrument1', 'instrument2', 'instrument0', 'instrument3'}
rigid.satellite = {'satellite1', 'satellite0', 'satellite2'}
rigid.direction = {'star9', 'star1', 'star0', 'phenomenon8', 'star10', 'planet5', 'star2', 'planet4', 'groundstation3', 'star7', 'star6'}
rigid.supports = set( [('instrument2', 'infrared1'), ('instrument1', 'infrared3'), ('instrument4', 'infrared3'), ('instrument2', 'infrared3'), ('instrument0', 'spectrograph0'), ('instrument2', 'thermograph2'), ('instrument3', 'infrared1'), ('instrument3', 'spectrograph0'), ('instrument3', 'infrared3'), ('instrument0', 'infrared1'), ] )
rigid.calibration_target = set( [('instrument2', 'star2'), ('instrument0', 'star1'), ('instrument3', 'star2'), ('instrument4', 'star0'), ('instrument1', 'star2'), ] )
rigid.on_board = set( [('instrument4', 'satellite2'), ('instrument1', 'satellite1'), ('instrument0', 'satellite0'), ('instrument2', 'satellite1'), ('instrument3', 'satellite1'), ] )
state.power_avail = set( [('satellite2',), ('satellite0',), ('satellite1',), ] )
state.pointing = set( [('satellite1', 'star6'), ('satellite0', 'phenomenon8'), ('satellite2', 'star6'), ] )
rigid.goal_have_image = set( [('star6', 'thermograph2'), ('phenomenon8', 'spectrograph0'), ('star7', 'infrared3'), ('star9', 'infrared1'), ('planet5', 'spectrograph0'), ('star10', 'infrared3'), ('planet4', 'thermograph2'), ] )
rigid.goal_pointing = set( [] )
state.power_on = set( [] )
state.calibrated = set( [] )
state.have_image = set( [] )

task_list = [('main',)]
