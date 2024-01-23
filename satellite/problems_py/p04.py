from ipyhop import State

from ordered_set import OrderedSet

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = OrderedSet(['instrument0', 'instrument1', 'instrument2', 'satellite0', 'satellite1', 'groundstation1', 'star0', 'star2', 'planet3', 'star4', 'planet5', 'star6', 'star7', 'phenomenon8', 'phenomenon9', 'infrared0', 'infrared1', 'thermograph2'])
rigid.satellite = OrderedSet(['satellite0', 'satellite1'])
rigid.direction = OrderedSet(['groundstation1', 'star0', 'star2', 'planet3', 'star4', 'planet5', 'star6', 'star7', 'phenomenon8', 'phenomenon9'])
rigid.instrument = OrderedSet(['instrument0', 'instrument1', 'instrument2'])
rigid.mode = OrderedSet(['infrared0', 'infrared1', 'thermograph2'])
rigid.supports = OrderedSet( [('instrument0', 'thermograph2'), ('instrument0', 'infrared0'), ('instrument1', 'infrared0'), ('instrument1', 'thermograph2'), ('instrument1', 'infrared1'), ('instrument2', 'thermograph2'), ('instrument2', 'infrared1'), ] )
rigid.calibration_target = OrderedSet( [('instrument0', 'star0'), ('instrument1', 'star2'), ('instrument2', 'star2'), ] )
rigid.on_board = OrderedSet( [('instrument0', 'satellite0'), ('instrument1', 'satellite1'), ('instrument2', 'satellite1'), ] )
state.power_avail = OrderedSet( [('satellite0',), ('satellite1',), ] )
state.pointing = OrderedSet( [('satellite0', 'star6'), ('satellite1', 'star0'), ] )
rigid.goal_pointing = OrderedSet( [('satellite1', 'planet5'), ] )
rigid.goal_have_image = OrderedSet( [('planet3', 'infrared1'), ('star4', 'infrared1'), ('planet5', 'thermograph2'), ('star6', 'infrared1'), ('star7', 'infrared0'), ('phenomenon8', 'thermograph2'), ('phenomenon9', 'infrared0'), ] )
state.power_on = OrderedSet( [] )
state.calibrated = OrderedSet( [] )
state.have_image = OrderedSet( [] )

task_list = [('main',)]
