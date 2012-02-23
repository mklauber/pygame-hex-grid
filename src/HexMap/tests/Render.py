import unittest

from HexMap.Render import Render, RenderUnits, RenderGrid, RenderFog

class TestRender():

	class TestRender( Render ):
		def draw( self ):
			super( self.TestRender, self ).draw()




def suite():
	pass

if __name__ == '__main__':
	tests = suite()
	unittest.TextTestRunner( verbosity=2 ).run( tests )
