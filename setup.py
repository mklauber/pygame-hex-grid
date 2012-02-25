from distutils.core import setup
import os.path

def read( filename ):
    path = os.path.join(os.path.dirname(__file__), filename)
    return open(path)

setup(
    name='pyghexmap',
    version=read( 'VERSION' ).read().strip(),
    url='https://github.com/mklauber/pygame-hex-grid/',
    packages=['hexmap'],
    license='GNU LESSER GENERAL PUBLIC LICENSE',
    author="Matt Lauber",
    author_email="pygame-hexmap@mklauber.com",
    description="A hex map implementation that provides a Map class, a abstract Render class that abstracts most of the drawing requirements, and a couple basic Render subclasses to get things started.",
	classifiers=[
        "Programming Language :: Python",
		"Development Status :: 3 - Alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
		"Topic :: Games/Entertainment :: Turn Based Strategy"
        ],
    long_description=read( 'README.rst' ).read(),
    install_requires=[ 'pygame']
 )
