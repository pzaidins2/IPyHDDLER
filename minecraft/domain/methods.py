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
		print( "Generating Graph" )
		neighbour_input = [*map( lambda x: (tuple(x[:2]),x[2]), rigid.neighbour )]
		neighbour_edges, _ = list(zip(*neighbour_input))
		neighbour_direction = { k: v for k, v in neighbour_input }
		neighbour_graph = nx.DiGraph( neighbour_edges )
		dist_dict = dict()
		for loc_0 in rigid.location:
			dist_dict[loc_0] = dict()
			for loc_1 in rigid.location:
				dist_dict[loc_0][loc_1] = abs( np.sum( loc_coord( loc_1 ) - loc_coord( loc_0 ) ) )
		reachable_graph = nx.Graph( rigid.reachable)

		on_top_graph = nx.DiGraph( rigid.on_top )

		rigid.neighbour_graph = neighbour_graph
		rigid.dist_dict = dist_dict
		rigid.neighbour_direction = neighbour_direction
		rigid.reachable_graph = reachable_graph
		rigid.on_top_graph = on_top_graph

		print("Graph Generated")

# returns graphs modified
def generate_dynamic_graph( state, rigid ):
	# static graph base
	dynamic_neighbour_graph = deepcopy(rigid.neighbour_graph)
	# keep only empty locations (player is empty)
	location = {*rigid.location}
	empty_location = {*map(lambda x: x[0], state.empty)}
	player_at_location = { *map( lambda x: x[ 0 ], state.player_at ) }
	empty_location |= player_at_location
	occupied_locations = location - empty_location

	dynamic_neighbour_graph.remove_nodes_from(occupied_locations)

	# generate dynamic dist dict
	static_dist_dict = rigid.dist_dict
	max_dist = max(map(lambda x: np.sum(loc_coord(x)), location )) + 1
	dynamic_dist_dict = dict(nx.shortest_path_length(dynamic_neighbour_graph))
	for loc_0 in rigid.location:
		if loc_0 not in dynamic_dist_dict.keys():
			dynamic_dist_dict[loc_0] = dict()
		for loc_1 in rigid.location:
			if loc_1 not in dynamic_dist_dict[loc_0].keys():
				dynamic_dist_dict[ loc_0 ][ loc_1 ] = static_dist_dict[ loc_0 ][ loc_1 ] + max_dist
			if loc_0 == loc_1:
				dynamic_dist_dict[ loc_0 ][ loc_1 ] = 0
	return dynamic_neighbour_graph, dynamic_dist_dict


def build_house_1( state, loc1, loc2, loc3, loc4, loc5, loc6, len, len2, hgt, t, rigid ):
	generate_graphs(state,rigid)
	yield [ ( 'buildwall', loc1, len, hgt, 'e', t, ), ( 'buildwall', loc2, len2, hgt, 'n', t, ), ( 'buildwall', loc3, len, hgt, 'w', t, ), ( 'buildwall', loc4, len2, hgt, 's', t, ), ( 'builddoor', loc5, ), ( 'buildroof', loc6, len, len2, 'e', 'n', t, ), ]

def build_wall_1( state, loc1, len, hgt, d, t, rigid ):
	if ( hgt, ) in rigid.isone:
		yield [ ( 'buildrow', loc1, len, d, t, ), ]

def build_wall_2( state, loc1, len, hgt, d, t, rigid ):
	on_top_graph = rigid.on_top_graph
	if not( ( hgt, ) in rigid.isone ):
		for hgt2 in rigid.numbers:
			if ( hgt, hgt2, ) in rigid.prev:
				for loc2 in nx.neighbors(on_top_graph,loc1):
					yield [ ( 'buildrow', loc1, len, d, t, ), ( 'buildwall', loc2, len, hgt2, d, t, ), ]

def build_roof_1( state, loc1, len, wdt, d, d2, t, rigid ):
	if ( wdt, ) in rigid.isone:
		yield [ ( 'buildrow', loc1, len, d, t, ), ]

def build_roof_2( state, loc1, len, wdt, d, d2, t, rigid ):
	neighbour_graph = rigid.neighbour_graph
	neighbour_direction = rigid.neighbour_direction
	if not( ( wdt, ) in rigid.isone ):
		for loc2 in nx.neighbors(neighbour_graph,loc1):
			dn = neighbour_direction[(loc1,loc2)]
			if dn == d2:
				for wdt2 in rigid.numbers:
					if ( wdt, wdt2, ) in rigid.prev:
						yield [ ( 'buildrow', loc1, len, d, t, ), ( 'buildroof', loc2, len, wdt2, d, d2, t, ), ]

def build_door_1( state, loc1, rigid ):
	on_top_graph = rigid.on_top_graph
	for loc2 in nx.neighbors(on_top_graph,loc1):
		yield [ ( 'removeblockabstract', loc1, ), ( 'removeblockabstract', loc2, ), ]

def build_row_1( state, loc1, len, d, t, rigid ):
	if ( len, ) in rigid.isone:
		yield [ ( 'placeblockabstract', loc1, t, ), ]

def build_row_2( state, loc1, len, d, t, rigid ):
	neighbour_graph = rigid.neighbour_graph
	neighbour_direction = rigid.neighbour_direction
	if not( ( len, ) in rigid.isone ):
		for loc2 in nx.neighbors(neighbour_graph,loc1):
			d2 = neighbour_direction[(loc1,loc2)]
			if d2 == d:
				for len2 in rigid.numbers:
					if ( len, len2, ) in rigid.prev:
						yield [ ( 'placeblockabstract', loc1, t, ), ( 'buildrow', loc2, len2, d, t, ), ]

