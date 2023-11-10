from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'phenomenon8', 'groundstation2', 'thermograph0', 'instrument1', 'star4', 'instrument2', 'star3', 'spectrograph1', 'planet9', 'instrument3', 'instrument8', 'image2', 'groundstation0', 'instrument5', 'satellite2', 'instrument0', 'instrument6', 'star7', 'instrument4', 'phenomenon5', 'satellite0', 'instrument7', 'phenomenon6', 'satellite1', 'groundstation1'}
rigid.mode = {'spectrograph1', 'image2', 'thermograph0'}
rigid.satellite = {'satellite2', 'satellite1', 'satellite0'}
rigid.instrument = {'instrument5', 'instrument0', 'instrument1', 'instrument6', 'instrument2', 'instrument4', 'instrument7', 'instrument3', 'instrument8'}
rigid.direction = {'groundstation0', 'phenomenon8', 'groundstation2', 'star4', 'star7', 'star3', 'phenomenon5', 'planet9', 'phenomenon6', 'groundstation1'}
rigid.supports = set( [('instrument1', 'image2'), ('instrument0', 'thermograph0'), ('instrument6', 'image2'), ('instrument8', 'spectrograph1'), ('instrument2', 'image2'), ('instrument8', 'thermograph0'), ('instrument4', 'image2'), ('instrument3', 'spectrograph1'), ('instrument0', 'image2'), ('instrument3', 'thermograph0'), ('instrument4', 'spectrograph1'), ('instrument8', 'image2'), ('instrument1', 'spectrograph1'), ('instrument5', 'spectrograph1'), ('instrument7', 'thermograph0'), ('instrument5', 'thermograph0'), ('instrument1', 'thermograph0'), ('instrument0', 'spectrograph1'), ('instrument7', 'image2'), ('instrument5', 'image2'), ] )
rigid.calibration_target = set( [('instrument5', 'groundstation1'), ('instrument1', 'groundstation1'), ('instrument2', 'groundstation0'), ('instrument8', 'groundstation0'), ('instrument4', 'groundstation2'), ('instrument0', 'groundstation2'), ('instrument3', 'groundstation0'), ('instrument6', 'groundstation1'), ('instrument7', 'groundstation1'), ] )
rigid.on_board = set( [('instrument0', 'satellite0'), ('instrument3', 'satellite1'), ('instrument7', 'satellite2'), ('instrument4', 'satellite1'), ('instrument6', 'satellite2'), ('instrument2', 'satellite0'), ('instrument5', 'satellite1'), ('instrument1', 'satellite0'), ('instrument8', 'satellite2'), ] )
state.power_avail = set( [('satellite1',), ('satellite2',), ('satellite0',), ] )
state.pointing = set( [('satellite0', 'phenomenon8'), ('satellite1', 'groundstation2'), ('satellite2', 'phenomenon5'), ] )
rigid.goal_pointing = set( [('satellite1', 'groundstation2'), ('satellite0', 'phenomenon5'), ] )
rigid.goal_have_image = set( [('planet9', 'spectrograph1'), ('star3', 'thermograph0'), ('phenomenon6', 'image2'), ('phenomenon8', 'image2'), ('star7', 'thermograph0'), ('phenomenon5', 'image2'), ] )
state.calibrated = set( [] )
state.power_on = set( [] )
state.have_image = set( [] )

task_list = [('main',)]
