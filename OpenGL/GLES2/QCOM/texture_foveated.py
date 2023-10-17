'''OpenGL extension QCOM.texture_foveated

This module customises the behaviour of the 
OpenGL.raw.GLES2.QCOM.texture_foveated to provide a more 
Python-friendly API

Overview (from the spec)
	
	Foveated rendering is a technique that aims to reduce fragment processing
	workload and bandwidth by reducing the average resolution of a render target.
	Perceived image quality is kept high by leaving the focal point of
	rendering at full resolution.
	
	It exists in two major forms:
	
	    - Static foveated (lens matched) rendering: where the gaze point is
	    fixed with a large fovea region and designed to match up with the lens
	    characteristics.
	    - Eye-tracked foveated rendering: where the gaze point is continuously
	    tracked by a sensor to allow a smaller fovea region (further reducing
	    average resolution)
	
	Traditionally foveated rendering involves breaking a render target's area
	into smaller regions such as bins, tiles, viewports, or layers which are
	rendered to individually. Each of these regions has the geometry projected
	or scaled differently so that the net resolution of these layers is less
	than the original render target's resolution. When these regions are mapped
	back to the original render target, they create a rendered result with
	decreased quality as pixels get further from the focal point.
	
	Foveated rendering is currently achieved by large modifications to an
	applications render pipelines to manually implement the required geometry
	amplifications, blits, and projection changes.  This presents a large
	implementation cost to an application developer and is generally
	inefficient as it can not make use of a platforms unique hardware features
	or optimized software paths. This extension aims to address these problems
	by exposing foveated rendering in an explicit and vendor neutral way, and by
	providing an interface with minimal changes to how an application specifies
	its render targets.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/QCOM/texture_foveated.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.QCOM.texture_foveated import *
from OpenGL.raw.GLES2.QCOM.texture_foveated import _EXTENSION_NAME

def glInitTextureFoveatedQCOM():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION