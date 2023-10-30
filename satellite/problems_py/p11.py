from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'star5', 'instrument0', 'instrument4', 'planet14', 'phenomenon7', 'phenomenon15', 'star10', 'planet19', 'satellite1', 'planet13', 'infrared0', 'instrument5', 'instrument3', 'star8', 'star4', 'planet16', 'star12', 'planet6', 'star11', 'instrument8', 'instrument6', 'star0', 'star2', 'satellite2', 'star17', 'instrument2', 'satellite4', 'instrument7', 'satellite3', 'star18', 'phenomenon9', 'image3', 'spectrograph4', 'infrared1', 'groundstation3', 'satellite0', 'thermograph2', 'star1', 'instrument1'}
rigid.direction = {'star5', 'planet14', 'phenomenon7', 'star0', 'star2', 'phenomenon15', 'star10', 'planet19', 'star17', 'planet13', 'star8', 'star4', 'star18', 'phenomenon9', 'planet16', 'groundstation3', 'star12', 'planet6', 'star11', 'star1'}
rigid.mode = {'infrared0', 'image3', 'spectrograph4', 'infrared1', 'thermograph2'}
rigid.instrument = {'instrument8', 'instrument0', 'instrument6', 'instrument4', 'instrument2', 'instrument5', 'instrument3', 'instrument7', 'instrument1'}
rigid.satellite = {'satellite3', 'satellite0', 'satellite1', 'satellite4', 'satellite2'}
rigid.supports = set( [('instrument7', 'image3'), ('instrument2', 'infrared0'), ('instrument8', 'infrared0'), ('instrument4', 'infrared1'), ('instrument1', 'infrared0'), ('instrument5', 'thermograph2'), ('instrument8', 'spectrograph4'), ('instrument8', 'infrared1'), ('instrument2', 'infrared1'), ('instrument3', 'spectrograph4'), ('instrument5', 'spectrograph4'), ('instrument6', 'infrared0'), ('instrument0', 'spectrograph4'), ('instrument4', 'image3'), ('instrument4', 'infrared0'), ('instrument1', 'infrared1'), ('instrument3', 'thermograph2'), ('instrument3', 'infrared1'), ] )
rigid.calibration_target = set( [('instrument6', 'groundstation3'), ('instrument8', 'star2'), ('instrument4', 'star2'), ('instrument7', 'star2'), ('instrument1', 'groundstation3'), ('instrument3', 'star0'), ('instrument2', 'star2'), ('instrument5', 'star0'), ('instrument0', 'star0'), ] )
rigid.on_board = set( [('instrument7', 'satellite3'), ('instrument8', 'satellite4'), ('instrument0', 'satellite0'), ('instrument5', 'satellite2'), ('instrument6', 'satellite2'), ('instrument2', 'satellite1'), ('instrument4', 'satellite2'), ('instrument1', 'satellite1'), ('instrument3', 'satellite1'), ] )
state.power_avail = set( [('satellite3',), ('satellite1',), ('satellite0',), ('satellite2',), ('satellite4',), ] )
state.pointing = set( [('satellite2', 'star4'), ('satellite0', 'star8'), ('satellite1', 'groundstation3'), ('satellite4', 'phenomenon9'), ('satellite3', 'phenomenon9'), ] )
rigid.goal_pointing = set( [('satellite4', 'star11'), ('satellite1', 'star4'), ('satellite0', 'phenomenon9'), ] )
rigid.goal_have_image = set( [('star11', 'infrared1'), ('phenomenon15', 'infrared0'), ('planet6', 'infrared1'), ('star5', 'image3'), ('phenomenon7', 'infrared1'), ('planet13', 'spectrograph4'), ('planet14', 'thermograph2'), ('star10', 'thermograph2'), ('star17', 'infrared0'), ('star8', 'image3'), ('planet16', 'image3'), ] )
state.calibrated = set( [] )
state.power_on = set( [] )
state.have_image = set( [] )

task_list = [('main',)]
