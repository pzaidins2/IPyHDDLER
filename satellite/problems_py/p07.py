from ipyhop import State

from ordered_set import OrderedSet

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = OrderedSet(['instrument0', 'instrument1', 'instrument2', 'instrument3', 'instrument4', 'instrument5', 'instrument6', 'instrument7', 'satellite0', 'satellite1', 'satellite2', 'satellite3', 'star3', 'groundstation2', 'star1', 'groundstation4', 'groundstation0', 'phenomenon5', 'star6', 'star7', 'planet8', 'planet9', 'planet10', 'planet11', 'image2', 'image1', 'image0', 'image3'])
rigid.satellite = OrderedSet(['satellite0', 'satellite1', 'satellite2', 'satellite3'])
rigid.direction = OrderedSet(['star3', 'groundstation2', 'star1', 'groundstation4', 'groundstation0', 'phenomenon5', 'star6', 'star7', 'planet8', 'planet9', 'planet10', 'planet11'])
rigid.instrument = OrderedSet(['instrument0', 'instrument1', 'instrument2', 'instrument3', 'instrument4', 'instrument5', 'instrument6', 'instrument7'])
rigid.mode = OrderedSet(['image2', 'image1', 'image0', 'image3'])
rigid.supports = OrderedSet( [('instrument0', 'image1'), ('instrument0', 'image3'), ('instrument1', 'image3'), ('instrument2', 'image0'), ('instrument3', 'image0'), ('instrument3', 'image2'), ('instrument4', 'image1'), ('instrument4', 'image0'), ('instrument5', 'image2'), ('instrument5', 'image0'), ('instrument5', 'image1'), ('instrument6', 'image2'), ('instrument6', 'image1'), ('instrument6', 'image0'), ('instrument7', 'image3'), ('instrument7', 'image0'), ('instrument7', 'image1'), ] )
rigid.calibration_target = OrderedSet( [('instrument0', 'star1'), ('instrument1', 'groundstation0'), ('instrument2', 'groundstation2'), ('instrument3', 'groundstation4'), ('instrument4', 'star1'), ('instrument5', 'star1'), ('instrument6', 'groundstation4'), ('instrument7', 'groundstation0'), ] )
rigid.on_board = OrderedSet( [('instrument0', 'satellite0'), ('instrument1', 'satellite0'), ('instrument2', 'satellite0'), ('instrument3', 'satellite1'), ('instrument4', 'satellite2'), ('instrument5', 'satellite2'), ('instrument6', 'satellite3'), ('instrument7', 'satellite3'), ] )
state.power_avail = OrderedSet( [('satellite0',), ('satellite1',), ('satellite2',), ('satellite3',), ] )
state.pointing = OrderedSet( [('satellite0', 'star6'), ('satellite1', 'groundstation0'), ('satellite2', 'star6'), ('satellite3', 'groundstation2'), ] )
rigid.goal_pointing = OrderedSet( [('satellite1', 'star1'), ('satellite2', 'phenomenon5'), ] )
rigid.goal_have_image = OrderedSet( [('phenomenon5', 'image0'), ('star6', 'image1'), ('star7', 'image0'), ('planet8', 'image0'), ('planet9', 'image3'), ('planet10', 'image0'), ('planet11', 'image2'), ] )
state.power_on = OrderedSet( [] )
state.calibrated = OrderedSet( [] )
state.have_image = OrderedSet( [] )

task_list = [('main',)]
