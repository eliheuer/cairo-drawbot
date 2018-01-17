"""

The MIT License (MIT)
[OSI Approved License]

The MIT License (MIT)

Copyright (c) 2014 Zulko

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import numpy as np



def rotation_matrix(a):
    return np.array([[np.cos(a),  -np.sin(a),0],
                      [np.sin(a),  np.cos(a),0],
                      [0,          0 ,       1.0]])

def translation_matrix(xy):
    return np.array([[1.0,0,xy[0]],
                     [0,1,xy[1]],
                     [0,0,1]])

def scaling_matrix(sx,sy):
    return np.array([[sx,0,0],
                     [0,sy,0],
                     [0,0,1]])

def polar_polygon(nfaces,radius, npoints):
    """ Returns the (x,y) coordinates of n points regularly spaced
    along a regular polygon of `nfaces` faces and given radius.
    """
    theta=np.linspace(0,2*np.pi,npoints)[:-1]
    cos, pi, n = np.cos, np.pi, nfaces
    r= cos( pi/n )/cos((theta%(2*pi/n))-pi/n)
    d = np.cumsum(np.sqrt(((r[1:]-r[:-1])**2)))
    d = [0]+list(d/d.max())
    return zip(radius*r, theta, d)

def polar2cart(r,theta):
    """ Transforms polar coodinates into cartesian coordinates (x,y).
    If r or theta or both are vectors, returns a np. array of the list
    [(x1,y1),(x2,y2),etc...]
    """

    res =  r*np.array([np.cos(theta), np.sin(theta)])
    return res if len(res.shape)==1 else res.T
