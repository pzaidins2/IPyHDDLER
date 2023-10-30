from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'image4', 'planet24', 'instrument5', 'star14', 'groundstation2', 'star1', 'instrument4', 'instrument2', 'groundstation3', 'planet29', 'planet6', 'planet9', 'planet10', 'star4', 'planet17', 'thermograph1', 'instrument1', 'planet23', 'planet20', 'satellite3', 'instrument8', 'image3', 'star19', 'instrument7', 'planet15', 'star26', 'instrument3', 'planet7', 'phenomenon12', 'planet16', 'planet25', 'satellite4', 'instrument0', 'satellite0', 'phenomenon5', 'phenomenon18', 'star0', 'phenomenon27', 'star22', 'instrument6', 'satellite1', 'thermograph0', 'thermograph2', 'planet13', 'star21', 'satellite2', 'planet8', 'planet11', 'planet28'}
rigid.satellite = {'satellite4', 'satellite0', 'satellite2', 'satellite1', 'satellite3'}
rigid.direction = {'planet15', 'star26', 'planet24', 'star14', 'groundstation2', 'planet7', 'phenomenon12', 'planet16', 'star1', 'planet25', 'groundstation3', 'planet29', 'phenomenon5', 'planet6', 'planet9', 'planet10', 'star4', 'phenomenon18', 'star0', 'planet17', 'planet23', 'phenomenon27', 'planet20', 'star22', 'planet13', 'star21', 'planet8', 'planet11', 'star19', 'planet28'}
rigid.mode = {'thermograph0', 'image4', 'thermograph2', 'thermograph1', 'image3'}
rigid.instrument = {'instrument7', 'instrument5', 'instrument1', 'instrument3', 'instrument6', 'instrument8', 'instrument4', 'instrument2', 'instrument0'}
rigid.supports = set( [('instrument2', 'image4'), ('instrument2', 'thermograph0'), ('instrument8', 'thermograph2'), ('instrument5', 'image4'), ('instrument1', 'image4'), ('instrument3', 'image4'), ('instrument2', 'thermograph2'), ('instrument0', 'image4'), ('instrument3', 'image3'), ('instrument5', 'thermograph1'), ('instrument1', 'thermograph1'), ('instrument6', 'thermograph0'), ('instrument4', 'image3'), ('instrument7', 'thermograph2'), ('instrument6', 'image3'), ('instrument8', 'image3'), ('instrument7', 'thermograph0'), ('instrument6', 'thermograph1'), ] )
rigid.calibration_target = set( [('instrument7', 'star0'), ('instrument8', 'groundstation3'), ('instrument2', 'groundstation3'), ('instrument3', 'star1'), ('instrument5', 'groundstation3'), ('instrument1', 'groundstation3'), ('instrument6', 'star4'), ('instrument0', 'groundstation3'), ('instrument4', 'groundstation3'), ] )
rigid.on_board = set( [('instrument7', 'satellite4'), ('instrument1', 'satellite0'), ('instrument0', 'satellite0'), ('instrument5', 'satellite3'), ('instrument3', 'satellite2'), ('instrument8', 'satellite4'), ('instrument6', 'satellite4'), ('instrument2', 'satellite1'), ('instrument4', 'satellite2'), ] )
state.power_avail = set( [('satellite1',), ('satellite0',), ('satellite4',), ('satellite3',), ('satellite2',), ] )
state.pointing = set( [('satellite3', 'star4'), ('satellite0', 'star19'), ('satellite1', 'planet17'), ('satellite2', 'planet7'), ('satellite4', 'phenomenon5'), ] )
rigid.goal_pointing = set( [('satellite4', 'planet11'), ('satellite2', 'planet11'), ('satellite1', 'phenomenon5'), ] )
rigid.goal_have_image = set( [('planet7', 'image3'), ('phenomenon18', 'image3'), ('star21', 'thermograph1'), ('planet6', 'image4'), ('planet9', 'thermograph0'), ('phenomenon12', 'image3'), ('planet13', 'thermograph1'), ('planet15', 'thermograph0'), ('star19', 'thermograph0'), ('planet29', 'thermograph0'), ('phenomenon27', 'thermograph1'), ('planet23', 'thermograph1'), ('star22', 'image4'), ('planet8', 'image3'), ('planet24', 'thermograph2'), ('planet11', 'thermograph2'), ('star14', 'image3'), ('planet10', 'thermograph1'), ('planet28', 'thermograph2'), ('phenomenon5', 'thermograph1'), ('planet25', 'thermograph1'), ('star26', 'thermograph0'), ('planet17', 'image4'), ('planet16', 'image3'), ] )
state.calibrated = set( [] )
state.have_image = set( [] )
state.power_on = set( [] )

task_list = [('main',)]
