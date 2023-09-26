from ipyhop import Methods
import itertools

def build_house_1( state, loc1, loc2, loc3, loc4, loc5, loc6, len, len2, hgt, t, rigid ):
	yield [ ( 'buildwall', loc1, len, hgt, 'e', t, ), ( 'buildwall', loc2, len2, hgt, 'n', t, ), ( 'buildwall', loc3, len, hgt, 'w', t, ), ( 'buildwall', loc4, len2, hgt, 's', t, ), ( 'builddoor', loc5, ), ( 'buildroof', loc6, len, len2, 'e', 'n', t, ), ]

def build_wall_1( state, loc1, len, hgt, d, t, rigid ):
	if all( [ ( hgt, ) in rigid.isone, ] ):
		yield [ ( 'buildrow', loc1, len, d, t, ), ]

def build_wall_2( state, loc1, len, hgt, d, t, rigid ):
	for hgt2 in rigid.numbers:
		for loc2 in rigid.location:
			print( loc1, loc2 )
			if all( [ not( ( hgt, ) in rigid.isone ), ( hgt, hgt2, ) in rigid.prev, ( loc1, loc2, ) in rigid.on_top, ] ):
				yield [ ( 'buildrow', loc1, len, d, t, ), ( 'buildwall', loc2, len, hgt2, d, t, ), ]

def build_roof_1( state, loc1, len, wdt, d, d2, t, rigid ):
	if all( [ ( wdt, ) in rigid.isone, ] ):
		yield [ ( 'buildrow', loc1, len, d, t, ), ]

def build_roof_2( state, loc1, len, wdt, d, d2, t, rigid ):
	for loc2 in rigid.location:
		for wdt2 in rigid.numbers:
			if all( [ not( ( wdt, ) in rigid.isone ), ( wdt, wdt2, ) in rigid.prev, ( loc1, loc2, d2, ) in rigid.neighbour, ] ):
				yield [ ( 'buildrow', loc1, len, d, t, ), ( 'buildroof', loc2, len, wdt2, d, d2, t, ), ]

def build_door_1( state, loc1, rigid ):
	for loc2 in rigid.location:
		if all( [ ( loc1, loc2, ) in rigid.on_top, ] ):
			yield [ ( 'removeblockabstract', loc1, ), ( 'removeblockabstract', loc2, ), ]

def build_row_1( state, loc1, len, d, t, rigid ):
	if all( [ ( len, ) in rigid.isone, ] ):
		yield [ ( 'placeblockabstract', loc1, t, ), ]

def build_row_2( state, loc1, len, d, t, rigid ):
	for len2 in rigid.numbers:
		for loc2 in rigid.location:
			if all( [ not( ( len, ) in rigid.isone ), ( len, len2, ) in rigid.prev, ( loc1, loc2, d, ) in rigid.neighbour, ] ):
				yield [ ( 'placeblockabstract', loc1, t, ), ( 'buildrow', loc2, len2, d, t, ), ]

def build_row_3( state, loc1, len, d, t, rigid ):
	for len2 in rigid.numbers:
		for loc2 in rigid.location:
			if all( [ not( ( len, ) in rigid.isone ), ( len, len2, ) in rigid.prev, ( loc1, loc2, d, ) in rigid.neighbour, ] ):
				yield [ ( 'buildrow', loc2, len2, d, t, ), ( 'placeblockabstract', loc1, t, ), ]

def place_block_abstract_1( state, loc1, t, rigid ):
	for locp in rigid.location:
		if all( [ ( loc1, ) in state.empty, ( locp, loc1, ) in rigid.reachable, ( locp, ) in state.player_at, ] ):
			yield [ ( 'placeblock', loc1, t, ), ]

def place_block_abstract_2( state, loc1, t, rigid ):
	if all( [ ( loc1, t, ) in state.blockat, ] ):
		yield [ ]

def place_block_abstract_3( state, loc1, t, rigid ):
	for locp in rigid.location:
		for t2 in rigid.blocktype:
			if all( [ ( loc1, t2, ) in state.blockat, ( locp, loc1, ) in rigid.reachable, ( locp, ) in state.player_at, ] ):
				yield [ ( 'removeblock', loc1, t2, ), ( 'placeblock', loc1, t, ), ]

def place_block_abstract_4( state, loc1, t, rigid ):
	for d in rigid.direction:
		for locp in rigid.location:
			if all( [ not( ( locp, loc1, ) in rigid.reachable ), ( locp, ) in state.player_at, ] ):
				yield [ ( 'findway', locp, loc1, d, ), ( 'placeblockabstract', loc1, t, ), ]

def remove_block_abstract_1( state, loc1, rigid ):
	if all( [ ( loc1, ) in state.empty, ] ):
		yield [ ]

def remove_block_abstract_2( state, loc1, rigid ):
	for locp in rigid.location:
		for t in rigid.blocktype:
			if all( [ ( loc1, t, ) in state.blockat, ( locp, loc1, ) in rigid.reachable, ( locp, ) in state.player_at, ] ):
				yield [ ( 'removeblock', loc1, t, ), ]

def remove_block_abstract_3( state, loc1, rigid ):
	for d in rigid.direction:
		for locp in rigid.location:
			for t in rigid.blocktype:
				if all( [ ( loc1, t, ) in state.blockat, not( ( locp, loc1, ) in rigid.reachable ), ( locp, ) in state.player_at, ] ):
					yield [ ( 'findway', locp, loc1, d, ), ( 'removeblock', loc1, t, ), ]

def find_way_same_dir( state, locc, locg, d, rigid ):
	for locn in rigid.location:
		if all( [ ( locn, ) in state.empty, ( locc, locn, d, ) in rigid.neighbour, ] ):
			yield [ ( 'findway', locn, locg, d, ), ]

def find_way_change_dir( state, locc, locg, d, rigid ):
	for dn in rigid.direction:
		for locn in rigid.location:
			for locp in rigid.location:
				if all( [ ( locn, ) in state.empty, ( locc, locn, dn, ) in rigid.neighbour, not( ( locc, locn, d, ) in rigid.neighbour ), ( locp, ) in state.player_at, ] ):
					yield [ ( 'walk', locp, locc, ), ( 'findway', locn, locg, dn, ), ]

def find_way_stop( state, locc, locg, d, rigid ):
	for locp in rigid.location:
		if all( [ ( locc, locg, ) in rigid.reachable, ( locp, ) in state.player_at, ] ):
			yield [ ( 'walk', locp, locc, ), ]

methods = Methods()
methods.declare_task_methods( 'buildhouse', [ build_house_1, ] )
methods.declare_task_methods( 'buildwall', [ build_wall_1, build_wall_2, ] )
methods.declare_task_methods( 'buildroof', [ build_roof_2, build_roof_1, ] )
methods.declare_task_methods( 'builddoor', [ build_door_1, ] )
methods.declare_task_methods( 'buildrow', [ build_row_3, build_row_1, build_row_2, ] )
methods.declare_task_methods( 'placeblockabstract', [ place_block_abstract_1, place_block_abstract_4, place_block_abstract_2, place_block_abstract_3, ] )
methods.declare_task_methods( 'removeblockabstract', [ remove_block_abstract_2, remove_block_abstract_3, remove_block_abstract_1, ] )
methods.declare_task_methods( 'findway', [ find_way_stop, find_way_same_dir, find_way_change_dir, ] )
