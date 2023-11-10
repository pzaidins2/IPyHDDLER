from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'planet4', 'phenomenon5', 'image2', 'groundstation2', 'infrared1', 'groundstation1', 'star7', 'infrared0', 'planet3', 'instrument1', 'star0', 'satellite0', 'instrument0', 'phenomenon6'}
rigid.direction = {'planet4', 'phenomenon5', 'groundstation2', 'groundstation1', 'star7', 'planet3', 'star0', 'phenomenon6'}
rigid.satellite = {'satellite0'}
rigid.instrument = {'instrument0', 'instrument1'}
rigid.mode = {'image2', 'infrared0', 'infrared1'}
rigid.supports = set( [('instrument1', 'infrared0'), ('instrument1', 'image2'), ('instrument0', 'infrared0'), ('instrument1', 'infrared1'), ('instrument0', 'infrared1'), ] )
rigid.calibration_target = set( [('instrument1', 'groundstation2'), ('instrument0', 'star0'), ] )
rigid.on_board = set( [('instrument0', 'satellite0'), ('instrument1', 'satellite0'), ] )
state.power_avail = set( [('satellite0',), ] )
state.pointing = set( [('satellite0', 'planet4'), ] )
rigid.goal_have_image = set( [('star7', 'infrared0'), ('phenomenon6', 'infrared0'), ('phenomenon5', 'image2'), ('planet4', 'infrared0'), ('planet3', 'infrared0'), ] )
state.power_on = set( [] )
state.have_image = set( [] )
state.calibrated = set( [] )
rigid.goal_pointing = set( [] )

task_list = [('main',)]
