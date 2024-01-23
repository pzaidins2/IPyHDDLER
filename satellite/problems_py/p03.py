from ipyhop import State

from ordered_set import OrderedSet

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = OrderedSet(['instrument0', 'instrument1', 'instrument2', 'instrument3', 'satellite0', 'satellite1', 'star1', 'star2', 'star0', 'star3', 'star4', 'phenomenon5', 'phenomenon6', 'phenomenon7', 'image1', 'infrared0', 'spectrograph2'])
rigid.satellite = OrderedSet(['satellite0', 'satellite1'])
rigid.direction = OrderedSet(['star1', 'star2', 'star0', 'star3', 'star4', 'phenomenon5', 'phenomenon6', 'phenomenon7'])
rigid.instrument = OrderedSet(['instrument0', 'instrument1', 'instrument2', 'instrument3'])
rigid.mode = OrderedSet(['image1', 'infrared0', 'spectrograph2'])
rigid.supports = OrderedSet( [('instrument0', 'spectrograph2'), ('instrument0', 'infrared0'), ('instrument1', 'image1'), ('instrument2', 'infrared0'), ('instrument2', 'image1'), ('instrument3', 'spectrograph2'), ('instrument3', 'infrared0'), ('instrument3', 'image1'), ] )
rigid.calibration_target = OrderedSet( [('instrument0', 'star1'), ('instrument1', 'star2'), ('instrument2', 'star0'), ('instrument3', 'star0'), ] )
rigid.on_board = OrderedSet( [('instrument0', 'satellite0'), ('instrument1', 'satellite0'), ('instrument2', 'satellite0'), ('instrument3', 'satellite1'), ] )
state.power_avail = OrderedSet( [('satellite0',), ('satellite1',), ] )
state.pointing = OrderedSet( [('satellite0', 'star4'), ('satellite1', 'star0'), ] )
rigid.goal_pointing = OrderedSet( [('satellite0', 'phenomenon5'), ] )
rigid.goal_have_image = OrderedSet( [('star3', 'infrared0'), ('star4', 'spectrograph2'), ('phenomenon5', 'spectrograph2'), ('phenomenon7', 'spectrograph2'), ] )
state.power_on = OrderedSet( [] )
state.calibrated = OrderedSet( [] )
state.have_image = OrderedSet( [] )

task_list = [('main',)]
