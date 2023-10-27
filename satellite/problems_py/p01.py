from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.satellite = {'satellite0'}
rigid.instrument = {'instrument0'}
rigid.mode = {'spectrograph2', 'image1', 'thermograph0'}
rigid.direction = {'groundstation1', 'groundstation2', 'phenomenon6', 'phenomenon4', 'star0', 'phenomenon3', 'star5'}
rigid.supports = set( [('instrument0', 'thermograph0'), ] )
rigid.calibration_target = set( [('instrument0', 'groundstation2'), ] )
rigid.on_board = set( [('instrument0', 'satellite0'), ] )
state.power_avail = set( [('satellite0',), ] )
state.pointing = set( [('satellite0', 'phenomenon6'), ] )
rigid.goal_have_image = set( [('star5', 'thermograph0'), ('phenomenon6', 'thermograph0'), ('phenomenon4', 'thermograph0'), ] )
rigid.goal_pointing = set( [] )
state.calibrated = set( [] )
state.have_image = set( [] )
state.power_on = set( [] )

task_list = [('main',)]
