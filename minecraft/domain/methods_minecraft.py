from ipyhop import Methods
import itertools
import networkx as nx
import re
import numpy as np
from copy import deepcopy

re_coord = re.compile("l_([0-9]+)_([0-9]+)_([0-9]+)")

def loc_coord( loc ):
	match = re_coord.match( loc )
	coord = ( int( match.group( 1 ) ), int( match.group( 2 ) ), int( match.group( 3 ) ) )
	return np.asarray(coord)

# create static graphs once
def generate_graphs( state, rigid ):
	if "neighbour_graph" not in vars( rigid ).keys():

		# create a graph such that a link exists between all nodes that are neighbors
		# assumptions from observations:
		# if (a,b) is and edge (b,a) is an edge (symmetry)
		# if (a,b) has a direction d then (b,a) has the direction opposite of d and no other edge of form
		# (a,c) has a direction of d
		print( "Generating Graph" )
		neighbour_input = [*map( lambda x: (tuple(x[:2]),x[2]), rigid.neighbour )]
		neighbour_edges, _ = list(zip(*neighbour_input))
		neighbour_direction = { k: v for k, v in neighbour_input }
		neighbour_graph = nx.Graph( neighbour_edges )

		# assign manhattan distance to all mode pairs
		# coordinates are encoded in node names
		dist_dict = dict()
		for loc_0 in rigid.location:
			dist_dict[loc_0] = dict()
			for loc_1 in rigid.location:
				dist_dict[loc_0][loc_1] = abs( np.sum( loc_coord( loc_1 ) - loc_coord( loc_0 ) ) )

		# adjacency in this graph defines what nodes can be influenced by the player from a given node
		# assumptions from observations:
		# if (a,b) is and edge (b,a) is an edge (symmetry)
		reachable_graph = nx.Graph( rigid.reachable)

		# assumption from observation: each node is on top of at most one other node
		on_top_graph = nx.DiGraph( rigid.on_top )

		rigid.neighbour_graph = neighbour_graph
		rigid.dist_dict = dist_dict
		rigid.neighbour_direction = neighbour_direction
		rigid.reachable_graph = reachable_graph
		rigid.on_top_graph = on_top_graph

		print("Graph Generated")

def generate_reachable_dist_dict( state, curr_loc, goal_loc, rigid ):
	# static graph base
	dynamic_neighbour_graph = deepcopy(rigid.neighbour_graph)
	# keep only empty locations (player is empty)
	location = {*rigid.location}
	empty_location = {*map(lambda x: x[0], state.empty)}
	empty_location.add(curr_loc)
	occupied_locations = location - empty_location

	dynamic_neighbour_graph.remove_nodes_from(occupied_locations)

	# reachability graph
	reachable_graph = rigid.reachable_graph
	# get all locations reachable from goal_loc
	reachable_locs = {*nx.neighbors(reachable_graph,goal_loc)}
	# only care about locations in graph
	reachable_locs &= {*dynamic_neighbour_graph.nodes}
	reachable_dist_dict = nx.multi_source_dijkstra_path_length( dynamic_neighbour_graph, reachable_locs )
	return dynamic_neighbour_graph, reachable_dist_dict

def build_house_1( state, loc1, loc2, loc3, loc4, loc5, loc6, len, len2, hgt, t, rigid ):
	# create static graphs
	generate_graphs(state,rigid)
	# build 4 walls,  a door and a roof in order
	yield [ ( 'buildwall', loc1, len, hgt, 'e', t, ), ( 'buildwall', loc2, len2, hgt, 'n', t, ), ( 'buildwall', loc3, len, hgt, 'w', t, ), ( 'buildwall', loc4, len2, hgt, 's', t, ), ( 'builddoor', loc5, ), ( 'buildroof', loc6, len, len2, 'e', 'n', t, ), ]

def build_wall_1( state, loc1, len, hgt, d, t, rigid ):
	# row starting
	if ( hgt, ) in rigid.isone:
		yield [ ( 'buildrow', loc1, len, d, t, ), ]

def build_wall_2( state, loc1, len, hgt, d, t, rigid ):
	on_top_graph = rigid.on_top_graph
	# row continuing
	if not ( hgt, ) in rigid.isone:
		for hgt2 in rigid.numbers:
			if ( hgt, hgt2, ) in rigid.prev:
				for loc2 in nx.neighbors(on_top_graph,loc1):
					yield [ ( 'buildrow', loc1, len, d, t, ), ( 'buildwall', loc2, len, hgt2, d, t, ), ]

