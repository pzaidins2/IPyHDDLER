from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'instrument8', 'instrument0', 'image2', 'groundstation0', 'instrument6', 'instrument4', 'satellite2', 'phenomenon5', 'satellite1', 'groundstation1', 'instrument2', 'instrument5', 'phenomenon8', 'instrument3', 'thermograph0', 'instrument7', 'spectrograph1', 'planet9', 'star4', 'star7', 'satellite0', 'star3', 'phenomenon6', 'groundstation2', 'instrument1'}
rigid.direction = {'planet9', 'star4', 'groundstation0', 'star7', 'phenomenon5', 'star3', 'groundstation1', 'phenomenon6', 'phenomenon8', 'groundstation2'}
rigid.mode = {'thermograph0', 'image2', 'spectrograph1'}
rigid.instrument = {'instrument8', 'instrument0', 'instrument6', 'instrument4', 'instrument2', 'instrument5', 'instrument3', 'instrument7', 'instrument1'}
rigid.satellite = {'satellite0', 'satellite1', 'satellite2'}
rigid.supports = set( [('instrument8', 'thermograph0'), ('instrument5', 'spectrograph1'), ('instrument3', 'spectrograph1'), ('instrument0', 'spectrograph1'), ('instrument6', 'image2'), ('instrument7', 'image2'), ('instrument1', 'spectrograph1'), ('instrument4', 'spectrograph1'), ('instrument5', 'image2'), ('instrument0', 'image2'), ('instrument7', 'thermograph0'), ('instrument2', 'image2'), ('instrument3', 'thermograph0'), ('instrument8', 'spectrograph1'), ('instrument5', 'thermograph0'), ('instrument0', 'thermograph0'), ('instrument1', 'image2'), ('instrument4', 'image2'), ('instrument1', 'thermograph0'), ('instrument8', 'image2'), ] )
rigid.calibration_target = set( [('instrument3', 'groundstation0'), ('instrument7', 'groundstation1'), ('instrument4', 'groundstation2'), ('instrument0', 'groundstation2'), ('instrument1', 'groundstation1'), ('instrument2', 'groundstation0'), ('instrument6', 'groundstation1'), ('instrument5', 'groundstation1'), ('instrument8', 'groundstation0'), ] )
rigid.on_board = set( [('instrument8', 'satellite2'), ('instrument4', 'satellite1'), ('instrument0', 'satellite0'), ('instrument6', 'satellite2'), ('instrument2', 'satellite0'), ('instrument7', 'satellite2'), ('instrument1', 'satellite0'), ('instrument3', 'satellite1'), ('instrument5', 'satellite1'), ] )
state.power_avail = set( [('satellite1',), ('satellite0',), ('satellite2',), ] )
state.pointing = set( [('satellite1', 'groundstation2'), ('satellite0', 'phenomenon8'), ('satellite2', 'phenomenon5'), ] )
rigid.goal_pointing = set( [('satellite1', 'groundstation2'), ('satellite0', 'phenomenon5'), ] )
rigid.goal_have_image = set( [('star3', 'thermograph0'), ('planet9', 'spectrograph1'), ('phenomenon5', 'image2'), ('star7', 'thermograph0'), ('phenomenon6', 'image2'), ('phenomenon8', 'image2'), ] )
state.calibrated = set( [] )
state.power_on = set( [] )
state.have_image = set( [] )

task_list = [('main',)]
