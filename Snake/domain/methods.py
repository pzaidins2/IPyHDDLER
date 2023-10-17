from ipyhop import Methods
import itertools
import networkx as nx
import numpy as np
import re
from copy import deepcopy

re_y = re.compile("px[0-9]+y([0-9]+)")

def graph_shortest_dist( state, rigid ):

	if "dist_dict" not in vars(rigid).keys():
		# print("Generating graph")
		# add edges
		G = nx.Graph( rigid.adjacent )
		# remove occupied
		connected_nodes = set()
		for _, b, t in state.connected:
			connected_nodes |= { b, t }
		for _, t in state.tail:
			connected_nodes.add(t)
		for _, h in state.head:
			connected_nodes.add(h)
		connected_nodes |= set(map( lambda x: x[ 0 ], state.mouse_at ))
		G.remove_nodes_from( set(map( lambda x: x[ 0 ], state.occupied )) - connected_nodes)
		# print("Calculating all shortest path lengths")
		dist_dict_gen = nx.all_pairs_shortest_path_length(G)
		rigid.dist_dict = dict( dist_dict_gen )
		rigid.G = G
		# track slots so that mice can only move in same slot
		slots = deepcopy( G )
		# remove bottle necks
		bridges = [*nx.bridges(slots)]
		slots.remove_edges_from( bridges )
		rigid.slots = slots
		slot_components = nx.connected_components(slots)
		slot_size = dict()
		for slot_comp in slot_components:
			for slot in slot_comp:
				slot_size[slot] = len(slot_comp)
		rigid.slot_size = slot_size
		rigid.max_slot_size = max( slot_size.values() )
		# # don't let mice block exit to slot
		# bridge_vertex_neighbors = set()
		# for bridge in bridges:
		# 	for v_b in bridge:
		# 		for n_v_b in nx.neighbors(G,v_b):
		# 			for n_n_v_b in nx.neighbors( G, n_v_b ):
		# 				bridge_vertex_neighbors.add(n_n_v_b)
		# print(bridge_vertex_neighbors)
		# slots.remove_nodes_from(bridge_vertex_neighbors)
		rigid.slots = slots

		# print("Path lengths calculated")
	# return length of shortest paths from s_loc to e_loc
	return rigid.dist_dict, rigid.G

# visit in order of 2nd smallest slot to largest with the smallest slot being last
def slot_heuristic( loc, rigid ):
	loc_slot_size = rigid.slot_size[ loc ]
	return loc_slot_size if loc_slot_size > 4 else rigid.max_slot_size + 1
	# match = re_y.match(loc)
	# y = match.group(1)
	# y_int = int(y)
	# if y_int <= 3 and y_int > 0:
	# 	return np.inf
	# else:
	# 	return int(y)

def hunt_all( state, rigid ):
	mouse_at = state.mouse_at
	head = state.head
	# returns point-to-point shortest distance dictionary and graph with only permanent obstacles
	relaxed_dist_dict, relaxed_graph = graph_shortest_dist( state, rigid )
	# print( mouse_at )
	# select snake
	for (snake, snakepos,) in head:
		# get adjacent locations to all mouse location and corresponding mouse locaiton
		mouse_at_loc = {*map(lambda x: x[0], mouse_at)}
		mouse_at_adjacent = []
		for loc in mouse_at_loc:
			for adj_loc in relaxed_graph.neighbors(loc):
				mouse_at_adjacent.append((loc,adj_loc))
		# sort by distance
		mouse_at_adjacent.sort(key=lambda x: relaxed_dist_dict[snakepos][x[1]])
		# sort by slot height
		# sort is stable so we are sorting by slot height with distance as tie breaker
		mouse_at_adjacent.sort(key=lambda x: slot_heuristic(x[0], rigid) )
		# select food and strike location
		for ( foodpos, pos1, ) in mouse_at_adjacent:
			yield [ ( 'move', snake, snakepos, pos1, ), ( 'strike', snake, pos1, foodpos, ), ( 'hunt', ), ]

def hunt_done( state, rigid ):
	mouse_at = state.mouse_at
	# if all( not( ( pos, ) in mouse_at ) for ( pos, ) in itertools.product( location, ) ):
	# faster check for mouse presence than above which is the literal translation from hddl
	if len(mouse_at) == 0:
		yield [ ]

def move_base( state, snake, snakepos, goalpos, rigid ):
	# at location, do nothing
	if ( snakepos == goalpos ):
		yield [ ]

def move_long_snake( state, snake, snakepos, goalpos, rigid ):
	connected = state.connected
	tail = state.tail
	occupied = state.occupied
	# returns point-to-point shortest distance dictionary and graph with only permanent obstacles
	relaxed_dist_dict, relaxed_graph = graph_shortest_dist( state, rigid )
	# get locations adjacent to snake
	adj_loc = [*relaxed_graph.neighbors(snakepos)]
	# filter out occupied locations
	unoccupied_adj_loc = [*filter(lambda x: not( ( x, ) in occupied ), adj_loc )]
	# sort by shortest distance to goal
	unoccupied_adj_loc.sort(key=lambda x:relaxed_dist_dict[x][goalpos] )
	# select immediate move location
	for pos2 in unoccupied_adj_loc:
		# a body part and tail of snake selection
		for  (_, bodypos, tailpos,) in filter( lambda x: x[0] == snake and (snake,x[2]) in tail, connected ):
			yield [ ( 'move_long', snake, pos2, snakepos, bodypos, tailpos, ), ( 'move', snake, pos2, goalpos, ), ]

def move_short_snake( state, snake, snakepos, goalpos, rigid ):
	occupied = state.occupied
	tail = state.tail
	# returns point-to-point shortest distance dictionary and graph with only permanent obstacles
	relaxed_dist_dict, relaxed_graph = graph_shortest_dist( state, rigid )
	# snake with tail must exist
	if ( snake, snakepos, ) in tail:
		# get locations adjacent to snake
		adj_loc = relaxed_graph.neighbors( snakepos )
		# filter out occupied locations
		unoccupied_adj_loc = [ *filter( lambda x: not ((x,) in occupied), adj_loc ) ]
		# sort by shortest distance to goal
		unoccupied_adj_loc.sort( key=lambda x: relaxed_dist_dict[ x ][ goalpos ] )
		# select immediate move location
		for pos2 in unoccupied_adj_loc:
			yield [ ( 'move_short', snake, pos2, snakepos, ), ( 'move', snake, pos2, goalpos, ), ]

methods = Methods()
methods.declare_task_methods( 'hunt', [ hunt_done, hunt_all, ] )
methods.declare_task_methods( 'move', [ move_base,  move_long_snake, move_short_snake, ] )
