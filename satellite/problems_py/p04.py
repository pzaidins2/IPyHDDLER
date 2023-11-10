from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'star7', 'satellite0', 'instrument0', 'star6', 'satellite1', 'infrared0', 'instrument2', 'star0', 'star4', 'groundstation1', 'phenomenon8', 'star2', 'infrared1', 'planet5', 'planet3', 'phenomenon9', 'thermograph2', 'instrument1'}
rigid.instrument = {'instrument0', 'instrument1', 'instrument2'}
rigid.direction = {'star0', 'star4', 'groundstation1', 'phenomenon8', 'star7', 'star2', 'planet5', 'planet3', 'star6', 'phenomenon9'}
rigid.mode = {'thermograph2', 'infrared0', 'infrared1'}
rigid.satellite = {'satellite0', 'satellite1'}
rigid.supports = set( [('instrument1', 'thermograph2'), ('instrument2', 'thermograph2'), ('instrument0', 'thermograph2'), ('instrument1', 'infrared0'), ('instrument0', 'infrared0'), ('instrument1', 'infrared1'), ('instrument2', 'infrared1'), ] )
rigid.calibration_target = set( [('instrument2', 'star2'), ('instrument0', 'star0'), ('instrument1', 'star2'), ] )
rigid.on_board = set( [('instrument1', 'satellite1'), ('instrument2', 'satellite1'), ('instrument0', 'satellite0'), ] )
state.power_avail = set( [('satellite0',), ('satellite1',), ] )
state.pointing = set( [('satellite0', 'star6'), ('satellite1', 'star0'), ] )
rigid.goal_pointing = set( [('satellite1', 'planet5'), ] )
rigid.goal_have_image = set( [('phenomenon8', 'thermograph2'), ('planet5', 'thermograph2'), ('planet3', 'infrared1'), ('star6', 'infrared1'), ('star7', 'infrared0'), ('phenomenon9', 'infrared0'), ('star4', 'infrared1'), ] )
state.power_on = set( [] )
state.have_image = set( [] )
state.calibrated = set( [] )

task_list = [('main',)]
