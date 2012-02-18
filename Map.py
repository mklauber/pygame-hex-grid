from abc import ABCMeta, abstractmethod
import argparse
import math
import pygame

import logging
logger = logging.getLogger( __name__ )


class Map( object ):
	"""
	An top level object for managing all game data related to positioning, movement, and display.
	"""
	def __init__( self, ( rows, cols ), *args, **keywords ):
		# for tracking units
		self.positions = Position()
		
		#Map size
		self.rows = rows
		self.cols = cols

	@property
	def size( self ):
		"""Returns the size of the grid as a tuple (row, col)"""
		return ( self.rows, self.cols )
		
	def distance( self, start, destination ):
		"""Takes two hex coordinates and determine the distance between them."""
		logger.debug( "Start: %s, Dest: %s", start, destination )
		diffX = destination[0] - start[0]
		diffY = destination[1] - start[1]
	
		distance = min( abs( diffX ), abs( diffY ) ) + abs( diffX - diffY )
		
		logger.debug( "diffX: %d, diffY: %d, distance: %d", diffX, diffY, distance )
		return distance 

	

	def ascii( self, numbers=True ):
		""" Debug method that draws the grid using ascii text """
		
		table = ""
		
		if numbers:
			text_length = len( 
				str( self.rows - 1 if self.cols % 2 == 1 else self.rows ) + 
				',' + 
				str( int( self.rows - 1 +math.floor( self.cols / 2 ) ) ) 
			)
		else:
			text_length = 3 
		
		#Header for first row
		for col in range( self.cols ):
			if col % 2 == 0:
				table += " " + '_' * text_length
			else:
				table += " " + ' ' * text_length
		table += "\n"
		# Each additional row
		for row in range( ( self.rows ) * 2 + 1 ):
			row_text = ""
			# Alternate starting slashes
			if row % 2 == 0:
				row_text += "/"
			else:
				row_text += "\\"
			# No leading slash on bottom row
			if row == self.rows * 2 :
				row_text = " "
			
			for col in range( self.cols ):
				if (row + col) % 2 == 1:
					row_text += '_' * text_length + "/"
				else:
					row_text += ' ' * text_length + "\\"
			
			# No trailing slass on first row, if even
			if row == 0 and self.cols % 2 == 0 :
				row_text = row_text[:-1]
				
			# No trailing slass on last row, if odd
			if row == self.rows * 2 and self.cols % 2 ==1 :
				row_text = row_text[:-1]
			
			# append row to table
			table +=  row_text + "\n"

		return table			

	
class Position( dict ):
	"""An extension of a basic dictionary with a fast lookup by value implementation."""
	def find( self, unit ):
		"""
		A fast lookup by value implementation
		"""
		temp = unit
		for pos, unit in self.items():
			if unit == temp:
				return pos

class MapUnit( object ):
	"""
	An abstract base class that will contain or require implementation of all the methods necessary for a unit to be managed by a map object.
	"""
	
	__metaclass__ = ABCMeta
	
	def __init__( self, map=map ):
		self.map = map=map
		
	@property
	def position( self ):
		"""A property that looks up the position of this unit on it's associated map."""
		return self.map.position.find( self )
	
	@abstractmethod
	def paint( self, surface ):
		"""An abstract base method to contain the painting code for a given unit."""
		pass
		
	def _paint( self ):
		"""A private method that does any necessary setup and teardown for the paint implementation."""
		#TODO: determine sizing for this surface
		surface = pygame.Surface()	#Create the surface needed for paint
		surface = self.paint( surface )
		return trim_tile( surface )	#Make transparent any areas outside the tile.
		
def _trim_tile( surface ):
	"""Helper method to make transparent any area on the surface outside the tile."""
	pass
		
		
if __name__ == '__main__':



	# Setup arguments for testing this code
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('-r', '--rows', dest='rows', type=int, default=5, help='Number of rows in grid.  Defaults to 5.')
	parser.add_argument('-c', '--cols', dest='cols', type=int, default=5, help='Number of columns in grid.  Defaults to 5.')
	parser.add_argument('-n', '--numbers', action='store', dest="numbers", type=bool, default=True, help='Display grid numbers on tiles.  Defaults to false')
						 
	args = parser.parse_args()
	print( "Args: %s" % ( args ) )
	m = Map( (args.rows, args.cols ) )
	print m.ascii()
