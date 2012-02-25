import unittest

import tests.Map as Map
import tests.Render as Render

def load_tests( loader, standard_tests, pattern ):
	tests = [ Map, Render ]

	return unittest.TestSuite( tests=[ test.load_tests( loader, standard_tests, None ) for test in tests] )

if __name__ == '__main__':

	loader = unittest.TestLoader()
	tests = load_tests( loader, None, None )
	unittest.TextTestRunner( verbosity=1 ).run( tests )

