from abc import ABCMeta, abstractmethod
import pygame
import math
from hexmap.map import Grid

SQRT3 = math.sqrt( 3 )

class Render( pygame.Surface ):

	__metaclass__ = ABCMeta



	def __init__( self, map, radius=24, *args, **keywords ):
		self.map = map
		self.radius = radius

		# Colors for the map
		self.GRID_COLOR = pygame.Color( 50, 50, 50 )

		super( Render, self ).__init__( ( self.width, self.height ), *args, **keywords )

		self.cell = [( .5 * self.radius, 0 ),
					( 1.5 * self.radius, 0 ),
					( 2 * self.radius, SQRT3 / 2 * self.radius ),
					( 1.5 * self.radius, SQRT3 * self.radius ),
					( .5 * self.radius, SQRT3 * self.radius ),
					( 0, SQRT3 / 2 * self.radius )
		]



	@property
	def width( self ):
		return	self.map.cols * self.radius * 1.5 + self.radius / 2.0
	@property
	def height( self ):
		return ( self.map.rows + .5 ) * self.radius * SQRT3 + 1

	def get_surface( self, ( row, col ) ):
		"""
		Returns a subsurface corresponding to the surface, hopefully with trim_cell wrapped around the blit method.
		"""
		width = 2 * self.radius
		height = self.radius * SQRT3

		top = ( row - math.ceil( col / 2.0 ) ) * height + ( height / 2 if col % 2 == 1 else 0 )
		left = 1.5 * self.radius * col

		return self.subsurface( pygame.Rect( left, top, width, height ) )

	# Draw methods
	@abstractmethod
	def draw( self ):
		"""
		An abstract base method for various render objects to call to paint 
		themselves.  If called via super, it fills the screen with the colorkey,
		if the colorkey is not set, it sets the colorkey to magenta (#FF00FF)
		and fills this surface. 
		"""
		color = self.get_colorkey()
		if not color:
			magenta = pygame.Color( 255, 0, 255 )
			self.set_colorkey( magenta )
			color = magenta
		self.fill( color )

	# Identify cell
	def get_cell( self, ( x, y ) ):
		"""
		Identify the cell clicked in terms of row and column
		"""
		# Identify the square grid the click is in.
		row = math.floor( y / ( SQRT3 * self.radius ) )
		col = math.floor( x / ( 1.5 * self.radius ) )

		# Determine if cell outside cell centered in this grid.
		x = x - col * 1.5 * self.radius
		y = y - row * SQRT3 * self.radius

		# Transform row to match our hex coordinates, approximately
		row = row + math.floor( ( col + 1 ) / 2.0 )

		# Correct row and col for boundaries of a hex grid 
		if col % 2 == 0:
			if 	y < SQRT3 * self.radius / 2 and x < .5 * self.radius and \
				y < SQRT3 * self.radius / 2 - x:
				row, col = row - 1, col - 1
			elif y > SQRT3 * self.radius / 2 and x < .5 * self.radius and \
				y > SQRT3 * self.radius / 2 + x:
				row, col = row, col - 1
		else:
			if 	x < .5 * self.radius and abs( y - SQRT3 * self.radius / 2 ) < SQRT3 * self.radius / 2 - x:
				row, col = row - 1 , col - 1
			elif y < SQRT3 * self.radius / 2:
				row, col = row - 1, col


		return ( row, col ) if self.map.valid_cell( ( row, col ) ) else None

	def fit_window( self, window ):
	   top = max( window.get_height() - self.height, 0 )
	   left = max( window.get_width() - map.width, 0 )
	   return ( top, left )

class RenderUnits( Render ):
	"""
	A premade render object that will automatically draw the Units from the map 
	
	"""

	def __init__( self, map, *args, **keywords ):
		super( RenderUnits, self ).__init__( map, *args, **keywords )
		if not hasattr( self.map, 'units' ):
			self.map.units = Grid()

	def draw( self ):
		"""
		Calls unit.paint for all units on self.map
		"""
		super( RenderUnits, self ).draw()
		units = self.map.units

		for position, unit in units.items():
			surface = self.get_surface( position )
			unit.paint( surface )

