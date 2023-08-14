from ipyhop import Actions

# def drive( state, l1, l2 ):
# 	if all( [ ( l1, ) in state.at, not( ( l1, ) in state.tollarea ), ( l1, l2, ) in state.road, ] ):
# 		state.at.remove( ( l1, ) ); state.at.add( ( l2, ) );
# 		return state

def strike( state, snake, headpos, foodpos ):
    if( all ( [
        ( snake, headpos ) in state.headpos,
        ( foodpos, ) in state.mouse_at,
        ( foodpos, headpos ) in state.adjacent,
        not( headpos == foodpos ),
    ] ) ):
        state.mouse_at.remove( ( foodpos, ) )
        state.head.remove( ( snake, headpos, ) )
        state.connected.add( ( snake, foodpos, headpos ) )
        state.head.add( ( snake, foodpos ) )



actions = Actions()
actions.declare_actions( [ ] )
