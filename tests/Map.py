import unittest

from hexmap.Map import Map, Grid, MapUnit

class TestMap( unittest.TestCase ):
	def setUp( self ):
		pass

	def test_size( self ):
		sizes = [ ( 1, 1 ), ( 2, 2 ), ( 3, 4 ), ( 5, 5 ), ( 10, 8 ) ]

		for rows, cols in sizes:
			m = Map( ( rows, cols ) )
			size = m.size
			self.assertTrue( rows == size[0],
				"Map %s returned %s rows, expected %s." % ( m, size[0], rows ) )

			self.assertTrue( cols == size[1],
				"Map %s returned %s rows, expected %s." % ( m, size[1], cols ) )

	def test_distance( self ):
		rows, cols = ( 8, 8 )
		tests = [
			( ( 0, 0 ), ( 1, 0 ), 1 ),
			( ( 0, 0 ), ( 1, 1 ), 1 ),
			( ( 0, 0 ), ( 1, 2 ), 2 ),
			( ( 5, 3 ), ( 9, 5 ), 4 ),
			( ( 9, 5 ), ( 5, 3 ), 4 ),
			( ( 7, 4 ), ( 3, 2 ), 4 ),
		]

		m = Map( ( rows, cols ) )

		for start, end, distance in tests:
			d = m.distance( start, end )
			self.assertTrue( distance == d,
				"Distance between %s, %s, expected to be %s, got %s"
				% ( start, end, distance, d ) )

	def test_direction( self ):
		rows, cols = ( 8, 8 )
		m = Map( ( rows, cols ) )

		# Test dominated directions
		tests = [
			( ( 0, 0 ), ( 1, 0 ), ( 1, 0 ) ),
			( ( 0, 0 ), ( 1, 1 ), ( 1, 1 ) ),
			( ( 0, 0 ), ( 0, 1 ), ( 0, 1 ) ),
			( ( 0, 1 ), ( 0, 0 ), ( 0, -1 ) ),
			( ( 1, 1 ), ( 0, 0 ), ( -1, -1 ) ),
			( ( 1, 0 ), ( 0, 0 ), ( -1, 0 ) ),

			( ( 0, 0 ), ( 3, 1 ), ( 1, 0 ) ),
			( ( 5, 3 ), ( 8, 5 ), ( 1, 1 ) ),
			( ( 8, 5 ), ( 5, 3 ), ( -1, -1 ) ),
		]

		for start, end, direction in tests:
			d = m.direction( start, end )
			self.assertTrue( direction == d,
				"Direction between %s, %s, expected to be %s, got %s"
				% ( start, end, direction, d ) )

		# Test directions with a random component
		tests = [
			( ( 0, 0 ), ( 2, 1 ), [ ( 1, 0 ), ( 1, 1 ) ] ),
			( ( 2, 2 ), ( 3, 4 ), [ ( 0, 1 ), ( 1, 1 ) ] ),
			( ( 5, 4 ), ( 6, 3 ), [ ( 1, 0 ), ( 0, -1 ) ] ),
			( ( 6, 3 ), ( 5, 4 ), [ ( -1, 0 ), ( 0, 1 ) ] ),
		]

		for start, end, directions in tests:
			d = m.direction( start, end )
			self.assertTrue( d in directions,
				"Direction between %s, %s, expected to be in %s, got %s"
				% ( start, end, directions, d ) )

	def test_neighbors( self ):
		tests = {
			( 0, 0 ) : [ ( 1, 0 ), ( 1, 1 ) ],
			( 1, 2 ) : [ ( 1, 1 ), ( 2, 2 ), ( 2, 3 ) ],
			( 1, 1 ) : [ ( 0, 0 ), ( 1, 0 ), ( 2, 1 ), ( 2, 2 ), ( 1, 2 ) ],
			( 2, 1 ) : [ ( 1, 1 ), ( 1, 0 ), ( 2, 0 ), ( 3, 1 ), ( 3, 2 ), ( 2, 2 ) ],
			( 7, 0 ) : [ ( 6, 0 ), ( 7, 1 ), ( 8, 1 ) ],
			( 8, 1 ) : [ ( 7, 0 ), ( 7, 1 ), ( 8, 2 ) ],
			( 3, 6 ) : [ ( 3, 5 ), ( 4, 6 ), ( 4, 7 ) ],
			( 4, 7 ) : [ ( 3, 6 ), ( 4, 6 ), ( 5, 7 ) ],
			( 9, 4 ) : [ ( 9, 3 ), ( 8, 3 ), ( 8, 4 ), ( 9, 5 ), ( 10, 5 ) ],
			( 11, 7 ): [ ( 10, 6 ), ( 10, 7 ) ]
		}

		m = Map( ( 8, 8 ) )
		for node, results in tests.items():
			neighbors = m.neighbors( node )
			self.assertEqual( set( neighbors ), set( results ),
				"Got incorrect neighbors for node %s:\n Expected: %s\nReceived: %s"
				% ( node, results, neighbors ) )

	def test_spread( self ):
		raise NotImplementedError

	def test_cone( self ):
		raise NotImplementedError

	def test_slice( self ):
		raise NotImplementedError

	def test_line( self ):
		raise NotImplementedError

class TestGrid( unittest.TestCase ):
	def setUp( self ):
		self.grid = Grid()

	def test_assignment( self ):
		key, value = ( 0, 0 ), "U"
		self.grid[ key ] = value
		self.assertTrue( key in self.grid,
			"Failed to create key %s" % str( key ) )
		self.assertTrue( value == self.grid[ key ],
			"Key %s does not return value %s" % ( key, value ) )

	def test_find( self ):
		key, value = ( 0, 0 ), "U"
		self.grid[ key ] = value
		self.assertTrue( key == self.grid.find( value ),
			 "Find %s did not correctly return key %s " % ( value, key ) )

class TestMapUnit( unittest.TestCase ):

	class TestUnit( MapUnit ):
		def paint( self, surface ):
			pass

	def setUp( self ):
		self.map = Map( ( 5, 5 ) )
		self.map.units = Grid()

	def test_position_succeeds( self ):
		pos, unit = ( 3, 2 ), self.TestUnit( self.map.units )
		self.map.units[ pos ] = unit
		self.assertTrue( unit.position == pos,
			"Unit %s position was returned as %s, instead of %s." % ( unit, unit.position, pos ) )

		unit = self.TestUnit( self.map.units )
		self.assertTrue( unit.position == None,
			"Unit %s position was returned as %s, but it should not be on the map." % ( unit, unit.position ) )

def load_tests( loader, tests, pattern ):
	tests = [ TestMap, TestGrid, TestMapUnit ]

	suite = unittest.TestSuite()
	for test_class in tests:
		tests = loader.loadTestsFromTestCase( test_class )
		suite.addTests( tests )
	return suite

if __name__ == '__main__':
	loader = unittest.TestLoader()
	tests = load_tests( loader, None, None )
	unittest.TextTestRunner( verbosity=2 ).run( tests )
