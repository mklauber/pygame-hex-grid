========
 HexMap 
========
------------------------------------
 A HexGrid implementation for PyGame
------------------------------------

Introduction
============
HexMap is a python module for use on top of pygame.  It is designed to take a lot of the work out of utilizing a hexgrid.

Classes
=======

Map( object )
~~~~~~~~~~~~~~~~~~~~

Map.__init__( (rows, cols) )
++++++++++++++++++++++++++++

The Map object manages most of the basic data manipulation and access for the hexMap.  You can think of it as the table tracking all the positioning information regarding your grid.  It is capable of telling you the distance between two cells, the direction from one cell to another, and all the valid cells in a variety of shapes.

*valid cells are cells which are present on this map*

A Map is numbered as Follows::

	 ___     ___     ___
	/0,0\___/1,2\___/2,4\ 
	\___/1,1\___/2,3\___/
	/1,0\___/2,2\___/3,4\
	\___/2,1\___/3,3\___/
	/2,0\___/3,2\___/4,4\
	\___/3,1\___/4,3\___/
	/3,0\___/4,2\___/5,4\
	\___/4,1\___/5,3\___/
	/4,0\___/5,2\___/6,4\
	\___/5,1\___/6,3\___/
	    \___/   \___/
	

Map.distance( start, destination )
++++++++++++++++++++++++++++++++++

This method will tell you the straight distance between two cells, ignoring any obstacles in the way.:

Map.direction( start, destination )
+++++++++++++++++++++++++++++++++++

This method will tell you the direction from the start point to the destination point.:

Map.neighbors( cell )
+++++++++++++++++++++

This will tell you the **valid** cells adjoining this cell. *does not include the cell itself*:

Map.spread( cell, radius=1 )
++++++++++++++++++++++++++++

Returns all the **valid** cells within *radius* of *cell*, including the cell itself.:

Map.cone( cell, direction, length=1 )
+++++++++++++++++++++++++++++++++++++

This method returns the set of **valid** cells expanding out from 3 cells facing *direction* from *cell*, extending *length*.

Grid( dict )
~~~~~~~~~~~~
Grid.__init__( map )
++++++++++++++++++++

MapUnit( object )
~~~~~~~~~~~~~~~~~

MapUnit.__init__( grid )
++++++++++++++++++++++++

Render( object )
~~~~~~~~~~~~~~~~

Render.__init__( map, radius=16 )
+++++++++++++++++++++++++++++++++

RenderUnits( Render )
~~~~~~~~~~~~~~~~~~~~~

RenderGrid( Render )
~~~~~~~~~~~~~~~~~~~~

RenderFog( Render )
~~~~~~~~~~~~~~~~~~~

Example
=======

