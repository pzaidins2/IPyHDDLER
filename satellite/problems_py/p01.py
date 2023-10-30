from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'star5', 'instrument0', 'image1', 'star0', 'spectrograph2', 'satellite0', 'phenomenon3', 'groundstation1', 'phenomenon4', 'phenomenon6', 'thermograph0', 'groundstation2'}
rigid.direction = {'star5', 'phenomenon3', 'groundstation1', 'phenomenon4', 'phenomenon6', 'star0', 'groundstation2'}
rigid.mode = {'image1', 'thermograph0', 'spectrograph2'}
rigid.instrument = {'instrument0'}
rigid.satellite = {'satellite0'}
rigid.supports = set( [('instrument0', 'thermograph0'), ] )
rigid.calibration_target = set( [('instrument0', 'groundstation2'), ] )
rigid.on_board = set( [('instrument0', 'satellite0'), ] )
state.power_avail = set( [('satellite0',), ] )
state.pointing = set( [('satellite0', 'phenomenon6'), ] )
rigid.goal_have_image = set( [('phenomenon4', 'thermograph0'), ('phenomenon6', 'thermograph0'), ('star5', 'thermograph0'), ] )
state.calibrated = set( [] )
rigid.goal_pointing = set( [] )
state.power_on = set( [] )
state.have_image = set( [] )

task_list = [('main',)]
