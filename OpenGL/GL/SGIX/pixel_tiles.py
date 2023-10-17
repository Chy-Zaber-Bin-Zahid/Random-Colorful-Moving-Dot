'''OpenGL extension SGIX.pixel_tiles

This module customises the behaviour of the 
OpenGL.raw.GL.SGIX.pixel_tiles to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension deals with the interaction of existing GL functions that
	read pixels from memory, applications that use grids of tiles of pixels, 
	and convolution.
	
	Applications that deal with large multi-dimensional images sometimes
	break the image into a grid of rectangular tiles of pixels. Such an
	approach can help control memory use and expedite roaming through an 
	image that is large with respect to the available memory. 
	
	GL functions that cause pixels to be read from memory (e.g., DrawPixels 
	and TexImage2D) assume the pixels are stored as a single series of rows
	of pixels. The grid of tiles is essentially a sequence of the structures
	that the pixel reading functions assume. When an application that uses
	tiling uses a GL function such as DrawPixels, it must iterate
	through the tiles, either coalescing the tiles into a single tile in
	preparation for a single GL call or calling the GL function for each tile.
	
	The convolution operation imposes strict ordering on the way pixels
	in a subimage that crosses tile boundaries must be transferred: the rows 
	of pixels transferred must span the entire subimage. Applications 
	that use tiles of pixels and convolution must copy the subimage to be 
	transferred from the grid of tiles to a contiguous region, then pass the
	now-contiguous rows of pixels to the convolution function. If the
	coalescing of tiles is not needed for some other reason or is not a 
	side effect of some necessary operation, it is just redundant movement 
	of the pixels.
	
	This extension seeks to eliminate the extra copy of data by extending the 
	existing GL functions to accept, as a source of pixels in memory, a 
	grid of tiles of pixels in addition to the current sequence of rows 
	of pixels.
	

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SGIX/pixel_tiles.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.SGIX.pixel_tiles import *
from OpenGL.raw.GL.SGIX.pixel_tiles import _EXTENSION_NAME

def glInitPixelTilesSGIX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION