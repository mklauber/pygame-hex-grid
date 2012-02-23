import unittest

import os, sys
dir = os.getcwd()
if dir not in sys.path:
	sys.path.append( dir )

import HexMap.tests.Map
import HexMap.tests.Render

def load_tests( loader, standard_tests, pattern ):
	tests = [ HexMap.tests.Map, HexMap.tests.Render ]

	return unittest.TestSuite( tests=[ test.load_tests( loader, standard_tests, None ) for test in tests] )

if __name__ == '__main__':

	loader = unittest.TestLoader()
	tests = load_tests( loader, None, None )
	unittest.TextTestRunner( verbosity=1 ).run( tests )

