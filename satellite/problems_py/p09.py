from ipyhop import State

from ordered_set import OrderedSet

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = OrderedSet(['instrument0', 'instrument1', 'instrument2', 'instrument3', 'instrument4', 'instrument5', 'instrument6', 'instrument7', 'instrument8', 'instrument9', 'instrument10', 'satellite0', 'satellite1', 'satellite2', 'satellite3', 'satellite4', 'star4', 'star3', 'groundstation1', 'star0', 'star2', 'planet5', 'phenomenon6', 'phenomenon7', 'phenomenon8', 'star9', 'planet10', 'planet11', 'phenomenon12', 'phenomenon13', 'star14', 'spectrograph0', 'image3', 'image4', 'infrared1', 'image2'])
rigid.satellite = OrderedSet(['satellite0', 'satellite1', 'satellite2', 'satellite3', 'satellite4'])
rigid.direction = OrderedSet(['star4', 'star3', 'groundstation1', 'star0', 'star2', 'planet5', 'phenomenon6', 'phenomenon7', 'phenomenon8', 'star9', 'planet10', 'planet11', 'phenomenon12', 'phenomenon13', 'star14'])
rigid.instrument = OrderedSet(['instrument0', 'instrument1', 'instrument2', 'instrument3', 'instrument4', 'instrument5', 'instrument6', 'instrument7', 'instrument8', 'instrument9', 'instrument10'])
rigid.mode = OrderedSet(['spectrograph0', 'image3', 'image4', 'infrared1', 'image2'])
rigid.supports = OrderedSet( [('instrument0', 'infrared1'), ('instrument0', 'image4'), ('instrument1', 'image4'), ('instrument1', 'image2'), ('instrument1', 'spectrograph0'), ('instrument2', 'image2'), ('instrument3', 'image2'), ('instrument3', 'image3'), ('instrument3', 'image4'), ('instrument4', 'image3'), ('instrument4', 'image2'), ('instrument5', 'image4'), ('instrument5', 'infrared1'), ('instrument5', 'spectrograph0'), ('instrument6', 'image2'), ('instrument6', 'spectrograph0'), ('instrument7', 'image3'), ('instrument7', 'spectrograph0'), ('instrument7', 'image4'), ('instrument8', 'image4'), ('instrument8', 'infrared1'), ('instrument8', 'image3'), ('instrument9', 'image4'), ('instrument10', 'image2'), ('instrument10', 'infrared1'), ('instrument10', 'image4'), ] )
rigid.calibration_target = OrderedSet( [('instrument0', 'star3'), ('instrument1', 'star4'), ('instrument2', 'star2'), ('instrument3', 'star2'), ('instrument4', 'star3'), ('instrument5', 'star3'), ('instrument6', 'star2'), ('instrument7', 'star0'), ('instrument8', 'groundstation1'), ('instrument9', 'star0'), ('instrument10', 'star2'), ] )
rigid.on_board = OrderedSet( [('instrument0', 'satellite0'), ('instrument1', 'satellite0'), ('instrument2', 'satellite0'), ('instrument3', 'satellite1'), ('instrument4', 'satellite1'), ('instrument5', 'satellite1'), ('instrument6', 'satellite2'), ('instrument7', 'satellite3'), ('instrument8', 'satellite4'), ('instrument9', 'satellite4'), ('instrument10', 'satellite4'), ] )
state.power_avail = OrderedSet( [('satellite0',), ('satellite1',), ('satellite2',), ('satellite3',), ('satellite4',), ] )
state.pointing = OrderedSet( [('satellite0', 'star0'), ('satellite1', 'planet11'), ('satellite2', 'phenomenon6'), ('satellite3', 'planet10'), ('satellite4', 'star9'), ] )
rigid.goal_pointing = OrderedSet( [('satellite0', 'phenomenon7'), ('satellite3', 'star9'), ('satellite4', 'planet5'), ] )
rigid.goal_have_image = OrderedSet( [('planet5', 'image2'), ('phenomenon6', 'image3'), ('phenomenon7', 'infrared1'), ('phenomenon8', 'image2'), ('star9', 'image3'), ('planet10', 'image4'), ('planet11', 'spectrograph0'), ('phenomenon12', 'image3'), ('phenomenon13', 'spectrograph0'), ('star14', 'image4'), ] )
state.power_on = OrderedSet( [] )
state.calibrated = OrderedSet( [] )
state.have_image = OrderedSet( [] )

task_list = [('main',)]