def build_roof_1( state, loc1, len, wdt, d, d2, t, rigid ):
	# roof starting
	if ( wdt, ) in rigid.isone:
		yield [ ( 'buildrow', loc1, len, d, t, ), ]

def build_roof_2( state, loc1, len, wdt, d, d2, t, rigid ):
	neighbour_graph = rigid.neighbour_graph
	neighbour_direction = rigid.neighbour_direction
	# roof continuing
	if not( ( wdt, ) in rigid.isone ):
		for wdt2 in rigid.numbers:
			if ( wdt, wdt2, ) in rigid.prev:
				# build row aligned along a direction
				for loc2 in nx.neighbors(neighbour_graph,loc1):
					dn = neighbour_direction[ (loc1, loc2) ]
					if dn == d2:
						yield [ ( 'buildrow', loc1, len, d, t, ), ( 'buildroof', loc2, len, wdt2, d, d2, t, ), ]

def build_door_1( state, loc1, rigid ):
	on_top_graph = rigid.on_top_graph
	# remove block at loc1 and above loc1 to make door
	for loc2 in nx.neighbors(on_top_graph,loc1):
		yield [ ( 'removeblockabstract', loc1, ), ( 'removeblockabstract', loc2, ), ]

def build_row_1( state, loc1, len, d, t, rigid ):
	# start row
	if ( len, ) in rigid.isone:
		yield [ ( 'placeblockabstract', loc1, t, ), ]

def build_row_2( state, loc1, len, d, t, rigid ):
	neighbour_graph = rigid.neighbour_graph
	neighbour_direction = rigid.neighbour_direction
	# continue row
	if not( ( len, ) in rigid.isone ):
		for len2 in rigid.numbers:
			if ( len, len2, ) in rigid.prev:
				# build along single direction
				for loc2 in nx.neighbors( neighbour_graph, loc1 ):
					dn = neighbour_direction[ (loc1, loc2) ]
					if dn == d:
						yield [ ( 'placeblockabstract', loc1, t, ), ( 'buildrow', loc2, len2, d, t, ), ]

def build_row_3( state, loc1, len, d, t, rigid ):
	neighbour_graph = rigid.neighbour_graph
	neighbour_direction = rigid.neighbour_direction
	# end row
	if not( ( len, ) in rigid.isone ):
		for len2 in rigid.numbers:
			if ( len, len2, ) in rigid.prev:
				for loc2 in nx.neighbors(neighbour_graph,loc1):
					dn = neighbour_direction[(loc1,loc2)]
					if dn == d:
						yield [ ( 'buildrow', loc2, len2, d, t, ), ( 'placeblockabstract', loc1, t, ), ]


def place_block_abstract_1( state, loc1, t, rigid ):
	# if player can reach and spot empty
	if ( loc1, ) in state.empty:
		for ( locp, ) in state.player_at:
			if ( locp, loc1, ) in rigid.reachable:
				yield [ ( 'placeblock', loc1, t, ), ]

def place_block_abstract_2( state, loc1, t, rigid ):
	# block of correct type already in spot
	if ( loc1, t, ) in state.blockat:
		yield [ ]

def place_block_abstract_3( state, loc1, t, rigid ):
	# block of wrong type in spot, remove and replace
	for ( locp, ) in state.player_at:
		if ( locp, loc1, ) in rigid.reachable:
			for t2 in rigid.blocktype -{t}:
				if ( loc1, t2, ) in state.blockat:
					yield [ ( 'removeblock', loc1, t2, ), ( 'placeblock', loc1, t, ), ]

def place_block_abstract_4( state, loc1, t, rigid ):
	neighbour_direction = rigid.neighbour_direction
	# player cannot reach loc1, move so they can
	for ( locp, ) in state.player_at:
		neighbour_graph, dist_dict = generate_reachable_dist_dict( state, locp, loc1, rigid )
		# examine graph distance between neighbors of player and loc1
		# try each direction starting with smallest graph distance to any reachable node of goal
		if not( ( locp, loc1, ) in rigid.reachable ):
			locp_neighbors = [*nx.neighbors(neighbour_graph,locp)]
			locp_neighbors = [*filter(lambda x: x in dist_dict.keys(), locp_neighbors)]
			locp_neighbors.sort( key=lambda x: dist_dict[x] )
			for locn in locp_neighbors:
				d = neighbour_direction[(locp,locn)]
				yield [ ( 'findway', locp, loc1, d, ), ( 'placeblockabstract', loc1, t, ), ]

def remove_block_abstract_1( state, loc1, rigid ):
	# removing empty block
	if ( loc1, ) in state.empty:
		yield [ ]

