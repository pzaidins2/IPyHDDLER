from ipyhop import State

from ordered_set import OrderedSet

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = OrderedSet(['instrument0', 'instrument1', 'instrument2', 'instrument3', 'instrument4', 'instrument5', 'instrument6', 'instrument7', 'instrument8', 'instrument9', 'satellite0', 'satellite1', 'satellite2', 'satellite3', 'star2', 'groundstation1', 'star0', 'star3', 'star4', 'phenomenon5', 'star6', 'star7', 'phenomenon8', 'phenomenon9', 'star10', 'planet11', 'phenomenon12', 'phenomenon13', 'phenomenon14', 'thermograph2', 'image0', 'thermograph1', 'spectrograph3'])
rigid.satellite = OrderedSet(['satellite0', 'satellite1', 'satellite2', 'satellite3'])
rigid.direction = OrderedSet(['star2', 'groundstation1', 'star0', 'star3', 'star4', 'phenomenon5', 'star6', 'star7', 'phenomenon8', 'phenomenon9', 'star10', 'planet11', 'phenomenon12', 'phenomenon13', 'phenomenon14'])
rigid.instrument = OrderedSet(['instrument0', 'instrument1', 'instrument2', 'instrument3', 'instrument4', 'instrument5', 'instrument6', 'instrument7', 'instrument8', 'instrument9'])
rigid.mode = OrderedSet(['thermograph2', 'image0', 'thermograph1', 'spectrograph3'])
rigid.supports = OrderedSet( [('instrument0', 'thermograph1'), ('instrument0', 'image0'), ('instrument1', 'spectrograph3'), ('instrument1', 'thermograph2'), ('instrument1', 'thermograph1'), ('instrument2', 'spectrograph3'), ('instrument3', 'thermograph2'), ('instrument3', 'image0'), ('instrument4', 'thermograph1'), ('instrument5', 'thermograph2'), ('instrument5', 'thermograph1'), ('instrument5', 'spectrograph3'), ('instrument6', 'thermograph1'), ('instrument6', 'thermograph2'), ('instrument7', 'thermograph2'), ('instrument7', 'thermograph1'), ('instrument7', 'image0'), ('instrument8', 'image0'), ('instrument9', 'spectrograph3'), ('instrument9', 'thermograph1'), ('instrument9', 'image0'), ] )
rigid.calibration_target = OrderedSet( [('instrument0', 'star3'), ('instrument1', 'star2'), ('instrument2', 'star4'), ('instrument3', 'groundstation1'), ('instrument4', 'star4'), ('instrument5', 'star0'), ('instrument6', 'star3'), ('instrument7', 'star0'), ('instrument8', 'star3'), ('instrument9', 'star4'), ] )
rigid.on_board = OrderedSet( [('instrument0', 'satellite0'), ('instrument1', 'satellite0'), ('instrument2', 'satellite0'), ('instrument3', 'satellite1'), ('instrument4', 'satellite1'), ('instrument5', 'satellite1'), ('instrument6', 'satellite2'), ('instrument7', 'satellite2'), ('instrument8', 'satellite3'), ('instrument9', 'satellite3'), ] )
state.power_avail = OrderedSet( [('satellite0',), ('satellite1',), ('satellite2',), ('satellite3',), ] )
state.pointing = OrderedSet( [('satellite0', 'phenomenon14'), ('satellite1', 'star4'), ('satellite2', 'star6'), ('satellite3', 'phenomenon5'), ] )
rigid.goal_have_image = OrderedSet( [('phenomenon5', 'thermograph1'), ('star6', 'thermograph1'), ('star7', 'spectrograph3'), ('phenomenon8', 'image0'), ('phenomenon9', 'image0'), ('star10', 'spectrograph3'), ('planet11', 'thermograph2'), ('phenomenon12', 'image0'), ('phenomenon13', 'thermograph1'), ('phenomenon14', 'thermograph2'), ] )
state.power_on = OrderedSet( [] )
state.calibrated = OrderedSet( [] )
state.have_image = OrderedSet( [] )
rigid.goal_pointing = OrderedSet( [] )

task_list = [('main',)]
