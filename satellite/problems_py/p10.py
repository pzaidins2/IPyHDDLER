from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'instrument8', 'satellite1', 'instrument9', 'star11', 'star1', 'star0', 'image4', 'star16', 'star7', 'planet9', 'satellite0', 'instrument4', 'instrument5', 'groundstation3', 'satellite3', 'instrument3', 'planet10', 'image2', 'instrument10', 'phenomenon13', 'star6', 'instrument1', 'star12', 'phenomenon14', 'satellite4', 'instrument7', 'satellite2', 'planet5', 'phenomenon8', 'star15', 'instrument0', 'infrared3', 'star2', 'spectrograph1', 'instrument2', 'star4', 'infrared0', 'instrument6'}
rigid.instrument = {'instrument8', 'instrument1', 'instrument9', 'instrument4', 'instrument0', 'instrument5', 'instrument2', 'instrument3', 'instrument7', 'instrument10', 'instrument6'}
rigid.direction = {'star11', 'star12', 'phenomenon14', 'star1', 'star0', 'planet5', 'star16', 'phenomenon8', 'star7', 'planet9', 'star15', 'star2', 'groundstation3', 'planet10', 'star4', 'phenomenon13', 'star6'}
rigid.mode = {'spectrograph1', 'image4', 'infrared0', 'image2', 'infrared3'}
rigid.satellite = {'satellite3', 'satellite1', 'satellite4', 'satellite2', 'satellite0'}
rigid.supports = set( [('instrument0', 'image4'), ('instrument2', 'image2'), ('instrument10', 'image2'), ('instrument2', 'infrared0'), ('instrument8', 'image4'), ('instrument5', 'image2'), ('instrument4', 'spectrograph1'), ('instrument4', 'infrared0'), ('instrument3', 'infrared0'), ('instrument7', 'spectrograph1'), ('instrument6', 'infrared0'), ('instrument5', 'infrared0'), ('instrument10', 'image4'), ('instrument4', 'image4'), ('instrument1', 'spectrograph1'), ('instrument1', 'infrared0'), ('instrument7', 'image4'), ('instrument8', 'spectrograph1'), ('instrument5', 'infrared3'), ('instrument3', 'infrared3'), ('instrument9', 'infrared3'), ('instrument6', 'infrared3'), ('instrument7', 'infrared3'), ] )
rigid.calibration_target = set( [('instrument0', 'star1'), ('instrument4', 'star2'), ('instrument8', 'star4'), ('instrument3', 'star4'), ('instrument10', 'star0'), ('instrument1', 'groundstation3'), ('instrument7', 'star4'), ('instrument9', 'star2'), ('instrument2', 'groundstation3'), ('instrument5', 'star0'), ('instrument6', 'groundstation3'), ] )
rigid.on_board = set( [('instrument0', 'satellite0'), ('instrument3', 'satellite1'), ('instrument6', 'satellite3'), ('instrument7', 'satellite3'), ('instrument4', 'satellite2'), ('instrument2', 'satellite1'), ('instrument8', 'satellite4'), ('instrument9', 'satellite4'), ('instrument5', 'satellite2'), ('instrument1', 'satellite0'), ('instrument10', 'satellite4'), ] )
state.power_avail = set( [('satellite0',), ('satellite1',), ('satellite4',), ('satellite2',), ('satellite3',), ] )
state.pointing = set( [('satellite4', 'planet10'), ('satellite1', 'star4'), ('satellite2', 'star1'), ('satellite0', 'star0'), ('satellite3', 'groundstation3'), ] )
rigid.goal_pointing = set( [('satellite4', 'planet9'), ] )
rigid.goal_have_image = set( [('phenomenon8', 'image4'), ('star12', 'image4'), ('star15', 'spectrograph1'), ('phenomenon14', 'spectrograph1'), ('star16', 'image2'), ('planet10', 'infrared3'), ('star6', 'infrared3'), ('star7', 'image4'), ('planet9', 'infrared0'), ('planet5', 'image4'), ('phenomenon13', 'image4'), ] )
state.calibrated = set( [] )
state.have_image = set( [] )
state.power_on = set( [] )

task_list = [('main',)]
