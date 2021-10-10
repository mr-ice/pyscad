#!/usr/bin/env python3

import openpyscad as ops
import argparse
import sys
import numpy
from math import sqrt


AP = argparse.ArgumentParser(description = "Make an OpenScad model")

AP.add_argument('--thickness', '-t', default=5,
    help="Thickness of the Bars and Legs of the template")

AP.add_argument('--basis', '-b', default='wyloch',
    help="The size of a square from 'wyloch','25mm','inch'")

AP.add_argument('--shape','-s',
    help="Shape of the outline from cone, cube, cylinder, line, sphere")

AP.add_argument('--radius','-r', type=int,
    help="Radius (or half a side) in ft (5ft to a square)")

AP.add_argument('--output', '-o', default='out.scad',
    help="Output filename, will be overwritten")

ya = AP.parse_args(sys.argv[1:])  # your args (for some reason args isn't working)

basis = {
    'wyloch': 31.75,
    'inch': 25.4,
    '25mm': 25.0
}

base = basis[ya.basis]

runits = int(ya.radius/5)  # 5 ft per square

# this may work, but 
# distance = lambda x, y: sqrt((x+0.5)**2+(y+0.5)**2)
def distance(x, y): return sqrt((x+0.5)**2+(y+0.5)**2)

# cone and sphere are related as a cone is an arc
# each quadrant is the same, so we generate a quadrant
grid = numpy.fromfunction(numpy.vectorize(distance), (runits, runits))

# the grid is a cone of distances, the cone just needs true/false to tell us which cells
# are in and which out of the cone.  This cone is 'se' facing.
quadrant = grid / runits < 1

# a spell 'radius' is an array of flipped cones, we'll call this the 'rshape'
se = quadrant
ne = numpy.rot90(quadrant, 1)
nw = numpy.rot90(quadrant, 2)
sw = numpy.rot90(quadrant, 3)

t_offset = ya.thickness + 0.5

# the rshape will be all the quadrants assembled
# stack the quadrants back in order
rshape = numpy.vstack(
    (
        numpy.hstack((nw, ne)),
        numpy.hstack((sw, se))
    )
)

if ya.shape == 'radius':
    c1 = ops.Cube([base, base, ya.thickness])
    u = ops.Union()

    for x in range(runits):
        for y in range(runits):
            if quadrant[x][y]:
                u.append(c1.translate([x*base, y*base, 0]))
    
    d = ops.Union()

    for tr in u.children:
        # make another set of tiles a little bit bigger than the
        # original tiles, so when we subtract them there aren't any
        # edges showing.
        s = tr.clone()
        s.v = [s.v[0]-t_offset, s.v[1]-t_offset, s.v[2]-1]
        s.children[0].size = [
            s.children[0].size[0] + 2,
            s.children[0].size[1] + 2,
            s.children[0].size[2] + 2
        ]
        d.append(s)

    (u-d).write(ya.output)