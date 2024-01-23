from ipyhop import State

from ordered_set import OrderedSet

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = OrderedSet(['instrument0', 'instrument1', 'instrument2', 'instrument3', 'instrument4', 'instrument5', 'instrument6', 'instrument7', 'instrument8', 'satellite0', 'satellite1', 'satellite2', 'satellite3', 'satellite4', 'star1', 'star4', 'star0', 'groundstation3', 'star2', 'star5', 'planet6', 'phenomenon7', 'star8', 'phenomenon9', 'star10', 'star11', 'star12', 'planet13', 'planet14', 'phenomenon15', 'planet16', 'star17', 'star18', 'planet19', 'thermograph2', 'image3', 'infrared1', 'spectrograph4', 'infrared0'])
rigid.satellite = OrderedSet(['satellite0', 'satellite1', 'satellite2', 'satellite3', 'satellite4'])
rigid.direction = OrderedSet(['star1', 'star4', 'star0', 'groundstation3', 'star2', 'star5', 'planet6', 'phenomenon7', 'star8', 'phenomenon9', 'star10', 'star11', 'star12', 'planet13', 'planet14', 'phenomenon15', 'planet16', 'star17', 'star18', 'planet19'])
rigid.instrument = OrderedSet(['instrument0', 'instrument1', 'instrument2', 'instrument3', 'instrument4', 'instrument5', 'instrument6', 'instrument7', 'instrument8'])
rigid.mode = OrderedSet(['thermograph2', 'image3', 'infrared1', 'spectrograph4', 'infrared0'])
rigid.supports = OrderedSet( [('instrument0', 'spectrograph4'), ('instrument1', 'infrared0'), ('instrument1', 'infrared1'), ('instrument2', 'infrared1'), ('instrument2', 'infrared0'), ('instrument3', 'spectrograph4'), ('instrument3', 'infrared1'), ('instrument3', 'thermograph2'), ('instrument4', 'infrared1'), ('instrument4', 'image3'), ('instrument4', 'infrared0'), ('instrument5', 'thermograph2'), ('instrument5', 'spectrograph4'), ('instrument6', 'infrared0'), ('instrument7', 'image3'), ('instrument8', 'infrared0'), ('instrument8', 'spectrograph4'), ('instrument8', 'infrared1'), ] )
rigid.calibration_target = OrderedSet( [('instrument0', 'star0'), ('instrument1', 'groundstation3'), ('instrument2', 'star2'), ('instrument3', 'star0'), ('instrument4', 'star2'), ('instrument5', 'star0'), ('instrument6', 'groundstation3'), ('instrument7', 'star2'), ('instrument8', 'star2'), ] )
rigid.on_board = OrderedSet( [('instrument0', 'satellite0'), ('instrument1', 'satellite1'), ('instrument2', 'satellite1'), ('instrument3', 'satellite1'), ('instrument4', 'satellite2'), ('instrument5', 'satellite2'), ('instrument6', 'satellite2'), ('instrument7', 'satellite3'), ('instrument8', 'satellite4'), ] )
state.power_avail = OrderedSet( [('satellite0',), ('satellite1',), ('satellite2',), ('satellite3',), ('satellite4',), ] )
state.pointing = OrderedSet( [('satellite0', 'star8'), ('satellite1', 'groundstation3'), ('satellite2', 'star4'), ('satellite3', 'phenomenon9'), ('satellite4', 'phenomenon9'), ] )
rigid.goal_pointing = OrderedSet( [('satellite0', 'phenomenon9'), ('satellite1', 'star4'), ('satellite4', 'star11'), ] )
rigid.goal_have_image = OrderedSet( [('star5', 'image3'), ('planet6', 'infrared1'), ('phenomenon7', 'infrared1'), ('star8', 'image3'), ('star10', 'thermograph2'), ('star11', 'infrared1'), ('planet13', 'spectrograph4'), ('planet14', 'thermograph2'), ('phenomenon15', 'infrared0'), ('planet16', 'image3'), ('star17', 'infrared0'), ] )
state.power_on = OrderedSet( [] )
state.calibrated = OrderedSet( [] )
state.have_image = OrderedSet( [] )

task_list = [('main',)]
