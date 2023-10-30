from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'phenomenon5', 'star3', 'satellite1', 'instrument3', 'spectrograph2', 'phenomenon7', 'star1', 'satellite0', 'instrument0', 'image1', 'phenomenon6', 'instrument2', 'infrared0', 'star4', 'star0', 'instrument1', 'star2'}
rigid.mode = {'image1', 'spectrograph2', 'infrared0'}
rigid.satellite = {'satellite1', 'satellite0'}
rigid.instrument = {'instrument2', 'instrument1', 'instrument3', 'instrument0'}
rigid.direction = {'phenomenon5', 'star3', 'phenomenon7', 'star1', 'phenomenon6', 'star4', 'star0', 'star2'}
rigid.supports = set( [('instrument0', 'infrared0'), ('instrument3', 'spectrograph2'), ('instrument2', 'infrared0'), ('instrument2', 'image1'), ('instrument1', 'image1'), ('instrument3', 'image1'), ('instrument3', 'infrared0'), ('instrument0', 'spectrograph2'), ] )
rigid.calibration_target = set( [('instrument1', 'star2'), ('instrument0', 'star1'), ('instrument2', 'star0'), ('instrument3', 'star0'), ] )
rigid.on_board = set( [('instrument2', 'satellite0'), ('instrument1', 'satellite0'), ('instrument0', 'satellite0'), ('instrument3', 'satellite1'), ] )
state.power_avail = set( [('satellite0',), ('satellite1',), ] )
state.pointing = set( [('satellite0', 'star4'), ('satellite1', 'star0'), ] )
rigid.goal_pointing = set( [('satellite0', 'phenomenon5'), ] )
rigid.goal_have_image = set( [('star3', 'infrared0'), ('phenomenon5', 'spectrograph2'), ('star4', 'spectrograph2'), ('phenomenon7', 'spectrograph2'), ] )
state.have_image = set( [] )
state.calibrated = set( [] )
state.power_on = set( [] )

task_list = [('main',)]
