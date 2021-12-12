#!/usr/bin/env python3

import openpyscad as ops
from MetricBolt import MetricBolt
from Config import ReadConfig

config = ReadConfig('belt-tensioner.config')
bolt = MetricBolt(4,8, negative=True)

u = ops.Union()
for x in (0, config.mount_bolt_horizontal_spacing):
    for y in (0, config.mount_bolt_vertical_spacing):
        u.append(bolt.bolt.translate([x,y,0]))

u.write('bolt-pattern.scad')
