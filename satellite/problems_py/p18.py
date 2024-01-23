from ipyhop import State

from ordered_set import OrderedSet

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = OrderedSet(['instrument0', 'instrument1', 'instrument2', 'instrument3', 'instrument4', 'instrument5', 'instrument6', 'instrument7', 'instrument8', 'instrument9', 'instrument10', 'instrument11', 'instrument12', 'satellite0', 'satellite1', 'satellite2', 'satellite3', 'satellite4', 'groundstation2', 'star4', 'star0', 'star1', 'star3', 'phenomenon5', 'planet6', 'planet7', 'star8', 'star9', 'star10', 'planet11', 'phenomenon12', 'phenomenon13', 'planet14', 'star15', 'phenomenon16', 'phenomenon17', 'phenomenon18', 'planet19', 'planet20', 'phenomenon21', 'star22', 'planet23', 'phenomenon24', 'image1', 'thermograph3', 'thermograph0', 'thermograph2', 'thermograph4'])
rigid.satellite = OrderedSet(['satellite0', 'satellite1', 'satellite2', 'satellite3', 'satellite4'])
rigid.direction = OrderedSet(['groundstation2', 'star4', 'star0', 'star1', 'star3', 'phenomenon5', 'planet6', 'planet7', 'star8', 'star9', 'star10', 'planet11', 'phenomenon12', 'phenomenon13', 'planet14', 'star15', 'phenomenon16', 'phenomenon17', 'phenomenon18', 'planet19', 'planet20', 'phenomenon21', 'star22', 'planet23', 'phenomenon24'])
rigid.instrument = OrderedSet(['instrument0', 'instrument1', 'instrument2', 'instrument3', 'instrument4', 'instrument5', 'instrument6', 'instrument7', 'instrument8', 'instrument9', 'instrument10', 'instrument11', 'instrument12'])
rigid.mode = OrderedSet(['image1', 'thermograph3', 'thermograph0', 'thermograph2', 'thermograph4'])
rigid.supports = OrderedSet( [('instrument0', 'thermograph4'), ('instrument0', 'thermograph0'), ('instrument0', 'thermograph2'), ('instrument1', 'thermograph3'), ('instrument2', 'image1'), ('instrument3', 'thermograph3'), ('instrument4', 'image1'), ('instrument5', 'thermograph3'), ('instrument6', 'thermograph2'), ('instrument6', 'thermograph0'), ('instrument6', 'image1'), ('instrument7', 'thermograph0'), ('instrument8', 'thermograph4'), ('instrument8', 'thermograph3'), ('instrument8', 'thermograph2'), ('instrument9', 'thermograph2'), ('instrument9', 'thermograph3'), ('instrument10', 'thermograph2'), ('instrument11', 'thermograph2'), ('instrument11', 'thermograph4'), ('instrument11', 'thermograph0'), ('instrument12', 'thermograph4'), ] )
rigid.calibration_target = OrderedSet( [('instrument0', 'star4'), ('instrument1', 'star0'), ('instrument2', 'star4'), ('instrument3', 'star1'), ('instrument4', 'star1'), ('instrument5', 'star3'), ('instrument6', 'star0'), ('instrument7', 'star3'), ('instrument8', 'star3'), ('instrument9', 'star1'), ('instrument10', 'star3'), ('instrument11', 'star1'), ('instrument12', 'star3'), ] )
rigid.on_board = OrderedSet( [('instrument0', 'satellite0'), ('instrument1', 'satellite0'), ('instrument2', 'satellite0'), ('instrument3', 'satellite1'), ('instrument4', 'satellite1'), ('instrument5', 'satellite1'), ('instrument6', 'satellite1'), ('instrument7', 'satellite2'), ('instrument8', 'satellite2'), ('instrument9', 'satellite2'), ('instrument10', 'satellite3'), ('instrument11', 'satellite3'), ('instrument12', 'satellite4'), ] )
state.power_avail = OrderedSet( [('satellite0',), ('satellite1',), ('satellite2',), ('satellite3',), ('satellite4',), ] )
state.pointing = OrderedSet( [('satellite0', 'star8'), ('satellite1', 'phenomenon21'), ('satellite2', 'star4'), ('satellite3', 'phenomenon16'), ('satellite4', 'phenomenon18'), ] )
rigid.goal_have_image = OrderedSet( [('phenomenon5', 'thermograph4'), ('planet7', 'image1'), ('star8', 'thermograph3'), ('star9', 'image1'), ('star10', 'image1'), ('phenomenon13', 'thermograph2'), ('star15', 'thermograph2'), ('phenomenon17', 'thermograph4'), ('phenomenon18', 'image1'), ('planet19', 'thermograph2'), ('planet20', 'thermograph4'), ('phenomenon21', 'image1'), ('star22', 'thermograph3'), ] )
state.power_on = OrderedSet( [] )
state.calibrated = OrderedSet( [] )
state.have_image = OrderedSet( [] )
rigid.goal_pointing = OrderedSet( [] )

task_list = [('main',)]
