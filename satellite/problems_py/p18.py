from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'planet20', 'planet6', 'instrument5', 'phenomenon5', 'thermograph3', 'planet23', 'instrument1', 'instrument0', 'instrument10', 'planet11', 'instrument8', 'satellite4', 'satellite2', 'star0', 'thermograph0', 'phenomenon21', 'satellite0', 'star3', 'phenomenon18', 'instrument7', 'star15', 'instrument2', 'planet14', 'instrument4', 'satellite1', 'phenomenon12', 'phenomenon13', 'phenomenon16', 'instrument12', 'groundstation2', 'star9', 'thermograph2', 'star4', 'instrument9', 'instrument6', 'phenomenon17', 'star1', 'thermograph4', 'star22', 'planet19', 'star8', 'image1', 'phenomenon24', 'instrument3', 'star10', 'satellite3', 'instrument11', 'planet7'}
rigid.satellite = {'satellite0', 'satellite3', 'satellite4', 'satellite2', 'satellite1'}
rigid.mode = {'thermograph2', 'thermograph4', 'thermograph3', 'image1', 'thermograph0'}
rigid.instrument = {'instrument5', 'instrument1', 'instrument0', 'instrument10', 'instrument9', 'instrument6', 'instrument4', 'instrument12', 'instrument3', 'instrument8', 'instrument7', 'instrument11', 'instrument2'}
rigid.direction = {'planet20', 'planet6', 'phenomenon5', 'planet23', 'planet11', 'planet14', 'phenomenon12', 'phenomenon13', 'phenomenon16', 'groundstation2', 'star0', 'star9', 'star4', 'phenomenon21', 'star3', 'phenomenon17', 'star1', 'star22', 'planet19', 'star8', 'phenomenon24', 'phenomenon18', 'star10', 'star15', 'planet7'}
rigid.supports = set( [('instrument6', 'thermograph2'), ('instrument3', 'thermograph3'), ('instrument8', 'thermograph3'), ('instrument5', 'thermograph3'), ('instrument0', 'thermograph4'), ('instrument9', 'thermograph2'), ('instrument10', 'thermograph2'), ('instrument8', 'thermograph4'), ('instrument7', 'thermograph0'), ('instrument11', 'thermograph2'), ('instrument6', 'thermograph0'), ('instrument0', 'thermograph2'), ('instrument8', 'thermograph2'), ('instrument11', 'thermograph0'), ('instrument6', 'image1'), ('instrument1', 'thermograph3'), ('instrument4', 'image1'), ('instrument12', 'thermograph4'), ('instrument0', 'thermograph0'), ('instrument9', 'thermograph3'), ('instrument2', 'image1'), ('instrument11', 'thermograph4'), ] )
rigid.calibration_target = set( [('instrument8', 'star3'), ('instrument12', 'star3'), ('instrument1', 'star0'), ('instrument11', 'star1'), ('instrument4', 'star1'), ('instrument7', 'star3'), ('instrument9', 'star1'), ('instrument0', 'star4'), ('instrument10', 'star3'), ('instrument2', 'star4'), ('instrument3', 'star1'), ('instrument6', 'star0'), ('instrument5', 'star3'), ] )
rigid.on_board = set( [('instrument7', 'satellite2'), ('instrument12', 'satellite4'), ('instrument3', 'satellite1'), ('instrument9', 'satellite2'), ('instrument1', 'satellite0'), ('instrument10', 'satellite3'), ('instrument8', 'satellite2'), ('instrument6', 'satellite1'), ('instrument5', 'satellite1'), ('instrument11', 'satellite3'), ('instrument2', 'satellite0'), ('instrument0', 'satellite0'), ('instrument4', 'satellite1'), ] )
state.power_avail = set( [('satellite0',), ('satellite4',), ('satellite2',), ('satellite1',), ('satellite3',), ] )
state.pointing = set( [('satellite2', 'star4'), ('satellite1', 'phenomenon21'), ('satellite0', 'star8'), ('satellite4', 'phenomenon18'), ('satellite3', 'phenomenon16'), ] )
rigid.goal_have_image = set( [('star9', 'image1'), ('star8', 'thermograph3'), ('phenomenon18', 'image1'), ('planet20', 'thermograph4'), ('star10', 'image1'), ('phenomenon21', 'image1'), ('star22', 'thermograph3'), ('star15', 'thermograph2'), ('phenomenon17', 'thermograph4'), ('planet7', 'image1'), ('planet19', 'thermograph2'), ('phenomenon5', 'thermograph4'), ('phenomenon13', 'thermograph2'), ] )
state.have_image = set( [] )
state.power_on = set( [] )
state.calibrated = set( [] )
rigid.goal_pointing = set( [] )

task_list = [('main',)]
