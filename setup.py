from distutils.core import setup

setup( 
    name='HexMap',
    version='0.1dev',
    packages=['hexmap' ],
    license='',
    author="Matt Lauber",
    author_email="pygame-hexmap@mklauber.com",
    description="A hex map implementation that provides a Map class, a abstract Render class that abstracts most of the drawing requirements, and a couple basic Render subclasses to get things started.",
    long_description=open( 'README.txt' ).read(),
 )
