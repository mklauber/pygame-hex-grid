import unittest

from HexMap.Map import Map, Position, MapUnit

class TestMap( unittest.TestCase ):
	pass


class TestPosition( unittest.TestCase ):
	def setUp( self ):
		self.position = Position()

	def test_assignment( self ):
		key, value = ( 0, 0 ), "U"
		self.position[ key ] = value
		self.assertTrue( key in self.position,
			"Failed to create key %s" % str( key ) )
		self.assertTrue( value == self.position[ key ],
			"Key %s does not return value %s" % ( key, value ) )

	def test_find( self ):
		key, value = ( 0, 0 ), "U"
		self.position[ key ] = value
		self.assertTrue( key == self.position.find( value ),
			 "Find %s did not correctly return key %s " % ( value, key ) )

class TestMapUnit( unittest.TestCase ):

	class TestUnit( MapUnit ):
		def paint( self, surface ):
			pass

	def setUp( self ):
		self.map = Map( ( 5, 5 ) )

	def test_position_succeeds( self ):
		pos, unit = ( 3, 2 ), self.TestUnit( self.map )
		self.map.positions[ pos ] = unit
		self.assertTrue( unit.position == pos,
			"Unit %s position was returned as %s, instead of %s." % ( unit, unit.position, pos ) )

		unit = self.TestUnit( self.map )
		self.assertTrue( unit.position == None,
			"Unit %s position was returned as %s, but it should not be on the map." % ( unit, unit.position ) )

def suite():
	tests = [ TestMap, TestPosition, TestMapUnit ]

	loader = unittest.TestLoader().loadTestsFromTestCase
	tests = map( loader, tests )
	return unittest.TestSuite( tests=tests )

if __name__ == '__main__':
	tests = suite()
	unittest.TextTestRunner( verbosity=2 ).run( tests )
