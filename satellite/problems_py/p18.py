from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'star9', 'phenomenon18', 'planet19', 'phenomenon16', 'image1', 'instrument11', 'instrument6', 'phenomenon17', 'planet6', 'star1', 'thermograph2', 'star15', 'planet7', 'star4', 'phenomenon21', 'instrument0', 'instrument4', 'planet14', 'planet23', 'instrument12', 'instrument9', 'star10', 'thermograph3', 'instrument2', 'instrument5', 'satellite1', 'phenomenon12', 'star8', 'thermograph0', 'satellite3', 'satellite0', 'instrument3', 'star3', 'phenomenon24', 'star0', 'groundstation2', 'instrument1', 'instrument8', 'planet11', 'thermograph4', 'instrument7', 'planet20', 'satellite2', 'satellite4', 'phenomenon13', 'instrument10', 'star22', 'phenomenon5'}
rigid.direction = {'star9', 'phenomenon18', 'planet19', 'star10', 'phenomenon16', 'phenomenon12', 'star8', 'phenomenon17', 'planet6', 'star3', 'star1', 'phenomenon24', 'star0', 'star15', 'groundstation2', 'planet7', 'star4', 'phenomenon21', 'planet11', 'planet20', 'planet14', 'phenomenon13', 'star22', 'phenomenon5', 'planet23'}
rigid.mode = {'thermograph3', 'thermograph0', 'image1', 'thermograph4', 'thermograph2'}
rigid.satellite = {'satellite1', 'satellite2', 'satellite4', 'satellite3', 'satellite0'}
rigid.instrument = {'instrument1', 'instrument2', 'instrument8', 'instrument11', 'instrument5', 'instrument7', 'instrument0', 'instrument10', 'instrument6', 'instrument4', 'instrument3', 'instrument12', 'instrument9'}
rigid.supports = set( [('instrument8', 'thermograph4'), ('instrument10', 'thermograph2'), ('instrument8', 'thermograph3'), ('instrument0', 'thermograph0'), ('instrument6', 'thermograph2'), ('instrument1', 'thermograph3'), ('instrument11', 'thermograph4'), ('instrument7', 'thermograph0'), ('instrument0', 'thermograph2'), ('instrument6', 'image1'), ('instrument2', 'image1'), ('instrument0', 'thermograph4'), ('instrument9', 'thermograph2'), ('instrument11', 'thermograph0'), ('instrument8', 'thermograph2'), ('instrument5', 'thermograph3'), ('instrument12', 'thermograph4'), ('instrument3', 'thermograph3'), ('instrument6', 'thermograph0'), ('instrument9', 'thermograph3'), ('instrument11', 'thermograph2'), ('instrument4', 'image1'), ] )
rigid.calibration_target = set( [('instrument7', 'star3'), ('instrument9', 'star1'), ('instrument6', 'star0'), ('instrument10', 'star3'), ('instrument2', 'star4'), ('instrument0', 'star4'), ('instrument4', 'star1'), ('instrument11', 'star1'), ('instrument8', 'star3'), ('instrument5', 'star3'), ('instrument3', 'star1'), ('instrument12', 'star3'), ('instrument1', 'star0'), ] )
rigid.on_board = set( [('instrument10', 'satellite3'), ('instrument12', 'satellite4'), ('instrument9', 'satellite2'), ('instrument3', 'satellite1'), ('instrument8', 'satellite2'), ('instrument11', 'satellite3'), ('instrument6', 'satellite1'), ('instrument2', 'satellite0'), ('instrument0', 'satellite0'), ('instrument1', 'satellite0'), ('instrument7', 'satellite2'), ('instrument5', 'satellite1'), ('instrument4', 'satellite1'), ] )
state.power_avail = set( [('satellite3',), ('satellite1',), ('satellite0',), ('satellite2',), ('satellite4',), ] )
state.pointing = set( [('satellite2', 'star4'), ('satellite3', 'phenomenon16'), ('satellite1', 'phenomenon21'), ('satellite4', 'phenomenon18'), ('satellite0', 'star8'), ] )
rigid.goal_have_image = set( [('phenomenon5', 'thermograph4'), ('phenomenon13', 'thermograph2'), ('planet7', 'image1'), ('star22', 'thermograph3'), ('planet19', 'thermograph2'), ('star15', 'thermograph2'), ('star10', 'image1'), ('star8', 'thermograph3'), ('phenomenon18', 'image1'), ('phenomenon21', 'image1'), ('star9', 'image1'), ('planet20', 'thermograph4'), ('phenomenon17', 'thermograph4'), ] )
state.power_on = set( [] )
state.calibrated = set( [] )
rigid.goal_pointing = set( [] )
state.have_image = set( [] )

task_list = [('main',)]