def remove_block_abstract_2( state, loc1, rigid ):
	# remove reachable block
	for ( locp, ) in state.player_at:
		if ( locp, loc1, ) in rigid.reachable:
			for t in rigid.blocktype:
				if ( loc1, t, ) in state.blockat:
					yield [ ( 'removeblock', loc1, t, ), ]

def remove_block_abstract_3( state, loc1, rigid ):
	neighbour_direction = rigid.neighbour_direction
	# remove block not reachable by player, move to reach
	for ( locp, ) in state.player_at:
		neighbour_graph, dist_dict = generate_reachable_dist_dict( state, locp, loc1, rigid )
		if not( ( locp, loc1, ) in rigid.reachable ):
			for t in rigid.blocktype:
				if ( loc1, t, ) in state.blockat:
					# try each direction starting with smallest graph distance to any reachable node of goal
					locp_neighbors = [ *nx.neighbors( neighbour_graph, locp ) ]
					locp_neighbors.sort( key=lambda x: dist_dict[ x ] )
					for locn in locp_neighbors:
						d = neighbour_direction[ (locp, locn) ]
						yield [ ( 'findway', locp, loc1, d, ), ( 'removeblock', loc1, t, ), ]

# experimental for smarter navigation
def find_way( state, locc, locg, d, rigid ):
	# stop
	if ( locc, locg, ) in rigid.reachable:
		for ( locp, ) in state.player_at:
			yield [ ( 'walk', locp, locc, ), ]
	else:
		neighbour_graph, dist_dict = generate_reachable_dist_dict( state, locc, locg, rigid )
		neighbour_direction = rigid.neighbour_direction
		for (locp,) in state.player_at:
			locc_neighbors = [ *nx.neighbors( neighbour_graph, locc ) ]
			locc_neighbors.sort( key=lambda x: dist_dict[ x ] )
			for locn in locc_neighbors:
				if (locn,) in state.empty:
					dn = neighbour_direction[ (locc, locn) ]
					# change dir
					if dn != d:
						yield [ ('walk', locp, locc,), ('findway', locn, locg, dn,), ]
					# same dir
					else:
						yield [ ('findway', locn, locg, d,), ]

def find_way_same_dir( state, locc, locg, d, rigid ):
	neighbour_graph, dist_dict = generate_reachable_dist_dict( state, locc, locg, rigid )
	neighbour_direction = rigid.neighbour_direction
	# continue moving in same direction
	for locn in nx.neighbors(neighbour_graph,locc):
		if ( locn, ) in state.empty:
			dn = neighbour_direction[(locc,locn)]
			if dn == d:
				yield [ ( 'findway', locn, locg, d, ), ]

def find_way_change_dir( state, locc, locg, d, rigid ):
	neighbour_graph, dist_dict = generate_reachable_dist_dict( state, locc, locg, rigid )
	neighbour_direction = rigid.neighbour_direction
	# change driection with preference for shortest graph distance to any reachable node of goal
	for (locp,) in state.player_at:
		locc_neighbors = [*nx.neighbors(neighbour_graph,locc)]
		locc_neighbors.sort(key=lambda x: dist_dict[ x ])
		for locn in locc_neighbors:
			if ( locn, ) in state.empty:
				dn = neighbour_direction[(locc,locn)]
				if dn != d:
					yield [ ( 'walk', locp, locc, ), ( 'findway', locn, locg, dn, ), ]

def find_way_stop( state, locc, locg, d, rigid ):
	# player can now reach stop moving
	if ( locc, locg, ) in rigid.reachable:
		for ( locp, ) in state.player_at:
			yield [ ( 'walk', locp, locc, ), ]

methods = Methods()
methods.declare_task_methods( 'buildhouse', [ build_house_1, ] )
methods.declare_task_methods( 'buildwall', [ build_wall_1, build_wall_2, ] )
methods.declare_task_methods( 'buildroof', [ build_roof_1, build_roof_2, ] )
methods.declare_task_methods( 'builddoor', [ build_door_1, ] )
methods.declare_task_methods( 'buildrow', [  build_row_1, build_row_2, build_row_3, ] )
methods.declare_task_methods( 'placeblockabstract', [ place_block_abstract_1, place_block_abstract_2, place_block_abstract_3, place_block_abstract_4, ] )
methods.declare_task_methods( 'removeblockabstract', [ remove_block_abstract_1, remove_block_abstract_2,  remove_block_abstract_3, ] )
methods.declare_task_methods( 'findway', [ find_way_stop, find_way_same_dir, find_way_change_dir ] )