class RenderGrid( Render ):
	def draw( self ):
		"""
		Draws a hex grid, based on the map object, onto this Surface
		"""
		super( RenderGrid, self ).draw()
		# A point list describing a single cell, based on the radius of each hex

		for col in range( self.map.cols ):
			# Alternate the offset of the cells based on column
			offset = self.radius * SQRT3 / 2 if col % 2 else 0
			for row in range( self.map.rows ):
				# Calculate the offset of the cell
				top = offset + SQRT3 * row * self.radius
				left = 1.5 * col * self.radius
				# Create a point list containing the offset cell
				points = [( x + left, y + top ) for ( x, y ) in self.cell]
				# Draw the polygon onto the surface
				pygame.draw.polygon( self, self.GRID_COLOR, points, 1 )

class RenderFog( Render ):

	OBSCURED = pygame.Color( 00, 00, 00, 255 )
	SEEN	 = pygame.Color( 00, 00, 00, 100 )
	VISIBLE	 = pygame.Color( 00, 00, 00, 0 )

	def __init__( self, map, *args, **keywords ):

		super( RenderFog, self ).__init__( map, *args, flags=pygame.SRCALPHA, **keywords )
		if not hasattr( self.map, 'fog' ):
			self.map.fog = Grid( default=self.OBSCURED )

	def draw( self ):

		#Some constants for the math		
		height = self.radius * SQRT3
		width = 1.5 * self.radius
		offset = height / 2

		self.fill( self.OBSCURED )

		for cell in self.map.cells():
			row, col = cell
			surface = self.get_cell( cell )

			# Calculate the position of the cell
			top = row * height - offset * col
			left = width * col

			#Determine the points that corresponds with
			points = [( x + left, y + top ) for ( x, y ) in self.cell]
			# Draw the polygon onto the surface
			pygame.draw.polygon( self, self.map.fog[ cell ], points, 0 )




def trim_cell( surface ):
	pass


if __name__ == '__main__':
	from .map import Map, MapUnit
	import sys

	class Unit( MapUnit ):
		color = pygame.Color( 200, 200, 200 )
		def paint( self, surface ):
			radius = surface.get_width() / 2
			pygame.draw.circle( surface, self.color, ( radius, int( SQRT3 / 2 * radius ) ), int( radius - radius * .3 ) )

	m = Map( ( 5, 5 ) )

	grid = RenderGrid( m, radius=32 )
	units = RenderUnits( m, radius=32 )
	fog = RenderFog( m, radius=32 )

	m.units[( 0, 0 ) ] = Unit( m )
	m.units[( 3, 2 ) ] = Unit( m )
	m.units[( 5, 3 ) ] = Unit( m )
	m.units[( 5, 4 ) ] = Unit( m )

	for cell in m.spread( ( 3, 2 ), radius=2 ):
		m.fog[cell] = fog.SEEN

	for cell in m.spread( ( 3, 2 ) ):
		m.fog[cell] = fog.VISIBLE

	print( m.ascii() )


	try:
		pygame.init()
		fpsClock = pygame.time.Clock()

		window = pygame.display.set_mode( ( 640, 480 ), 1 )
		from pygame.locals import QUIT, MOUSEBUTTONDOWN

		#Leave it running until exit
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.type == MOUSEBUTTONDOWN:
					print( units.get_cell( event.pos ) )

			window.fill( pygame.Color( 'white' ) )
			grid.draw()
			units.draw()
			fog.draw()
			window.blit( grid, ( 0, 0 ) )
			window.blit( units, ( 0, 0 ) )
			window.blit( fog, ( 0, 0 ) )
			pygame.display.update()
			fpsClock.tick( 10 )
	finally:
		pygame.quit()






