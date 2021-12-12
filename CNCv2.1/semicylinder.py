import openpyscad as ops

def semicylinder(height, radius, depth):
    cutter_h = height + 2
    cutter_w = radius * 2 + 2
    
    d = ops.Difference()

    c = ops.Cylinder(height, radius)
    c = c.translate([+depth-radius,0,0])
    s = ops.Cube([cutter_w, cutter_w, cutter_h])
    d.append(c)
    # this put the cutter block at zero
    s = s.translate([-cutter_w, -cutter_w/2, -1])
    d.append(s)
    return d