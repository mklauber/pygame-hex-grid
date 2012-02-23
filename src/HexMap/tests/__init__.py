import unittest
import Map
import Render

def suite():
	tests = [ Map, Render ]

	return unittest.TestSuite( tests=[ test.suite() for test in tests] )

if __name__ == '__main__':
	tests = suite()
	unittest.TextTestRunner( verbosity=2 ).run( tests )

