from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'star4', 'star0', 'star7', 'phenomenon8', 'satellite0', 'infrared1', 'infrared0', 'instrument1', 'satellite1', 'planet5', 'star2', 'thermograph2', 'instrument2', 'groundstation1', 'star6', 'instrument0', 'phenomenon9', 'planet3'}
rigid.satellite = {'satellite0', 'satellite1'}
rigid.direction = {'star4', 'star0', 'star7', 'phenomenon8', 'planet5', 'star2', 'groundstation1', 'star6', 'phenomenon9', 'planet3'}
rigid.mode = {'thermograph2', 'infrared1', 'infrared0'}
rigid.instrument = {'instrument0', 'instrument2', 'instrument1'}
rigid.supports = set( [('instrument1', 'infrared0'), ('instrument0', 'infrared0'), ('instrument2', 'thermograph2'), ('instrument1', 'infrared1'), ('instrument0', 'thermograph2'), ('instrument2', 'infrared1'), ('instrument1', 'thermograph2'), ] )
rigid.calibration_target = set( [('instrument2', 'star2'), ('instrument1', 'star2'), ('instrument0', 'star0'), ] )
rigid.on_board = set( [('instrument1', 'satellite1'), ('instrument2', 'satellite1'), ('instrument0', 'satellite0'), ] )
state.power_avail = set( [('satellite1',), ('satellite0',), ] )
state.pointing = set( [('satellite0', 'star6'), ('satellite1', 'star0'), ] )
rigid.goal_pointing = set( [('satellite1', 'planet5'), ] )
rigid.goal_have_image = set( [('planet3', 'infrared1'), ('star4', 'infrared1'), ('star6', 'infrared1'), ('phenomenon9', 'infrared0'), ('planet5', 'thermograph2'), ('phenomenon8', 'thermograph2'), ('star7', 'infrared0'), ] )
state.calibrated = set( [] )
state.have_image = set( [] )
state.power_on = set( [] )

task_list = [('main',)]
