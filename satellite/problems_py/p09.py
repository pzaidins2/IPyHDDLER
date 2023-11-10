from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'phenomenon8', 'instrument5', 'instrument1', 'instrument0', 'instrument10', 'planet11', 'image4', 'instrument4', 'phenomenon12', 'satellite1', 'phenomenon13', 'instrument8', 'star2', 'image2', 'satellite4', 'phenomenon6', 'satellite2', 'star14', 'spectrograph0', 'star0', 'star9', 'image3', 'star4', 'groundstation1', 'planet5', 'planet10', 'instrument9', 'infrared1', 'phenomenon7', 'instrument6', 'satellite0', 'instrument3', 'satellite3', 'star3', 'instrument7', 'instrument2'}
rigid.satellite = {'satellite0', 'satellite3', 'satellite4', 'satellite2', 'satellite1'}
rigid.mode = {'image2', 'spectrograph0', 'image3', 'infrared1', 'image4'}
rigid.instrument = {'instrument5', 'instrument1', 'instrument0', 'instrument10', 'instrument9', 'instrument6', 'instrument4', 'instrument3', 'instrument8', 'instrument7', 'instrument2'}
rigid.direction = {'star0', 'phenomenon8', 'star9', 'star4', 'groundstation1', 'planet5', 'planet10', 'planet11', 'phenomenon7', 'phenomenon12', 'phenomenon13', 'star2', 'star3', 'phenomenon6', 'star14'}
rigid.supports = set( [('instrument6', 'spectrograph0'), ('instrument1', 'spectrograph0'), ('instrument1', 'image4'), ('instrument10', 'image4'), ('instrument3', 'image3'), ('instrument9', 'image4'), ('instrument8', 'image3'), ('instrument0', 'infrared1'), ('instrument5', 'infrared1'), ('instrument8', 'infrared1'), ('instrument6', 'image2'), ('instrument3', 'image4'), ('instrument0', 'image4'), ('instrument8', 'image4'), ('instrument4', 'image2'), ('instrument1', 'image2'), ('instrument5', 'spectrograph0'), ('instrument5', 'image4'), ('instrument10', 'image2'), ('instrument2', 'image2'), ('instrument7', 'image3'), ('instrument3', 'image2'), ('instrument4', 'image3'), ('instrument7', 'spectrograph0'), ('instrument7', 'image4'), ('instrument10', 'infrared1'), ] )
rigid.calibration_target = set( [('instrument10', 'star2'), ('instrument3', 'star2'), ('instrument2', 'star2'), ('instrument1', 'star4'), ('instrument4', 'star3'), ('instrument7', 'star0'), ('instrument6', 'star2'), ('instrument9', 'star0'), ('instrument0', 'star3'), ('instrument8', 'groundstation1'), ('instrument5', 'star3'), ] )
rigid.on_board = set( [('instrument8', 'satellite4'), ('instrument7', 'satellite3'), ('instrument3', 'satellite1'), ('instrument1', 'satellite0'), ('instrument6', 'satellite2'), ('instrument5', 'satellite1'), ('instrument10', 'satellite4'), ('instrument2', 'satellite0'), ('instrument9', 'satellite4'), ('instrument0', 'satellite0'), ('instrument4', 'satellite1'), ] )
state.power_avail = set( [('satellite0',), ('satellite4',), ('satellite2',), ('satellite1',), ('satellite3',), ] )
state.pointing = set( [('satellite0', 'star0'), ('satellite3', 'planet10'), ('satellite2', 'phenomenon6'), ('satellite1', 'planet11'), ('satellite4', 'star9'), ] )
rigid.goal_pointing = set( [('satellite3', 'star9'), ('satellite4', 'planet5'), ('satellite0', 'phenomenon7'), ] )
rigid.goal_have_image = set( [('planet5', 'image2'), ('star9', 'image3'), ('phenomenon6', 'image3'), ('star14', 'image4'), ('phenomenon7', 'infrared1'), ('phenomenon12', 'image3'), ('planet10', 'image4'), ('phenomenon13', 'spectrograph0'), ('planet11', 'spectrograph0'), ('phenomenon8', 'image2'), ] )
state.have_image = set( [] )
state.power_on = set( [] )
state.calibrated = set( [] )

task_list = [('main',)]
