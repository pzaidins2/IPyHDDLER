from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'star4', 'planet13', 'star5', 'star2', 'instrument8', 'groundstation3', 'thermograph2', 'spectrograph4', 'phenomenon9', 'star1', 'infrared1', 'phenomenon7', 'instrument6', 'phenomenon15', 'instrument5', 'satellite1', 'instrument3', 'planet19', 'star10', 'planet6', 'instrument0', 'infrared0', 'satellite2', 'instrument2', 'satellite3', 'star11', 'satellite0', 'instrument4', 'star17', 'star0', 'instrument7', 'star8', 'planet14', 'image3', 'planet16', 'star18', 'star12', 'instrument1', 'satellite4'}
rigid.satellite = {'satellite1', 'satellite0', 'satellite2', 'satellite4', 'satellite3'}
rigid.instrument = {'instrument0', 'instrument2', 'instrument5', 'instrument8', 'instrument7', 'instrument4', 'instrument3', 'instrument1', 'instrument6'}
rigid.mode = {'image3', 'spectrograph4', 'infrared0', 'infrared1', 'thermograph2'}
rigid.direction = {'star4', 'planet6', 'planet13', 'star5', 'star2', 'groundstation3', 'star11', 'star17', 'star0', 'star8', 'phenomenon9', 'planet14', 'star1', 'phenomenon7', 'planet16', 'phenomenon15', 'star18', 'star12', 'planet19', 'star10'}
rigid.supports = set( [('instrument5', 'thermograph2'), ('instrument3', 'spectrograph4'), ('instrument6', 'infrared0'), ('instrument8', 'infrared0'), ('instrument0', 'spectrograph4'), ('instrument8', 'spectrograph4'), ('instrument7', 'image3'), ('instrument4', 'infrared1'), ('instrument5', 'spectrograph4'), ('instrument4', 'infrared0'), ('instrument1', 'infrared1'), ('instrument1', 'infrared0'), ('instrument3', 'infrared1'), ('instrument3', 'thermograph2'), ('instrument4', 'image3'), ('instrument8', 'infrared1'), ('instrument2', 'infrared1'), ('instrument2', 'infrared0'), ] )
rigid.calibration_target = set( [('instrument2', 'star2'), ('instrument1', 'groundstation3'), ('instrument7', 'star2'), ('instrument3', 'star0'), ('instrument4', 'star2'), ('instrument0', 'star0'), ('instrument6', 'groundstation3'), ('instrument5', 'star0'), ('instrument8', 'star2'), ] )
rigid.on_board = set( [('instrument8', 'satellite4'), ('instrument3', 'satellite1'), ('instrument5', 'satellite2'), ('instrument0', 'satellite0'), ('instrument2', 'satellite1'), ('instrument6', 'satellite2'), ('instrument7', 'satellite3'), ('instrument4', 'satellite2'), ('instrument1', 'satellite1'), ] )
state.power_avail = set( [('satellite4',), ('satellite1',), ('satellite0',), ('satellite3',), ('satellite2',), ] )
state.pointing = set( [('satellite4', 'phenomenon9'), ('satellite2', 'star4'), ('satellite0', 'star8'), ('satellite1', 'groundstation3'), ('satellite3', 'phenomenon9'), ] )
rigid.goal_pointing = set( [('satellite0', 'phenomenon9'), ('satellite4', 'star11'), ('satellite1', 'star4'), ] )
rigid.goal_have_image = set( [('star5', 'image3'), ('star11', 'infrared1'), ('star10', 'thermograph2'), ('planet16', 'image3'), ('star17', 'infrared0'), ('star8', 'image3'), ('phenomenon15', 'infrared0'), ('phenomenon7', 'infrared1'), ('planet13', 'spectrograph4'), ('planet14', 'thermograph2'), ('planet6', 'infrared1'), ] )
state.calibrated = set( [] )
state.have_image = set( [] )
state.power_on = set( [] )

task_list = [('main',)]
