from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'star4', 'instrument0', 'infrared0', 'phenomenon5', 'instrument2', 'image1', 'star2', 'star3', 'satellite1', 'satellite0', 'instrument3', 'star0', 'instrument1', 'star1', 'phenomenon6', 'phenomenon7', 'spectrograph2'}
rigid.satellite = {'satellite1', 'satellite0'}
rigid.instrument = {'instrument0', 'instrument3', 'instrument2', 'instrument1'}
rigid.mode = {'infrared0', 'spectrograph2', 'image1'}
rigid.direction = {'star4', 'phenomenon5', 'star2', 'star3', 'star0', 'star1', 'phenomenon6', 'phenomenon7'}
rigid.supports = set( [('instrument0', 'infrared0'), ('instrument1', 'image1'), ('instrument3', 'spectrograph2'), ('instrument3', 'image1'), ('instrument0', 'spectrograph2'), ('instrument3', 'infrared0'), ('instrument2', 'image1'), ('instrument2', 'infrared0'), ] )
rigid.calibration_target = set( [('instrument2', 'star0'), ('instrument3', 'star0'), ('instrument1', 'star2'), ('instrument0', 'star1'), ] )
rigid.on_board = set( [('instrument0', 'satellite0'), ('instrument1', 'satellite0'), ('instrument2', 'satellite0'), ('instrument3', 'satellite1'), ] )
state.power_avail = set( [('satellite0',), ('satellite1',), ] )
state.pointing = set( [('satellite0', 'star4'), ('satellite1', 'star0'), ] )
rigid.goal_pointing = set( [('satellite0', 'phenomenon5'), ] )
rigid.goal_have_image = set( [('star4', 'spectrograph2'), ('phenomenon7', 'spectrograph2'), ('star3', 'infrared0'), ('phenomenon5', 'spectrograph2'), ] )
state.calibrated = set( [] )
state.have_image = set( [] )
state.power_on = set( [] )

task_list = [('main',)]
