from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'star7', 'planet11', 'instrument7', 'planet8', 'star3', 'star14', 'star18', 'instrument3', 'instrument8', 'groundstation1', 'thermograph2', 'satellite0', 'instrument2', 'infrared0', 'star4', 'star2', 'star9', 'instrument9', 'instrument6', 'satellite2', 'instrument4', 'planet20', 'infrared3', 'satellite1', 'phenomenon24', 'planet16', 'satellite3', 'infrared1', 'star12', 'phenomenon21', 'phenomenon6', 'star23', 'planet10', 'satellite4', 'star0', 'instrument1', 'instrument5', 'phenomenon13', 'instrument0', 'star22', 'spectrograph4', 'planet5', 'phenomenon17', 'star15', 'star19'}
rigid.mode = {'spectrograph4', 'infrared3', 'infrared0', 'infrared1', 'thermograph2'}
rigid.satellite = {'satellite2', 'satellite1', 'satellite4', 'satellite0', 'satellite3'}
rigid.instrument = {'instrument7', 'instrument9', 'instrument6', 'instrument3', 'instrument8', 'instrument4', 'instrument0', 'instrument2', 'instrument1', 'instrument5'}
rigid.direction = {'star7', 'planet11', 'planet8', 'star3', 'star14', 'star18', 'star12', 'phenomenon21', 'groundstation1', 'phenomenon6', 'star23', 'planet10', 'star4', 'star0', 'star2', 'star9', 'phenomenon13', 'star22', 'planet20', 'planet5', 'phenomenon17', 'phenomenon24', 'star15', 'star19', 'planet16'}
rigid.supports = set( [('instrument4', 'infrared0'), ('instrument1', 'infrared0'), ('instrument2', 'infrared1'), ('instrument3', 'spectrograph4'), ('instrument9', 'infrared3'), ('instrument4', 'infrared3'), ('instrument7', 'infrared1'), ('instrument8', 'spectrograph4'), ('instrument2', 'infrared0'), ('instrument6', 'infrared1'), ('instrument3', 'infrared0'), ('instrument5', 'infrared1'), ('instrument0', 'spectrograph4'), ('instrument0', 'infrared1'), ('instrument8', 'infrared0'), ('instrument9', 'spectrograph4'), ('instrument9', 'infrared1'), ('instrument7', 'infrared3'), ('instrument8', 'infrared3'), ('instrument1', 'infrared1'), ('instrument4', 'thermograph2'), ] )
rigid.calibration_target = set( [('instrument5', 'groundstation1'), ('instrument8', 'star2'), ('instrument6', 'star4'), ('instrument1', 'star2'), ('instrument3', 'star4'), ('instrument4', 'star4'), ('instrument2', 'star3'), ('instrument9', 'star4'), ('instrument0', 'star0'), ('instrument7', 'star2'), ] )
rigid.on_board = set( [('instrument7', 'satellite4'), ('instrument3', 'satellite1'), ('instrument5', 'satellite2'), ('instrument6', 'satellite3'), ('instrument4', 'satellite1'), ('instrument8', 'satellite4'), ('instrument0', 'satellite0'), ('instrument2', 'satellite0'), ('instrument1', 'satellite0'), ('instrument9', 'satellite4'), ] )
state.power_avail = set( [('satellite0',), ('satellite1',), ('satellite2',), ('satellite3',), ('satellite4',), ] )
state.pointing = set( [('satellite4', 'star14'), ('satellite3', 'phenomenon6'), ('satellite0', 'planet16'), ('satellite2', 'star15'), ('satellite1', 'star4'), ] )
rigid.goal_have_image = set( [('star14', 'thermograph2'), ('phenomenon6', 'spectrograph4'), ('star18', 'spectrograph4'), ('star15', 'infrared3'), ('star22', 'infrared1'), ('star19', 'thermograph2'), ('phenomenon21', 'thermograph2'), ('star7', 'infrared0'), ('phenomenon24', 'infrared0'), ('star23', 'spectrograph4'), ('planet16', 'infrared1'), ('planet11', 'infrared3'), ('planet8', 'infrared1'), ('star9', 'spectrograph4'), ('phenomenon13', 'spectrograph4'), ('planet5', 'infrared0'), ('planet10', 'thermograph2'), ('phenomenon17', 'spectrograph4'), ('planet20', 'thermograph2'), ] )
state.have_image = set( [] )
state.calibrated = set( [] )
rigid.goal_pointing = set( [] )
state.power_on = set( [] )

task_list = [('main',)]
