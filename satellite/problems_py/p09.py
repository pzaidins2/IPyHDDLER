from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'star9', 'star14', 'instrument2', 'groundstation1', 'phenomenon6', 'planet5', 'instrument5', 'satellite1', 'phenomenon12', 'image4', 'instrument6', 'infrared1', 'image3', 'satellite3', 'satellite0', 'instrument3', 'star3', 'star2', 'star0', 'phenomenon8', 'image2', 'planet10', 'instrument1', 'star4', 'planet11', 'instrument8', 'instrument7', 'satellite4', 'satellite2', 'spectrograph0', 'phenomenon13', 'instrument0', 'instrument10', 'instrument4', 'phenomenon7', 'instrument9'}
rigid.direction = {'star9', 'star0', 'phenomenon7', 'phenomenon8', 'star14', 'planet10', 'star4', 'groundstation1', 'phenomenon6', 'planet5', 'planet11', 'phenomenon12', 'phenomenon13', 'star3', 'star2'}
rigid.mode = {'spectrograph0', 'image4', 'image2', 'infrared1', 'image3'}
rigid.satellite = {'satellite1', 'satellite2', 'satellite4', 'satellite3', 'satellite0'}
rigid.instrument = {'instrument1', 'instrument2', 'instrument8', 'instrument5', 'instrument7', 'instrument0', 'instrument10', 'instrument6', 'instrument4', 'instrument3', 'instrument9'}
rigid.supports = set( [('instrument1', 'spectrograph0'), ('instrument10', 'infrared1'), ('instrument3', 'image2'), ('instrument0', 'image4'), ('instrument4', 'image2'), ('instrument5', 'image4'), ('instrument6', 'spectrograph0'), ('instrument0', 'infrared1'), ('instrument7', 'image4'), ('instrument3', 'image4'), ('instrument1', 'image2'), ('instrument9', 'image4'), ('instrument7', 'image3'), ('instrument3', 'image3'), ('instrument5', 'infrared1'), ('instrument10', 'image4'), ('instrument8', 'image4'), ('instrument10', 'image2'), ('instrument4', 'image3'), ('instrument1', 'image4'), ('instrument5', 'spectrograph0'), ('instrument8', 'image3'), ('instrument6', 'image2'), ('instrument7', 'spectrograph0'), ('instrument8', 'infrared1'), ('instrument2', 'image2'), ] )
rigid.calibration_target = set( [('instrument0', 'star3'), ('instrument10', 'star2'), ('instrument2', 'star2'), ('instrument1', 'star4'), ('instrument9', 'star0'), ('instrument8', 'groundstation1'), ('instrument6', 'star2'), ('instrument3', 'star2'), ('instrument5', 'star3'), ('instrument4', 'star3'), ('instrument7', 'star0'), ] )
rigid.on_board = set( [('instrument7', 'satellite3'), ('instrument8', 'satellite4'), ('instrument10', 'satellite4'), ('instrument6', 'satellite2'), ('instrument9', 'satellite4'), ('instrument3', 'satellite1'), ('instrument2', 'satellite0'), ('instrument0', 'satellite0'), ('instrument1', 'satellite0'), ('instrument5', 'satellite1'), ('instrument4', 'satellite1'), ] )
state.power_avail = set( [('satellite3',), ('satellite1',), ('satellite0',), ('satellite2',), ('satellite4',), ] )
state.pointing = set( [('satellite0', 'star0'), ('satellite4', 'star9'), ('satellite2', 'phenomenon6'), ('satellite3', 'planet10'), ('satellite1', 'planet11'), ] )
rigid.goal_pointing = set( [('satellite0', 'phenomenon7'), ('satellite3', 'star9'), ('satellite4', 'planet5'), ] )
rigid.goal_have_image = set( [('phenomenon13', 'spectrograph0'), ('planet11', 'spectrograph0'), ('phenomenon6', 'image3'), ('planet5', 'image2'), ('planet10', 'image4'), ('phenomenon8', 'image2'), ('phenomenon12', 'image3'), ('phenomenon7', 'infrared1'), ('star9', 'image3'), ('star14', 'image4'), ] )
state.power_on = set( [] )
state.calibrated = set( [] )
state.have_image = set( [] )

task_list = [('main',)]
