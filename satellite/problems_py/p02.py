from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'star0', 'star7', 'planet4', 'groundstation2', 'infrared0', 'groundstation1', 'phenomenon6', 'image2', 'instrument1', 'instrument0', 'infrared1', 'planet3', 'phenomenon5', 'satellite0'}
rigid.direction = {'star0', 'star7', 'planet4', 'groundstation2', 'groundstation1', 'phenomenon6', 'planet3', 'phenomenon5'}
rigid.mode = {'infrared0', 'image2', 'infrared1'}
rigid.satellite = {'satellite0'}
rigid.instrument = {'instrument0', 'instrument1'}
rigid.supports = set( [('instrument0', 'infrared0'), ('instrument1', 'infrared0'), ('instrument0', 'infrared1'), ('instrument1', 'infrared1'), ('instrument1', 'image2'), ] )
rigid.calibration_target = set( [('instrument1', 'groundstation2'), ('instrument0', 'star0'), ] )
rigid.on_board = set( [('instrument0', 'satellite0'), ('instrument1', 'satellite0'), ] )
state.power_avail = set( [('satellite0',), ] )
state.pointing = set( [('satellite0', 'planet4'), ] )
rigid.goal_have_image = set( [('phenomenon6', 'infrared0'), ('planet3', 'infrared0'), ('planet4', 'infrared0'), ('phenomenon5', 'image2'), ('star7', 'infrared0'), ] )
state.power_on = set( [] )
state.calibrated = set( [] )
rigid.goal_pointing = set( [] )
state.have_image = set( [] )

task_list = [('main',)]
