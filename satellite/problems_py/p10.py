from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'image2', 'image4', 'infrared3', 'satellite2', 'satellite1', 'satellite3', 'infrared0', 'star6', 'planet9', 'instrument7', 'spectrograph1', 'phenomenon14', 'instrument6', 'star11', 'instrument0', 'planet10', 'star16', 'star1', 'phenomenon8', 'instrument4', 'star2', 'star7', 'instrument3', 'instrument1', 'star0', 'satellite0', 'instrument2', 'satellite4', 'planet5', 'instrument8', 'instrument5', 'star15', 'phenomenon13', 'groundstation3', 'star12', 'star4', 'instrument10', 'instrument9'}
rigid.direction = {'phenomenon8', 'star2', 'star7', 'star6', 'planet9', 'star0', 'phenomenon14', 'star11', 'planet5', 'star15', 'phenomenon13', 'planet10', 'groundstation3', 'star16', 'star1', 'star4', 'star12'}
rigid.satellite = {'satellite4', 'satellite2', 'satellite1', 'satellite0', 'satellite3'}
rigid.instrument = {'instrument4', 'instrument8', 'instrument5', 'instrument7', 'instrument3', 'instrument1', 'instrument10', 'instrument0', 'instrument2', 'instrument6', 'instrument9'}
rigid.mode = {'image2', 'image4', 'infrared3', 'spectrograph1', 'infrared0'}
rigid.supports = set( [('instrument2', 'image2'), ('instrument7', 'infrared3'), ('instrument4', 'image4'), ('instrument10', 'image2'), ('instrument6', 'infrared0'), ('instrument7', 'image4'), ('instrument3', 'infrared3'), ('instrument10', 'image4'), ('instrument5', 'infrared0'), ('instrument8', 'image4'), ('instrument4', 'infrared0'), ('instrument4', 'spectrograph1'), ('instrument2', 'infrared0'), ('instrument7', 'spectrograph1'), ('instrument6', 'infrared3'), ('instrument5', 'infrared3'), ('instrument1', 'infrared0'), ('instrument1', 'spectrograph1'), ('instrument9', 'infrared3'), ('instrument8', 'spectrograph1'), ('instrument3', 'infrared0'), ('instrument5', 'image2'), ('instrument0', 'image4'), ] )
rigid.calibration_target = set( [('instrument2', 'groundstation3'), ('instrument1', 'groundstation3'), ('instrument0', 'star1'), ('instrument8', 'star4'), ('instrument9', 'star2'), ('instrument7', 'star4'), ('instrument5', 'star0'), ('instrument3', 'star4'), ('instrument10', 'star0'), ('instrument4', 'star2'), ('instrument6', 'groundstation3'), ] )
rigid.on_board = set( [('instrument0', 'satellite0'), ('instrument3', 'satellite1'), ('instrument5', 'satellite2'), ('instrument8', 'satellite4'), ('instrument6', 'satellite3'), ('instrument4', 'satellite2'), ('instrument9', 'satellite4'), ('instrument10', 'satellite4'), ('instrument7', 'satellite3'), ('instrument1', 'satellite0'), ('instrument2', 'satellite1'), ] )
state.power_avail = set( [('satellite3',), ('satellite0',), ('satellite2',), ('satellite1',), ('satellite4',), ] )
state.pointing = set( [('satellite3', 'groundstation3'), ('satellite2', 'star1'), ('satellite1', 'star4'), ('satellite4', 'planet10'), ('satellite0', 'star0'), ] )
rigid.goal_pointing = set( [('satellite4', 'planet9'), ] )
rigid.goal_have_image = set( [('planet5', 'image4'), ('star12', 'image4'), ('phenomenon14', 'spectrograph1'), ('planet9', 'infrared0'), ('phenomenon8', 'image4'), ('star15', 'spectrograph1'), ('star7', 'image4'), ('planet10', 'infrared3'), ('phenomenon13', 'image4'), ('star6', 'infrared3'), ('star16', 'image2'), ] )
state.power_on = set( [] )
state.have_image = set( [] )
state.calibrated = set( [] )

task_list = [('main',)]
