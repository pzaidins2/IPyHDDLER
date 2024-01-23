from ipyhop import State

from ordered_set import OrderedSet

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = OrderedSet(['instrument0', 'instrument1', 'instrument2', 'instrument3', 'instrument4', 'satellite0', 'satellite1', 'satellite2', 'groundstation3', 'star1', 'star2', 'star0', 'planet4', 'planet5', 'star6', 'star7', 'phenomenon8', 'star9', 'star10', 'thermograph2', 'spectrograph0', 'infrared1', 'infrared3'])
rigid.satellite = OrderedSet(['satellite0', 'satellite1', 'satellite2'])
rigid.direction = OrderedSet(['groundstation3', 'star1', 'star2', 'star0', 'planet4', 'planet5', 'star6', 'star7', 'phenomenon8', 'star9', 'star10'])
rigid.instrument = OrderedSet(['instrument0', 'instrument1', 'instrument2', 'instrument3', 'instrument4'])
rigid.mode = OrderedSet(['thermograph2', 'spectrograph0', 'infrared1', 'infrared3'])
rigid.supports = OrderedSet( [('instrument0', 'infrared1'), ('instrument0', 'spectrograph0'), ('instrument1', 'infrared3'), ('instrument2', 'infrared1'), ('instrument2', 'infrared3'), ('instrument2', 'thermograph2'), ('instrument3', 'infrared1'), ('instrument3', 'infrared3'), ('instrument3', 'spectrograph0'), ('instrument4', 'infrared3'), ] )
rigid.calibration_target = OrderedSet( [('instrument0', 'star1'), ('instrument1', 'star2'), ('instrument2', 'star2'), ('instrument3', 'star2'), ('instrument4', 'star0'), ] )
rigid.on_board = OrderedSet( [('instrument0', 'satellite0'), ('instrument1', 'satellite1'), ('instrument2', 'satellite1'), ('instrument3', 'satellite1'), ('instrument4', 'satellite2'), ] )
state.power_avail = OrderedSet( [('satellite0',), ('satellite1',), ('satellite2',), ] )
state.pointing = OrderedSet( [('satellite0', 'phenomenon8'), ('satellite1', 'star6'), ('satellite2', 'star6'), ] )
rigid.goal_have_image = OrderedSet( [('planet4', 'thermograph2'), ('planet5', 'spectrograph0'), ('star6', 'thermograph2'), ('star7', 'infrared3'), ('phenomenon8', 'spectrograph0'), ('star9', 'infrared1'), ('star10', 'infrared3'), ] )
state.power_on = OrderedSet( [] )
state.calibrated = OrderedSet( [] )
state.have_image = OrderedSet( [] )
rigid.goal_pointing = OrderedSet( [] )

task_list = [('main',)]
