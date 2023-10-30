from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'instrument0', 'instrument3', 'instrument2', 'star6', 'groundstation2', 'instrument1', 'instrument4', 'groundstation4', 'planet10', 'satellite2', 'star1', 'groundstation0', 'satellite1', 'satellite3', 'instrument6', 'star7', 'image2', 'planet9', 'image3', 'image0', 'instrument7', 'satellite0', 'planet11', 'planet8', 'instrument5', 'star3', 'phenomenon5', 'image1'}
rigid.direction = {'star6', 'groundstation2', 'star7', 'planet9', 'groundstation4', 'planet10', 'planet11', 'star1', 'planet8', 'star3', 'groundstation0', 'phenomenon5'}
rigid.mode = {'image0', 'image3', 'image1', 'image2'}
rigid.satellite = {'satellite2', 'satellite1', 'satellite3', 'satellite0'}
rigid.instrument = {'instrument0', 'instrument3', 'instrument6', 'instrument1', 'instrument4', 'instrument7', 'instrument5', 'instrument2'}
rigid.supports = set( [('instrument7', 'image3'), ('instrument6', 'image0'), ('instrument5', 'image0'), ('instrument3', 'image2'), ('instrument4', 'image0'), ('instrument7', 'image0'), ('instrument2', 'image0'), ('instrument3', 'image0'), ('instrument6', 'image1'), ('instrument5', 'image1'), ('instrument0', 'image1'), ('instrument1', 'image3'), ('instrument6', 'image2'), ('instrument7', 'image1'), ('instrument0', 'image3'), ('instrument5', 'image2'), ('instrument4', 'image1'), ] )
rigid.calibration_target = set( [('instrument7', 'groundstation0'), ('instrument3', 'groundstation4'), ('instrument2', 'groundstation2'), ('instrument5', 'star1'), ('instrument0', 'star1'), ('instrument4', 'star1'), ('instrument6', 'groundstation4'), ('instrument1', 'groundstation0'), ] )
rigid.on_board = set( [('instrument4', 'satellite2'), ('instrument6', 'satellite3'), ('instrument0', 'satellite0'), ('instrument1', 'satellite0'), ('instrument2', 'satellite0'), ('instrument7', 'satellite3'), ('instrument3', 'satellite1'), ('instrument5', 'satellite2'), ] )
state.power_avail = set( [('satellite0',), ('satellite2',), ('satellite1',), ('satellite3',), ] )
state.pointing = set( [('satellite3', 'groundstation2'), ('satellite0', 'star6'), ('satellite1', 'groundstation0'), ('satellite2', 'star6'), ] )
rigid.goal_pointing = set( [('satellite2', 'phenomenon5'), ('satellite1', 'star1'), ] )
rigid.goal_have_image = set( [('planet11', 'image2'), ('star6', 'image1'), ('planet8', 'image0'), ('planet9', 'image3'), ('star7', 'image0'), ('phenomenon5', 'image0'), ('planet10', 'image0'), ] )
state.power_on = set( [] )
state.have_image = set( [] )
state.calibrated = set( [] )

task_list = [('main',)]
