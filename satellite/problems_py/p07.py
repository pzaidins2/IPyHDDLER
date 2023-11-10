from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'star6', 'instrument2', 'planet11', 'image2', 'instrument7', 'image1', 'star7', 'planet8', 'star3', 'star1', 'instrument4', 'instrument3', 'groundstation0', 'groundstation2', 'image0', 'planet9', 'satellite0', 'instrument0', 'planet10', 'groundstation4', 'phenomenon5', 'satellite2', 'satellite3', 'instrument5', 'instrument6', 'satellite1', 'image3', 'instrument1'}
rigid.direction = {'star6', 'groundstation4', 'phenomenon5', 'planet11', 'star7', 'planet8', 'star3', 'star1', 'groundstation0', 'groundstation2', 'planet9', 'planet10'}
rigid.satellite = {'satellite2', 'satellite0', 'satellite3', 'satellite1'}
rigid.mode = {'image0', 'image3', 'image2', 'image1'}
rigid.instrument = {'instrument2', 'instrument7', 'instrument4', 'instrument5', 'instrument3', 'instrument6', 'instrument1', 'instrument0'}
rigid.supports = set( [('instrument6', 'image2'), ('instrument2', 'image0'), ('instrument5', 'image1'), ('instrument7', 'image3'), ('instrument6', 'image1'), ('instrument7', 'image0'), ('instrument0', 'image1'), ('instrument5', 'image0'), ('instrument1', 'image3'), ('instrument4', 'image1'), ('instrument6', 'image0'), ('instrument3', 'image2'), ('instrument4', 'image0'), ('instrument0', 'image3'), ('instrument7', 'image1'), ('instrument3', 'image0'), ('instrument5', 'image2'), ] )
rigid.calibration_target = set( [('instrument3', 'groundstation4'), ('instrument1', 'groundstation0'), ('instrument2', 'groundstation2'), ('instrument6', 'groundstation4'), ('instrument5', 'star1'), ('instrument4', 'star1'), ('instrument0', 'star1'), ('instrument7', 'groundstation0'), ] )
rigid.on_board = set( [('instrument3', 'satellite1'), ('instrument4', 'satellite2'), ('instrument2', 'satellite0'), ('instrument7', 'satellite3'), ('instrument1', 'satellite0'), ('instrument0', 'satellite0'), ('instrument6', 'satellite3'), ('instrument5', 'satellite2'), ] )
state.power_avail = set( [('satellite2',), ('satellite0',), ('satellite1',), ('satellite3',), ] )
state.pointing = set( [('satellite2', 'star6'), ('satellite1', 'groundstation0'), ('satellite3', 'groundstation2'), ('satellite0', 'star6'), ] )
rigid.goal_pointing = set( [('satellite1', 'star1'), ('satellite2', 'phenomenon5'), ] )
rigid.goal_have_image = set( [('star6', 'image1'), ('planet9', 'image3'), ('phenomenon5', 'image0'), ('planet11', 'image2'), ('planet10', 'image0'), ('planet8', 'image0'), ('star7', 'image0'), ] )
state.calibrated = set( [] )
state.have_image = set( [] )
state.power_on = set( [] )

task_list = [('main',)]
