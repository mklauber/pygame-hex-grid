import unittest

from HexMap.Map import Map
from HexMap.Render import Render, RenderUnits, RenderGrid, RenderFog

class TestRender( unittest.TestCase ):

	class TestRender( Render ):
		def draw( self ):
			super( self.TestRender, self ).draw()


def load_tests( loader, tests, pattern ):
	tests = [ TestRender ]

	suite = unittest.TestSuite()
	for test_class in tests:
		tests = loader.loadTestsFromTestCase( test_class )
		suite.addTests( tests )
	return suite

if __name__ == '__main__':
	tests = suite()
	unittest.TextTestRunner( verbosity=2 ).run( tests )
