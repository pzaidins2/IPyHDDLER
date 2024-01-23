from ipyhop import State

from ordered_set import OrderedSet

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = OrderedSet(['instrument0', 'instrument1', 'satellite0', 'groundstation1', 'star0', 'groundstation2', 'planet3', 'planet4', 'phenomenon5', 'phenomenon6', 'star7', 'infrared0', 'infrared1', 'image2'])
rigid.satellite = OrderedSet(['satellite0'])
rigid.direction = OrderedSet(['groundstation1', 'star0', 'groundstation2', 'planet3', 'planet4', 'phenomenon5', 'phenomenon6', 'star7'])
rigid.instrument = OrderedSet(['instrument0', 'instrument1'])
rigid.mode = OrderedSet(['infrared0', 'infrared1', 'image2'])
rigid.supports = OrderedSet( [('instrument0', 'infrared1'), ('instrument0', 'infrared0'), ('instrument1', 'image2'), ('instrument1', 'infrared1'), ('instrument1', 'infrared0'), ] )
rigid.calibration_target = OrderedSet( [('instrument0', 'star0'), ('instrument1', 'groundstation2'), ] )
rigid.on_board = OrderedSet( [('instrument0', 'satellite0'), ('instrument1', 'satellite0'), ] )
state.power_avail = OrderedSet( [('satellite0',), ] )
state.pointing = OrderedSet( [('satellite0', 'planet4'), ] )
rigid.goal_have_image = OrderedSet( [('planet3', 'infrared0'), ('planet4', 'infrared0'), ('phenomenon5', 'image2'), ('phenomenon6', 'infrared0'), ('star7', 'infrared0'), ] )
state.power_on = OrderedSet( [] )
state.calibrated = OrderedSet( [] )
state.have_image = OrderedSet( [] )
rigid.goal_pointing = OrderedSet( [] )

task_list = [('main',)]
