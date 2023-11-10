from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'star0', 'phenomenon6', 'spectrograph2', 'groundstation2', 'instrument0', 'star5', 'groundstation1', 'thermograph0', 'satellite0', 'image1', 'phenomenon3', 'phenomenon4'}
rigid.mode = {'image1', 'thermograph0', 'spectrograph2'}
rigid.instrument = {'instrument0'}
rigid.satellite = {'satellite0'}
rigid.direction = {'groundstation1', 'phenomenon3', 'star0', 'phenomenon6', 'groundstation2', 'phenomenon4', 'star5'}
rigid.supports = set( [('instrument0', 'thermograph0'), ] )
rigid.calibration_target = set( [('instrument0', 'groundstation2'), ] )
rigid.on_board = set( [('instrument0', 'satellite0'), ] )
state.power_avail = set( [('satellite0',), ] )
state.pointing = set( [('satellite0', 'phenomenon6'), ] )
rigid.goal_have_image = set( [('phenomenon4', 'thermograph0'), ('star5', 'thermograph0'), ('phenomenon6', 'thermograph0'), ] )
rigid.goal_pointing = set( [] )
state.power_on = set( [] )
state.calibrated = set( [] )
state.have_image = set( [] )

task_list = [('main',)]
