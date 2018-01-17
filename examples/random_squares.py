"""
This generates a picture with 100 squares of random size, angle,
color and position.


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

import gizeh as gz
import numpy as np

L = 200 # <- dimensions of the final picture
surface = gz.Surface(L, L, bg_color=(1,1,1))

# We generate 1000 random values of size, angle, color, position.
# 'rand' is a function that generates numbers between 0 and 1
n_squares = 1000 # number of squares
angles = 2*np.pi* np.random.rand(n_squares) # n_squares angles between 0 and 2pi
sizes = 20 + 20 * np.random.rand(n_squares) # all sizes between 20 and 40
positions = L * np.random.rand(n_squares, 2) # [ [x1, y1] [x2 y2] [x3 y3]]...
colors = np.random.rand(n_squares, 3)


for angle, size, position, color in zip(angles, sizes, positions, colors):
    square = gz.square(size, xy=position, angle=angle, fill=color,
                       stroke_width=size/20) # stroke is black by default.
    square.draw(surface)

surface.write_to_png("random_squares.png")
