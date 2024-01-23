from ipyhop import State

from ordered_set import OrderedSet

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = OrderedSet(['instrument0', 'satellite0', 'star0', 'groundstation1', 'groundstation2', 'phenomenon3', 'phenomenon4', 'star5', 'phenomenon6', 'image1', 'spectrograph2', 'thermograph0'])
rigid.satellite = OrderedSet(['satellite0'])
rigid.direction = OrderedSet(['star0', 'groundstation1', 'groundstation2', 'phenomenon3', 'phenomenon4', 'star5', 'phenomenon6'])
rigid.instrument = OrderedSet(['instrument0'])
rigid.mode = OrderedSet(['image1', 'spectrograph2', 'thermograph0'])
rigid.supports = OrderedSet( [('instrument0', 'thermograph0'), ] )
rigid.calibration_target = OrderedSet( [('instrument0', 'groundstation2'), ] )
rigid.on_board = OrderedSet( [('instrument0', 'satellite0'), ] )
state.power_avail = OrderedSet( [('satellite0',), ] )
state.pointing = OrderedSet( [('satellite0', 'phenomenon6'), ] )
rigid.goal_have_image = OrderedSet( [('phenomenon4', 'thermograph0'), ('star5', 'thermograph0'), ('phenomenon6', 'thermograph0'), ] )
state.power_on = OrderedSet( [] )
state.calibrated = OrderedSet( [] )
state.have_image = OrderedSet( [] )
rigid.goal_pointing = OrderedSet( [] )

task_list = [('main',)]
