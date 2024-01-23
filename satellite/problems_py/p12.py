from ipyhop import State

from ordered_set import OrderedSet

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = OrderedSet(['instrument0', 'instrument1', 'instrument2', 'instrument3', 'instrument4', 'instrument5', 'instrument6', 'instrument7', 'instrument8', 'instrument9', 'satellite0', 'satellite1', 'satellite2', 'satellite3', 'satellite4', 'star0', 'star3', 'groundstation1', 'star2', 'star4', 'planet5', 'phenomenon6', 'star7', 'planet8', 'star9', 'planet10', 'planet11', 'star12', 'phenomenon13', 'star14', 'star15', 'planet16', 'phenomenon17', 'star18', 'star19', 'planet20', 'phenomenon21', 'star22', 'star23', 'phenomenon24', 'thermograph2', 'infrared0', 'infrared1', 'spectrograph4', 'infrared3'])
rigid.satellite = OrderedSet(['satellite0', 'satellite1', 'satellite2', 'satellite3', 'satellite4'])
rigid.direction = OrderedSet(['star0', 'star3', 'groundstation1', 'star2', 'star4', 'planet5', 'phenomenon6', 'star7', 'planet8', 'star9', 'planet10', 'planet11', 'star12', 'phenomenon13', 'star14', 'star15', 'planet16', 'phenomenon17', 'star18', 'star19', 'planet20', 'phenomenon21', 'star22', 'star23', 'phenomenon24'])
rigid.instrument = OrderedSet(['instrument0', 'instrument1', 'instrument2', 'instrument3', 'instrument4', 'instrument5', 'instrument6', 'instrument7', 'instrument8', 'instrument9'])
rigid.mode = OrderedSet(['thermograph2', 'infrared0', 'infrared1', 'spectrograph4', 'infrared3'])
rigid.supports = OrderedSet( [('instrument0', 'infrared1'), ('instrument0', 'spectrograph4'), ('instrument1', 'infrared1'), ('instrument1', 'infrared0'), ('instrument2', 'infrared1'), ('instrument2', 'infrared0'), ('instrument3', 'infrared0'), ('instrument3', 'spectrograph4'), ('instrument4', 'infrared0'), ('instrument4', 'infrared3'), ('instrument4', 'thermograph2'), ('instrument5', 'infrared1'), ('instrument6', 'infrared1'), ('instrument7', 'infrared1'), ('instrument7', 'infrared3'), ('instrument8', 'infrared0'), ('instrument8', 'infrared3'), ('instrument8', 'spectrograph4'), ('instrument9', 'infrared3'), ('instrument9', 'spectrograph4'), ('instrument9', 'infrared1'), ] )
rigid.calibration_target = OrderedSet( [('instrument0', 'star0'), ('instrument1', 'star2'), ('instrument2', 'star3'), ('instrument3', 'star4'), ('instrument4', 'star4'), ('instrument5', 'groundstation1'), ('instrument6', 'star4'), ('instrument7', 'star2'), ('instrument8', 'star2'), ('instrument9', 'star4'), ] )
rigid.on_board = OrderedSet( [('instrument0', 'satellite0'), ('instrument1', 'satellite0'), ('instrument2', 'satellite0'), ('instrument3', 'satellite1'), ('instrument4', 'satellite1'), ('instrument5', 'satellite2'), ('instrument6', 'satellite3'), ('instrument7', 'satellite4'), ('instrument8', 'satellite4'), ('instrument9', 'satellite4'), ] )
state.power_avail = OrderedSet( [('satellite0',), ('satellite1',), ('satellite2',), ('satellite3',), ('satellite4',), ] )
state.pointing = OrderedSet( [('satellite0', 'planet16'), ('satellite1', 'star4'), ('satellite2', 'star15'), ('satellite3', 'phenomenon6'), ('satellite4', 'star14'), ] )
rigid.goal_have_image = OrderedSet( [('planet5', 'infrared0'), ('phenomenon6', 'spectrograph4'), ('star7', 'infrared0'), ('planet8', 'infrared1'), ('star9', 'spectrograph4'), ('planet10', 'thermograph2'), ('planet11', 'infrared3'), ('phenomenon13', 'spectrograph4'), ('star14', 'thermograph2'), ('star15', 'infrared3'), ('planet16', 'infrared1'), ('phenomenon17', 'spectrograph4'), ('star18', 'spectrograph4'), ('star19', 'thermograph2'), ('planet20', 'thermograph2'), ('phenomenon21', 'thermograph2'), ('star22', 'infrared1'), ('star23', 'spectrograph4'), ('phenomenon24', 'infrared0'), ] )
state.power_on = OrderedSet( [] )
state.calibrated = OrderedSet( [] )
state.have_image = OrderedSet( [] )
rigid.goal_pointing = OrderedSet( [] )

task_list = [('main',)]
