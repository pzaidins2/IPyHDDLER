from ipyhop import State

from ordered_set import OrderedSet

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = OrderedSet(['instrument0', 'instrument1', 'instrument2', 'instrument3', 'instrument4', 'instrument5', 'instrument6', 'instrument7', 'instrument8', 'satellite0', 'satellite1', 'satellite2', 'groundstation2', 'groundstation1', 'groundstation0', 'star3', 'star4', 'phenomenon5', 'phenomenon6', 'star7', 'phenomenon8', 'planet9', 'thermograph0', 'image2', 'spectrograph1'])
rigid.satellite = OrderedSet(['satellite0', 'satellite1', 'satellite2'])
rigid.direction = OrderedSet(['groundstation2', 'groundstation1', 'groundstation0', 'star3', 'star4', 'phenomenon5', 'phenomenon6', 'star7', 'phenomenon8', 'planet9'])
rigid.instrument = OrderedSet(['instrument0', 'instrument1', 'instrument2', 'instrument3', 'instrument4', 'instrument5', 'instrument6', 'instrument7', 'instrument8'])
rigid.mode = OrderedSet(['thermograph0', 'image2', 'spectrograph1'])
rigid.supports = OrderedSet( [('instrument0', 'image2'), ('instrument0', 'thermograph0'), ('instrument0', 'spectrograph1'), ('instrument1', 'thermograph0'), ('instrument1', 'spectrograph1'), ('instrument1', 'image2'), ('instrument2', 'image2'), ('instrument3', 'spectrograph1'), ('instrument3', 'thermograph0'), ('instrument4', 'image2'), ('instrument4', 'spectrograph1'), ('instrument5', 'image2'), ('instrument5', 'spectrograph1'), ('instrument5', 'thermograph0'), ('instrument6', 'image2'), ('instrument7', 'image2'), ('instrument7', 'thermograph0'), ('instrument8', 'spectrograph1'), ('instrument8', 'image2'), ('instrument8', 'thermograph0'), ] )
rigid.calibration_target = OrderedSet( [('instrument0', 'groundstation2'), ('instrument1', 'groundstation1'), ('instrument2', 'groundstation0'), ('instrument3', 'groundstation0'), ('instrument4', 'groundstation2'), ('instrument5', 'groundstation1'), ('instrument6', 'groundstation1'), ('instrument7', 'groundstation1'), ('instrument8', 'groundstation0'), ] )
rigid.on_board = OrderedSet( [('instrument0', 'satellite0'), ('instrument1', 'satellite0'), ('instrument2', 'satellite0'), ('instrument3', 'satellite1'), ('instrument4', 'satellite1'), ('instrument5', 'satellite1'), ('instrument6', 'satellite2'), ('instrument7', 'satellite2'), ('instrument8', 'satellite2'), ] )
state.power_avail = OrderedSet( [('satellite0',), ('satellite1',), ('satellite2',), ] )
state.pointing = OrderedSet( [('satellite0', 'phenomenon8'), ('satellite1', 'groundstation2'), ('satellite2', 'phenomenon5'), ] )
rigid.goal_pointing = OrderedSet( [('satellite0', 'phenomenon5'), ('satellite1', 'groundstation2'), ] )
rigid.goal_have_image = OrderedSet( [('star3', 'thermograph0'), ('phenomenon5', 'image2'), ('phenomenon6', 'image2'), ('star7', 'thermograph0'), ('phenomenon8', 'image2'), ('planet9', 'spectrograph1'), ] )
state.power_on = OrderedSet( [] )
state.calibrated = OrderedSet( [] )
state.have_image = OrderedSet( [] )

task_list = [('main',)]
