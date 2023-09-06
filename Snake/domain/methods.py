from ipyhop import Methods
import itertools
import networkx as nx
import numpy as np
def graph_shortest_dist( state, rigid ):

	if "dist_dict" not in vars(rigid).keys():
		print("Generating graph")
		# add edges
		G = nx.Graph( rigid.adjacent )
		# remove occupied
		# print(set(filter(lambda x: any(x==l for s, l in state.head | state.tail ) or x == e_loc, rigid.location ) ) )
		# print(G.edges)
		connected_nodes = set()
		for _, b, t in state.connected:
			connected_nodes |= { b, t }
		for _, t in state.tail:
			connected_nodes.add(t)
		for _, h in state.head:
			connected_nodes.add(h)
		connected_nodes |= set(map( lambda x: x[ 0 ], state.mouse_at ))
		G.remove_nodes_from( set(map( lambda x: x[ 0 ], state.occupied )) - connected_nodes)
		print("Calculating all shortest path lengths")
		dist_dict_gen = nx.all_pairs_shortest_path_length(G)
		rigid.dist_dict = dict( dist_dict_gen )
		# for l_0 in rigid.location:
		# 	if l_0 not in rigid.dist_dict.keys():
		# 		rigid.dist_dict[l_0] = dict()
		# 	for l_1 in rigid.location:
		# 		if l_1 not in rigid.dist_dict[l_0].keys():
		# 			rigid.dist_dict[l_0][l_1] = ( 0 if l_0 == l_1 else np.inf )
		rigid.G = G
		print("Path lengths calculated")
	# return length of shortest paths from s_loc to e_loc
	return rigid.dist_dict, rigid.G

def dynamic_graph_shortest_dist_from_to( state, loc_from, loc_to, rigid ):
	G = nx.Graph( rigid.adjacent )
	# remove occupied (except start and end)
	connected_nodes = { loc_to, loc_from }
	G.remove_nodes_from( set( map( lambda x: x[ 0 ], state.occupied ) ) - connected_nodes )
	# shortest path length between from and to
	return nx.shortest_path_length(source=loc_from,target=loc_to)

	

def hunt_all( state, rigid ):
	mouse_at = state.mouse_at
	adjacent = rigid.adjacent
	occupied = state.occupied
	head = state.head
	dist_dict, graph = graph_shortest_dist( state, rigid )
	# print( mouse_at )
	for (snake, snakepos,) in head:
		# dist_dict = graph_shortest_dist_to( state, snakepos, rigid )
		# reachable = set(dist_dict.keys())
		# max_dist = len(adjacent) ** 2
		# print(snakepos)
		mouse_at_loc = {*map(lambda x: x[0], mouse_at)}
		mouse_at_adjacent = []
		for loc in mouse_at_loc:
			for adj_loc in set(graph.neighbors(loc)) - mouse_at_loc:
				mouse_at_adjacent.append((loc,adj_loc))
		mouse_at_adjacent.sort(key=lambda x: dist_dict[snakepos][x[1]])
		for ( foodpos, pos1, ) in mouse_at_adjacent:
			yield [ ( 'move', snake, snakepos, pos1, ), ( 'strike', snake, pos1, foodpos, ), ( 'hunt', ), ]

def hunt_done( state, rigid ):
	mouse_at = state.mouse_at
	# if all( not( ( pos, ) in mouse_at ) for ( pos, ) in itertools.product( location, ) ):
	if len(mouse_at) == 0:
		yield [ ]

def move_base( state, snake, snakepos, goalpos, rigid ):
	if ( snakepos == goalpos ):
		yield [ ]

def move_long_snake( state, snake, snakepos, goalpos, rigid ):
	connected = state.connected
	tail = state.tail
	occupied = state.occupied
	dist_dict, graph = graph_shortest_dist( state, rigid )
	adj_loc = graph.neighbors(snakepos)
	unoccupied_adj_loc = [*filter(lambda x: not( ( x, ) in occupied ), adj_loc )]
	unoccupied_adj_loc.sort(key=lambda x: dist_dict[x][goalpos] )

	for pos2 in unoccupied_adj_loc:
		for  (_, bodypos, tailpos,) in filter( lambda x: x[0] == snake and (snake,x[2]) in tail, connected ):
			yield [ ( 'move_long', snake, pos2, snakepos, bodypos, tailpos, ), ( 'move', snake, pos2, goalpos, ), ]

def move_short_snake( state, snake, snakepos, goalpos, rigid ):
	occupied = state.occupied
	tail = state.tail
	dist_dict, graph = graph_shortest_dist( state, rigid )
	if ( snake, snakepos, ) in tail:
		adj_loc = graph.neighbors( snakepos )
		unoccupied_adj_loc = [ *filter( lambda x: not ((x,) in occupied), adj_loc ) ]
		unoccupied_adj_loc.sort( key=lambda x: dist_dict[ x ][ goalpos ] )

		for pos2 in unoccupied_adj_loc:
			yield [ ( 'move_short', snake, pos2, snakepos, ), ( 'move', snake, pos2, goalpos, ), ]

methods = Methods()
methods.declare_task_methods( 'hunt', [ hunt_done, hunt_all, ] )
methods.declare_task_methods( 'move', [ move_base,  move_long_snake, move_short_snake, ] )
