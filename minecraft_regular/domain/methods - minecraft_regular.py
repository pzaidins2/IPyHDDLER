from ipyhop import Methods
import itertools

def build_house_1( state, loc1, loc2, loc3, loc4, loc5, loc6, len, len2, hgt, t, rigid ):
	yield [ ( 'buildwall', loc1, len, hgt, 'e', t, ), ( 'buildwall', loc2, len2, hgt, 'n', t, ), ( 'buildwall', loc3, len, hgt, 'w', t, ), ( 'buildwall', loc4, len2, hgt, 's', t, ), ( 'builddoor', loc5, ), ( 'buildroof', loc6, len, len2, 'e', 'n', t, ), ]

def build_wall_1( state, loc1, len, hgt, d, t, rigid ):
	if ( hgt, ) in rigid.isone:
		yield [ ( 'buildrow', loc1, len, d, t, ), ]

def build_wall_2( state, loc1, len, hgt, d, t, rigid ):
	if not( ( hgt, ) in rigid.isone ):
		for hgt2 in rigid.numbers:
			if ( hgt, hgt2, ) in rigid.prev:
				for loc2 in rigid.location:
					if ( loc1, loc2, ) in rigid.on_top:
						yield [ ( 'buildrow', loc1, len, d, t, ), ( 'buildwall', loc2, len, hgt2, d, t, ), ]

def build_roof_1( state, loc1, len, wdt, d, d2, t, rigid ):
	if ( wdt, ) in rigid.isone:
		yield [ ( 'buildrow', loc1, len, d, t, ), ]

def build_roof_2( state, loc1, len, wdt, d, d2, t, rigid ):
	if not( ( wdt, ) in rigid.isone ):
		for wdt2 in rigid.numbers:
			if ( wdt, wdt2, ) in rigid.prev:
				for loc2 in rigid.location:
					if (loc1, loc2, d2,) in rigid.neighbour:
						yield [ ( 'buildrow', loc1, len, d, t, ), ( 'buildroof', loc2, len, wdt2, d, d2, t, ), ]

def build_door_1( state, loc1, rigid ):
	for loc2 in rigid.location:
		if ( loc1, loc2, ) in rigid.on_top:
			yield [ ( 'removeblockabstract', loc1, ), ( 'removeblockabstract', loc2, ), ]

def build_row_1( state, loc1, len, d, t, rigid ):
	if ( len, ) in rigid.isone:
		yield [ ( 'placeblockabstract', loc1, t, ), ]

def build_row_2( state, loc1, len, d, t, rigid ):
	if not( ( len, ) in rigid.isone ):
		for len2 in rigid.numbers:
			if ( len, len2, ) in rigid.prev:
				for loc2 in rigid.location:
					if ( loc1, loc2, d, ) in rigid.neighbour:
						yield [ ( 'placeblockabstract', loc1, t, ), ( 'buildrow', loc2, len2, d, t, ), ]

def build_row_3( state, loc1, len, d, t, rigid ):
	if not( ( len, ) in rigid.isone ):
		for len2 in rigid.numbers:
			if ( len, len2, ) in rigid.prev:
				for loc2 in rigid.location:
					if ( loc1, loc2, d, ) in rigid.neighbour:
						yield [ ( 'buildrow', loc2, len2, d, t, ), ( 'placeblockabstract', loc1, t, ), ]

def place_block_abstract_1( state, loc1, t, rigid ):
	if ( loc1, ) in state.empty:
		yield [ ( 'placeblock', loc1, t, ), ]

def place_block_abstract_2( state, loc1, t, rigid ):
	if ( loc1, t, ) in state.blockat:
		yield [ ]

def place_block_abstract_3( state, loc1, t, rigid ):
	for t2 in rigid.blocktype:
		if ( loc1, t2, ) in state.blockat:
			yield [ ( 'removeblock', loc1, t2, ), ( 'placeblock', loc1, t, ), ]

def remove_block_abstract_1( state, loc1, rigid ):
	if ( loc1, ) in state.empty:
		yield [ ]

def remove_block_abstract_2( state, loc1, rigid ):
	for t in rigid.blocktype:
		if ( loc1, t, ) in state.blockat:
			yield [ ( 'removeblock', loc1, t, ), ]

methods = Methods()
methods.declare_task_methods( 'buildhouse', [ build_house_1, ] )
methods.declare_task_methods( 'buildwall', [ build_wall_1, build_wall_2, ] )
methods.declare_task_methods( 'buildroof', [ build_roof_2, build_roof_1, ] )
methods.declare_task_methods( 'builddoor', [ build_door_1, ] )
methods.declare_task_methods( 'buildrow', [ build_row_2, build_row_3, build_row_1, ] )
methods.declare_task_methods( 'placeblockabstract', [ place_block_abstract_3, place_block_abstract_1, place_block_abstract_2, ] )
methods.declare_task_methods( 'removeblockabstract', [ remove_block_abstract_2, remove_block_abstract_1, ] )
