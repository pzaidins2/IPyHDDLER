from ipyhop import State

from ordered_set import OrderedSet

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = OrderedSet(['instrument0', 'instrument1', 'instrument2', 'instrument3', 'instrument4', 'instrument5', 'instrument6', 'instrument7', 'instrument8', 'instrument9', 'instrument10', 'instrument11', 'satellite0', 'satellite1', 'satellite2', 'satellite3', 'satellite4', 'satellite5', 'groundstation3', 'groundstation4', 'groundstation2', 'groundstation0', 'groundstation1', 'phenomenon5', 'phenomenon6', 'phenomenon7', 'planet8', 'star9', 'star10', 'phenomenon11', 'phenomenon12', 'phenomenon13', 'star14', 'planet15', 'planet16', 'planet17', 'phenomenon18', 'star19', 'star20', 'planet21', 'star22', 'planet23', 'star24', 'thermograph4', 'image1', 'thermograph3', 'image2', 'thermograph0'])
rigid.satellite = OrderedSet(['satellite0', 'satellite1', 'satellite2', 'satellite3', 'satellite4', 'satellite5'])
rigid.direction = OrderedSet(['groundstation3', 'groundstation4', 'groundstation2', 'groundstation0', 'groundstation1', 'phenomenon5', 'phenomenon6', 'phenomenon7', 'planet8', 'star9', 'star10', 'phenomenon11', 'phenomenon12', 'phenomenon13', 'star14', 'planet15', 'planet16', 'planet17', 'phenomenon18', 'star19', 'star20', 'planet21', 'star22', 'planet23', 'star24'])
rigid.instrument = OrderedSet(['instrument0', 'instrument1', 'instrument2', 'instrument3', 'instrument4', 'instrument5', 'instrument6', 'instrument7', 'instrument8', 'instrument9', 'instrument10', 'instrument11'])
rigid.mode = OrderedSet(['thermograph4', 'image1', 'thermograph3', 'image2', 'thermograph0'])
rigid.supports = OrderedSet( [('instrument0', 'thermograph0'), ('instrument0', 'image1'), ('instrument1', 'image2'), ('instrument1', 'thermograph3'), ('instrument2', 'image1'), ('instrument2', 'thermograph3'), ('instrument2', 'thermograph4'), ('instrument3', 'thermograph0'), ('instrument3', 'thermograph4'), ('instrument3', 'image2'), ('instrument4', 'thermograph4'), ('instrument4', 'image1'), ('instrument4', 'thermograph0'), ('instrument5', 'thermograph4'), ('instrument6', 'thermograph3'), ('instrument6', 'image1'), ('instrument7', 'image2'), ('instrument7', 'thermograph3'), ('instrument8', 'thermograph4'), ('instrument8', 'thermograph0'), ('instrument9', 'thermograph0'), ('instrument9', 'image2'), ('instrument9', 'image1'), ('instrument10', 'thermograph3'), ('instrument10', 'image1'), ('instrument11', 'thermograph0'), ('instrument11', 'image2'), ] )
rigid.calibration_target = OrderedSet( [('instrument0', 'groundstation2'), ('instrument1', 'groundstation0'), ('instrument2', 'groundstation2'), ('instrument3', 'groundstation2'), ('instrument4', 'groundstation1'), ('instrument5', 'groundstation4'), ('instrument6', 'groundstation0'), ('instrument7', 'groundstation4'), ('instrument8', 'groundstation2'), ('instrument9', 'groundstation2'), ('instrument10', 'groundstation0'), ('instrument11', 'groundstation1'), ] )
rigid.on_board = OrderedSet( [('instrument0', 'satellite0'), ('instrument1', 'satellite0'), ('instrument2', 'satellite0'), ('instrument3', 'satellite1'), ('instrument4', 'satellite2'), ('instrument5', 'satellite2'), ('instrument6', 'satellite2'), ('instrument7', 'satellite3'), ('instrument8', 'satellite3'), ('instrument9', 'satellite4'), ('instrument10', 'satellite4'), ('instrument11', 'satellite5'), ] )
state.power_avail = OrderedSet( [('satellite0',), ('satellite1',), ('satellite2',), ('satellite3',), ('satellite4',), ('satellite5',), ] )
state.pointing = OrderedSet( [('satellite0', 'phenomenon12'), ('satellite1', 'groundstation1'), ('satellite2', 'groundstation2'), ('satellite3', 'groundstation4'), ('satellite4', 'planet15'), ('satellite5', 'phenomenon11'), ] )
rigid.goal_pointing = OrderedSet( [('satellite0', 'planet21'), ('satellite2', 'star14'), ('satellite5', 'planet17'), ] )
rigid.goal_have_image = OrderedSet( [('phenomenon5', 'image1'), ('phenomenon7', 'thermograph0'), ('planet8', 'image2'), ('star9', 'thermograph0'), ('star10', 'thermograph3'), ('phenomenon12', 'thermograph0'), ('phenomenon13', 'image1'), ('star14', 'thermograph4'), ('planet15', 'image2'), ('planet17', 'image2'), ('phenomenon18', 'image1'), ('star19', 'thermograph4'), ('star20', 'thermograph4'), ('planet21', 'thermograph0'), ('star22', 'thermograph3'), ('planet23', 'image1'), ] )
state.power_on = OrderedSet( [] )
state.calibrated = OrderedSet( [] )
state.have_image = OrderedSet( [] )

task_list = [('main',)]
