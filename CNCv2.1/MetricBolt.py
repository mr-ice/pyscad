import openpyscad as ops
class MetricDim:
    def __init__(self, size, s, m, e, p):
        self.size = size
        self.r = size/2
        self.clearance = self.r * 1.08  # 8~10% more for threads to clear a hole
        self.s = s  # face to face
        self.m = m  # nut depth
        self.e = e  # point to point
        self.p = p  # thread pitch
 

class MetricBolt:
    negative_expansion = 1.08

    dims = {
        1.6 : MetricDim(1.6, 3.20, 1.30, 3.41, 0.35),
        2   : MetricDim(2,   4.00, 1.60, 4.32, 0.4),
        2.5 : MetricDim(2.5, 5.00, 2.00, 5.45, 0.45),
        3   : MetricDim(3,   5.50, 2.40, 6.01, 0.5),
        3.5 : MetricDim(3.5, 6.00, 2.80, 6.58, 0.6),
        4   : MetricDim(4,   7.00, 3.20, 7.66, 0.7),
        5   : MetricDim(5,   8.00, 4.70, 8.79, 0.8),
        6   : MetricDim(6,  10.00, 5.20, 11.05, 1.0)
    }
    def __init__(self, thread_dia, length, negative=False):
        self.dia = thread_dia
        self.length = length
        self.negative = negative
        self.faces = 6

    @property
    def cap(self):
        h = self.dia
        r = self.dims[self.dia].e/1.9
        if self.negative:
            h *= 4
            r *= self.negative_expansion
        return ops.Cylinder(h, r=r, _fn=180)

    @property
    def shaft(self):
        r = self.dia/2
        if self.negative:
            r *= self.negative_expansion
        return ops.Cylinder(self.length, r=r, _fn=180)

    @property
    def nut(self):
        h = self.dims[self.dia].m
        r = self.dims[self.dia].e/2
        if self.negative:
            h *= 4
            r *= self.negative_expansion
        return ops.Cylinder(h, r=r, _fn=self.faces)

    @property
    def bolt(self):
        u = ops.Union()
        s = self.shaft
        c = self.cap
        n = self.nut
        u.append(n.translate([0,0,s.h + c.h]))
        u.append(s.translate([0,0,c.h]))
        u.append(c)
        return u

    @property
    def boltnut(self):
        u = ops.Union()
        u.append(self.shaft)
        u.append(self.nut.translate([0,0,self.length]))
        return u

    @property
    def boltcap(self):
        u = ops.Union()
        u.append(self.shaft.translate([0,0,self.dia]))
        u.append(self.cap)
        return u
