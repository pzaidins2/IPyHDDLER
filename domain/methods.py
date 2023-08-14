from ipyhop import Methods

def moveone( state, l1, l2 ):
	yield [ ( 'drive', l1, l2, ), ]

def movemore( state, l1, l3 ):
	for l2 in state.location:
		yield [ ( 'drive', l1, l2, ), ( 'move', l2, l3, ), ]

def movenone( state, l1, l1___1 ):
	if all( [ l1 == l1___1, ] ):
		yield [ ]

def moveoneta( state, l1, l2 ):
	yield [ ( 'driveta', l1, l2, ), ( 'paytoll', l2, ), ]

def movemoreta( state, l1, l3 ):
	for l2 in state.location:
		yield [ ( 'driveta', l1, l2, ), ( 'move', l2, l3, ), ( 'paytoll', l3, ), ]

methods = Methods()
methods.declare_task_methods( 'move', [ movemoreta, movenone, moveone, movemore, moveoneta, ] )