def build_row_3( state, loc1, len, d, t, rigid ):
	neighbour_graph = rigid.neighbour_graph
	neighbour_direction = rigid.neighbour_direction
	if not( ( len, ) in rigid.isone ):
		prev_len = filter(lambda x: x[0] == len, rigid.prev )
		for ( _, len2, ) in prev_len:
			for loc2 in nx.neighbors( neighbour_graph, loc1 ):
				d2 = neighbour_direction[ (loc1, loc2) ]
				if d2 == d:
					yield [ ( 'buildrow', loc2, len2, d, t, ), ( 'placeblockabstract', loc1, t, ), ]

def place_block_abstract_1( state, loc1, t, rigid ):
	if ( loc1, ) in state.empty:
		for ( locp, ) in state.player_at:
			if ( locp, loc1, ) in rigid.reachable:
				yield [ ( 'placeblock', loc1, t, ), ]

def place_block_abstract_2( state, loc1, t, rigid ):
	if ( loc1, t, ) in state.blockat:
		yield [ ]

def place_block_abstract_3( state, loc1, t, rigid ):
	for ( locp, ) in state.player_at:
		if ( locp, loc1, ) in rigid.reachable:
			for t2 in rigid.blocktype:
				if ( loc1, t2, ) in state.blockat :
					yield [ ( 'removeblock', loc1, t2, ), ( 'placeblock', loc1, t, ), ]

def place_block_abstract_4( state, loc1, t, rigid ):
	neighbour_graph, dist_dict = generate_dynamic_graph(state,rigid)
	neighbour_direction = rigid.neighbour_direction
	for ( locp, ) in state.player_at:
		if not( ( locp, loc1, ) in rigid.reachable ):
			# we are prioritizing direct paths
			locp_neighbour = [*nx.neighbors(neighbour_graph,locp)]
			locp_neighbour.sort( key=lambda x: dist_dict[x][loc1] )
			for locd in locp_neighbour:
				d = neighbour_direction[(locp,locd)]
				yield [ ( 'findway', locp, loc1, d, ), ( 'placeblockabstract', loc1, t, ), ]

def remove_block_abstract_1( state, loc1, rigid ):
	if ( loc1, ) in state.empty:
		yield [ ]

def remove_block_abstract_2( state, loc1, rigid ):
	for ( locp, ) in state.player_at:
		if ( locp, loc1, ) in rigid.reachable:
			for t in rigid.blocktype:
				if ( loc1, t, ) in state.blockat:
					yield [ ( 'removeblock', loc1, t, ), ]

def remove_block_abstract_3( state, loc1, rigid ):
	neighbour_graph, dist_dict = generate_dynamic_graph(state,rigid)
	neighbour_direction = rigid.neighbour_direction
	for ( locp, ) in state.player_at:
		if not ((locp, loc1,) in rigid.reachable):
			for t in rigid.blocktype:
				if ( loc1, t, ) in state.blockat:
					# we are prioritizing direct paths
					locp_neighbour = [ *nx.neighbors( neighbour_graph, locp ) ]
					locp_neighbour.sort( key=lambda x: dist_dict[ x ][ loc1 ] )
					for locd in locp_neighbour:
						d = neighbour_direction[ (locp, locd) ]
						yield [ ( 'findway', locp, loc1, d, ), ( 'removeblock', loc1, t, ), ]

def find_way_same_dir( state, locc, locg, d, rigid ):
	neighbour_graph, dist_dict = generate_dynamic_graph(state,rigid)
	neighbour_direction = rigid.neighbour_direction
	possible_ways = []
	for locn in nx.neighbors( neighbour_graph, locc ):
		dn = neighbour_direction[(locc,locn)]
		if dn == d and ( locn, ) in state.empty:
			possible_ways.append(locn)
	possible_ways.sort(key=lambda x: dist_dict[x][locg])
	for locn in possible_ways:
		yield [ ( 'findway', locn, locg, d, ), ]

def find_way_change_dir( state, locc, locg, d, rigid ):
	neighbour_graph, dist_dict = generate_dynamic_graph(state,rigid)
	neighbour_direction = rigid.neighbour_direction
	possible_ways = []
	for locn in nx.neighbors( neighbour_graph, locc ):
		if ( locn, ) in state.empty:
			dn = neighbour_direction[(locc,locn)]
			if dn != d:
				for (locp,) in state.player_at:
					possible_ways.append( ( locp, locn, dn ) )
	possible_ways.sort( key=lambda x: dist_dict[x[1]][locg])
	for ( locp, locn, dn ) in possible_ways:
		yield [ ( 'walk', locp, locc, ), ( 'findway', locn, locg, dn, ), ]

def find_way_stop( state, locc, locg, d, rigid ):
	if (locc, locg,) in rigid.reachable:
		for ( locp, ) in state.player_at:
			yield [ ( 'walk', locp, locc, ), ]

methods = Methods()
methods.declare_task_methods( 'buildhouse', [ build_house_1, ] )
methods.declare_task_methods( 'buildwall', [ build_wall_1, build_wall_2, ] )
methods.declare_task_methods( 'buildroof', [ build_roof_1, build_roof_2, ] )
methods.declare_task_methods( 'builddoor', [ build_door_1, ] )
methods.declare_task_methods( 'buildrow', [ build_row_1, build_row_2, build_row_3, ] )
methods.declare_task_methods( 'placeblockabstract', [ place_block_abstract_1,  place_block_abstract_2, place_block_abstract_3, place_block_abstract_4, ] )
methods.declare_task_methods( 'removeblockabstract', [ remove_block_abstract_1, remove_block_abstract_2, remove_block_abstract_3,  ] )
methods.declare_task_methods( 'findway', [ find_way_stop, find_way_same_dir, find_way_change_dir, ] )
