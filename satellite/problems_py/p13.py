from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'planet25', 'phenomenon12', 'groundstation2', 'star21', 'instrument1', 'star4', 'instrument2', 'planet20', 'planet9', 'instrument3', 'image3', 'planet13', 'instrument8', 'planet10', 'instrument5', 'satellite2', 'instrument0', 'thermograph2', 'instrument6', 'planet8', 'star22', 'satellite0', 'star1', 'star0', 'planet16', 'planet23', 'star26', 'satellite3', 'planet15', 'thermograph0', 'thermograph1', 'groundstation3', 'planet29', 'planet17', 'satellite4', 'phenomenon27', 'planet28', 'planet6', 'planet7', 'phenomenon18', 'instrument4', 'star19', 'phenomenon5', 'instrument7', 'planet11', 'satellite1', 'image4', 'star14', 'planet24'}
rigid.mode = {'thermograph0', 'thermograph2', 'image3', 'image4', 'thermograph1'}
rigid.satellite = {'satellite3', 'satellite2', 'satellite0', 'satellite4', 'satellite1'}
rigid.instrument = {'instrument5', 'instrument0', 'instrument1', 'instrument6', 'instrument2', 'instrument4', 'instrument7', 'instrument3', 'instrument8'}
rigid.direction = {'planet25', 'phenomenon12', 'planet15', 'groundstation2', 'star21', 'star4', 'groundstation3', 'planet20', 'planet9', 'planet29', 'planet17', 'phenomenon27', 'planet13', 'planet28', 'planet10', 'star14', 'planet6', 'planet7', 'phenomenon18', 'planet8', 'star22', 'star1', 'star0', 'star19', 'phenomenon5', 'planet16', 'planet11', 'planet23', 'star26', 'planet24'}
rigid.supports = set( [('instrument7', 'thermograph0'), ('instrument8', 'image3'), ('instrument5', 'image4'), ('instrument2', 'thermograph2'), ('instrument0', 'image4'), ('instrument7', 'thermograph2'), ('instrument1', 'image4'), ('instrument3', 'image4'), ('instrument8', 'thermograph2'), ('instrument4', 'image3'), ('instrument5', 'thermograph1'), ('instrument3', 'image3'), ('instrument6', 'thermograph0'), ('instrument1', 'thermograph1'), ('instrument6', 'image3'), ('instrument2', 'image4'), ('instrument6', 'thermograph1'), ('instrument2', 'thermograph0'), ] )
rigid.calibration_target = set( [('instrument5', 'groundstation3'), ('instrument7', 'star0'), ('instrument0', 'groundstation3'), ('instrument4', 'groundstation3'), ('instrument1', 'groundstation3'), ('instrument3', 'star1'), ('instrument6', 'star4'), ('instrument8', 'groundstation3'), ('instrument2', 'groundstation3'), ] )
rigid.on_board = set( [('instrument0', 'satellite0'), ('instrument7', 'satellite4'), ('instrument4', 'satellite2'), ('instrument3', 'satellite2'), ('instrument2', 'satellite1'), ('instrument5', 'satellite3'), ('instrument6', 'satellite4'), ('instrument1', 'satellite0'), ('instrument8', 'satellite4'), ] )
state.power_avail = set( [('satellite1',), ('satellite0',), ('satellite2',), ('satellite4',), ('satellite3',), ] )
state.pointing = set( [('satellite2', 'planet7'), ('satellite3', 'star4'), ('satellite1', 'planet17'), ('satellite4', 'phenomenon5'), ('satellite0', 'star19'), ] )
rigid.goal_pointing = set( [('satellite2', 'planet11'), ('satellite4', 'planet11'), ('satellite1', 'phenomenon5'), ] )
rigid.goal_have_image = set( [('planet17', 'image4'), ('star21', 'thermograph1'), ('planet16', 'image3'), ('planet8', 'image3'), ('planet13', 'thermograph1'), ('phenomenon12', 'image3'), ('planet24', 'thermograph2'), ('planet28', 'thermograph2'), ('phenomenon27', 'thermograph1'), ('star14', 'image3'), ('planet29', 'thermograph0'), ('phenomenon5', 'thermograph1'), ('planet11', 'thermograph2'), ('star26', 'thermograph0'), ('star22', 'image4'), ('planet23', 'thermograph1'), ('planet10', 'thermograph1'), ('planet6', 'image4'), ('phenomenon18', 'image3'), ('planet25', 'thermograph1'), ('planet7', 'image3'), ('planet9', 'thermograph0'), ('star19', 'thermograph0'), ('planet15', 'thermograph0'), ] )
state.calibrated = set( [] )
state.power_on = set( [] )
state.have_image = set( [] )

task_list = [('main',)]
