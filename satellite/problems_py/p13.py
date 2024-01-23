from ipyhop import State

from ordered_set import OrderedSet

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = OrderedSet(['instrument0', 'instrument1', 'instrument2', 'instrument3', 'instrument4', 'instrument5', 'instrument6', 'instrument7', 'instrument8', 'satellite0', 'satellite1', 'satellite2', 'satellite3', 'satellite4', 'groundstation2', 'star1', 'star4', 'star0', 'groundstation3', 'phenomenon5', 'planet6', 'planet7', 'planet8', 'planet9', 'planet10', 'planet11', 'phenomenon12', 'planet13', 'star14', 'planet15', 'planet16', 'planet17', 'phenomenon18', 'star19', 'planet20', 'star21', 'star22', 'planet23', 'planet24', 'planet25', 'star26', 'phenomenon27', 'planet28', 'planet29', 'image4', 'thermograph1', 'thermograph0', 'thermograph2', 'image3'])
rigid.satellite = OrderedSet(['satellite0', 'satellite1', 'satellite2', 'satellite3', 'satellite4'])
rigid.direction = OrderedSet(['groundstation2', 'star1', 'star4', 'star0', 'groundstation3', 'phenomenon5', 'planet6', 'planet7', 'planet8', 'planet9', 'planet10', 'planet11', 'phenomenon12', 'planet13', 'star14', 'planet15', 'planet16', 'planet17', 'phenomenon18', 'star19', 'planet20', 'star21', 'star22', 'planet23', 'planet24', 'planet25', 'star26', 'phenomenon27', 'planet28', 'planet29'])
rigid.instrument = OrderedSet(['instrument0', 'instrument1', 'instrument2', 'instrument3', 'instrument4', 'instrument5', 'instrument6', 'instrument7', 'instrument8'])
rigid.mode = OrderedSet(['image4', 'thermograph1', 'thermograph0', 'thermograph2', 'image3'])
rigid.supports = OrderedSet( [('instrument0', 'image4'), ('instrument1', 'thermograph1'), ('instrument1', 'image4'), ('instrument2', 'thermograph0'), ('instrument2', 'image4'), ('instrument2', 'thermograph2'), ('instrument3', 'image4'), ('instrument3', 'image3'), ('instrument4', 'image3'), ('instrument5', 'thermograph1'), ('instrument5', 'image4'), ('instrument6', 'image3'), ('instrument6', 'thermograph1'), ('instrument6', 'thermograph0'), ('instrument7', 'thermograph2'), ('instrument7', 'thermograph0'), ('instrument8', 'image3'), ('instrument8', 'thermograph2'), ] )
rigid.calibration_target = OrderedSet( [('instrument0', 'groundstation3'), ('instrument1', 'groundstation3'), ('instrument2', 'groundstation3'), ('instrument3', 'star1'), ('instrument4', 'groundstation3'), ('instrument5', 'groundstation3'), ('instrument6', 'star4'), ('instrument7', 'star0'), ('instrument8', 'groundstation3'), ] )
rigid.on_board = OrderedSet( [('instrument0', 'satellite0'), ('instrument1', 'satellite0'), ('instrument2', 'satellite1'), ('instrument3', 'satellite2'), ('instrument4', 'satellite2'), ('instrument5', 'satellite3'), ('instrument6', 'satellite4'), ('instrument7', 'satellite4'), ('instrument8', 'satellite4'), ] )
state.power_avail = OrderedSet( [('satellite0',), ('satellite1',), ('satellite2',), ('satellite3',), ('satellite4',), ] )
state.pointing = OrderedSet( [('satellite0', 'star19'), ('satellite1', 'planet17'), ('satellite2', 'planet7'), ('satellite3', 'star4'), ('satellite4', 'phenomenon5'), ] )
rigid.goal_pointing = OrderedSet( [('satellite1', 'phenomenon5'), ('satellite2', 'planet11'), ('satellite4', 'planet11'), ] )
rigid.goal_have_image = OrderedSet( [('phenomenon5', 'thermograph1'), ('planet6', 'image4'), ('planet7', 'image3'), ('planet8', 'image3'), ('planet9', 'thermograph0'), ('planet10', 'thermograph1'), ('planet11', 'thermograph2'), ('phenomenon12', 'image3'), ('planet13', 'thermograph1'), ('star14', 'image3'), ('planet15', 'thermograph0'), ('planet16', 'image3'), ('planet17', 'image4'), ('phenomenon18', 'image3'), ('star19', 'thermograph0'), ('star21', 'thermograph1'), ('star22', 'image4'), ('planet23', 'thermograph1'), ('planet24', 'thermograph2'), ('planet25', 'thermograph1'), ('star26', 'thermograph0'), ('phenomenon27', 'thermograph1'), ('planet28', 'thermograph2'), ('planet29', 'thermograph0'), ] )
state.power_on = OrderedSet( [] )
state.calibrated = OrderedSet( [] )
state.have_image = OrderedSet( [] )

task_list = [('main',)]
