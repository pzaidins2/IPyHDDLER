from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'satellite2', 'satellite4', 'star9', 'satellite3', 'infrared3', 'star22', 'star7', 'instrument0', 'star18', 'phenomenon21', 'infrared0', 'phenomenon24', 'instrument8', 'phenomenon13', 'planet5', 'star15', 'thermograph2', 'instrument5', 'instrument1', 'planet16', 'planet11', 'planet8', 'instrument9', 'star14', 'instrument6', 'satellite0', 'satellite1', 'star3', 'spectrograph4', 'instrument3', 'instrument2', 'star19', 'star12', 'star0', 'star4', 'phenomenon6', 'planet20', 'groundstation1', 'star2', 'instrument7', 'infrared1', 'planet10', 'instrument4', 'phenomenon17', 'star23'}
rigid.instrument = {'instrument9', 'instrument8', 'instrument7', 'instrument5', 'instrument0', 'instrument6', 'instrument4', 'instrument1', 'instrument3', 'instrument2'}
rigid.direction = {'star9', 'star14', 'star22', 'star7', 'phenomenon17', 'star18', 'star3', 'phenomenon21', 'star19', 'phenomenon24', 'star12', 'star0', 'star4', 'phenomenon6', 'planet20', 'groundstation1', 'phenomenon13', 'star2', 'planet10', 'planet5', 'star23', 'star15', 'planet16', 'planet11', 'planet8'}
rigid.mode = {'infrared3', 'thermograph2', 'infrared0', 'spectrograph4', 'infrared1'}
rigid.satellite = {'satellite2', 'satellite0', 'satellite4', 'satellite3', 'satellite1'}
rigid.supports = set( [('instrument7', 'infrared1'), ('instrument4', 'thermograph2'), ('instrument3', 'infrared0'), ('instrument3', 'spectrograph4'), ('instrument2', 'infrared0'), ('instrument8', 'infrared3'), ('instrument0', 'spectrograph4'), ('instrument2', 'infrared1'), ('instrument0', 'infrared1'), ('instrument5', 'infrared1'), ('instrument8', 'spectrograph4'), ('instrument4', 'infrared3'), ('instrument8', 'infrared0'), ('instrument9', 'infrared3'), ('instrument4', 'infrared0'), ('instrument9', 'spectrograph4'), ('instrument7', 'infrared3'), ('instrument6', 'infrared1'), ('instrument9', 'infrared1'), ('instrument1', 'infrared0'), ('instrument1', 'infrared1'), ] )
rigid.calibration_target = set( [('instrument4', 'star4'), ('instrument8', 'star2'), ('instrument3', 'star4'), ('instrument2', 'star3'), ('instrument5', 'groundstation1'), ('instrument1', 'star2'), ('instrument0', 'star0'), ('instrument7', 'star2'), ('instrument6', 'star4'), ('instrument9', 'star4'), ] )
rigid.on_board = set( [('instrument8', 'satellite4'), ('instrument5', 'satellite2'), ('instrument4', 'satellite1'), ('instrument3', 'satellite1'), ('instrument6', 'satellite3'), ('instrument7', 'satellite4'), ('instrument9', 'satellite4'), ('instrument1', 'satellite0'), ('instrument2', 'satellite0'), ('instrument0', 'satellite0'), ] )
state.power_avail = set( [('satellite3',), ('satellite4',), ('satellite1',), ('satellite2',), ('satellite0',), ] )
state.pointing = set( [('satellite2', 'star15'), ('satellite1', 'star4'), ('satellite4', 'star14'), ('satellite3', 'phenomenon6'), ('satellite0', 'planet16'), ] )
rigid.goal_have_image = set( [('star7', 'infrared0'), ('planet20', 'thermograph2'), ('star23', 'spectrograph4'), ('star14', 'thermograph2'), ('star15', 'infrared3'), ('planet8', 'infrared1'), ('star9', 'spectrograph4'), ('phenomenon24', 'infrared0'), ('phenomenon6', 'spectrograph4'), ('star22', 'infrared1'), ('planet16', 'infrared1'), ('planet10', 'thermograph2'), ('star19', 'thermograph2'), ('phenomenon17', 'spectrograph4'), ('star18', 'spectrograph4'), ('planet11', 'infrared3'), ('planet5', 'infrared0'), ('phenomenon21', 'thermograph2'), ('phenomenon13', 'spectrograph4'), ] )
rigid.goal_pointing = set( [] )
state.power_on = set( [] )
state.have_image = set( [] )
state.calibrated = set( [] )

task_list = [('main',)]
