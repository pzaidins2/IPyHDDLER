from ipyhop import State

from ordered_set import OrderedSet

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = OrderedSet(['instrument0', 'instrument1', 'instrument2', 'instrument3', 'instrument4', 'instrument5', 'instrument6', 'instrument7', 'instrument8', 'instrument9', 'instrument10', 'satellite0', 'satellite1', 'satellite2', 'satellite3', 'satellite4', 'star1', 'groundstation3', 'star4', 'star2', 'star0', 'planet5', 'star6', 'star7', 'phenomenon8', 'planet9', 'planet10', 'star11', 'star12', 'phenomenon13', 'phenomenon14', 'star15', 'star16', 'infrared0', 'spectrograph1', 'infrared3', 'image4', 'image2'])
rigid.satellite = OrderedSet(['satellite0', 'satellite1', 'satellite2', 'satellite3', 'satellite4'])
rigid.direction = OrderedSet(['star1', 'groundstation3', 'star4', 'star2', 'star0', 'planet5', 'star6', 'star7', 'phenomenon8', 'planet9', 'planet10', 'star11', 'star12', 'phenomenon13', 'phenomenon14', 'star15', 'star16'])
rigid.instrument = OrderedSet(['instrument0', 'instrument1', 'instrument2', 'instrument3', 'instrument4', 'instrument5', 'instrument6', 'instrument7', 'instrument8', 'instrument9', 'instrument10'])
rigid.mode = OrderedSet(['infrared0', 'spectrograph1', 'infrared3', 'image4', 'image2'])
rigid.supports = OrderedSet( [('instrument0', 'image4'), ('instrument1', 'infrared0'), ('instrument1', 'spectrograph1'), ('instrument2', 'infrared0'), ('instrument2', 'image2'), ('instrument3', 'infrared3'), ('instrument3', 'infrared0'), ('instrument4', 'spectrograph1'), ('instrument4', 'image4'), ('instrument4', 'infrared0'), ('instrument5', 'image2'), ('instrument5', 'infrared0'), ('instrument5', 'infrared3'), ('instrument6', 'infrared0'), ('instrument6', 'infrared3'), ('instrument7', 'image4'), ('instrument7', 'spectrograph1'), ('instrument7', 'infrared3'), ('instrument8', 'spectrograph1'), ('instrument8', 'image4'), ('instrument9', 'infrared3'), ('instrument10', 'image2'), ('instrument10', 'image4'), ] )
rigid.calibration_target = OrderedSet( [('instrument0', 'star1'), ('instrument1', 'groundstation3'), ('instrument2', 'groundstation3'), ('instrument3', 'star4'), ('instrument4', 'star2'), ('instrument5', 'star0'), ('instrument6', 'groundstation3'), ('instrument7', 'star4'), ('instrument8', 'star4'), ('instrument9', 'star2'), ('instrument10', 'star0'), ] )
rigid.on_board = OrderedSet( [('instrument0', 'satellite0'), ('instrument1', 'satellite0'), ('instrument2', 'satellite1'), ('instrument3', 'satellite1'), ('instrument4', 'satellite2'), ('instrument5', 'satellite2'), ('instrument6', 'satellite3'), ('instrument7', 'satellite3'), ('instrument8', 'satellite4'), ('instrument9', 'satellite4'), ('instrument10', 'satellite4'), ] )
state.power_avail = OrderedSet( [('satellite0',), ('satellite1',), ('satellite2',), ('satellite3',), ('satellite4',), ] )
state.pointing = OrderedSet( [('satellite0', 'star0'), ('satellite1', 'star4'), ('satellite2', 'star1'), ('satellite3', 'groundstation3'), ('satellite4', 'planet10'), ] )
rigid.goal_pointing = OrderedSet( [('satellite4', 'planet9'), ] )
rigid.goal_have_image = OrderedSet( [('planet5', 'image4'), ('star6', 'infrared3'), ('star7', 'image4'), ('phenomenon8', 'image4'), ('planet9', 'infrared0'), ('planet10', 'infrared3'), ('star12', 'image4'), ('phenomenon13', 'image4'), ('phenomenon14', 'spectrograph1'), ('star15', 'spectrograph1'), ('star16', 'image2'), ] )
state.power_on = OrderedSet( [] )
state.calibrated = OrderedSet( [] )
state.have_image = OrderedSet( [] )

task_list = [('main',)]
