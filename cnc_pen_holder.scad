use <../scadlib/move.scad>
use <../scadlib/tube.scad>
use <../scadlib/sector.scad>

// od = 36.5
// id = 11.75
od = 36.75;  // outer diameter (hole in plate)
id = 11.75; // inner diameter (hole for pen)
$fn = 180;

pen_depth = 10;

bar_width = 6;
// inner cylinder

oid = od - 4;

iod = id + 4;

slot_dia = 1; // added to dia to cut a slot

slot_half = (oid-iod)/2;

outer_thickness = 1;  // thickness of bottom outside OD
thickness = 2.33; // thickness of bottom inside OD

outer_wall_depth = 6 + outer_thickness;

difference() {  // difference
    
    // base
    tube(pen_depth, od+4, id);
    
    // remove outer bit to make tube
    move(z=outer_thickness)
    tube(pen_depth, od+5, od);
    
    // cut out the middle bits above the outer wall
    move(z=outer_wall_depth)
    tube(pen_depth, od+3, id+4);
    
    // cut out the middle bits below the outer wall
    move(z=thickness)
    tube(pen_depth, od-3, id+4);
    
    // slot in inner wall to provide friction fit for pen
    move(x=-0.5, y=-id/2-2.2, z=-1)
    cube([1,4,pen_depth+2]);

    difference() {
        // cylinder cuts
        for(i=[iod:slot_half:oid]){
            move(z=-1)
            tube(pen_depth, i+slot_dia, i);
        };
        
        // tabs to connect inner cylinder
        for(r=[60:120:359]) {
            linear_extrude(pen_depth+2)
            sector(id/2+4, [r, r+30]);
        };

        // tabs to connect outer cylinder
        difference() {
            for(r=[68:120:359]) {
                linear_extrude(pen_depth+2)
                sector(od/2, [r, r+20]);
            };
            move(z=-1)
            cylinder(pen_depth+4, r=od/2-4);
        };

        // tabs to connect middle spring strips
        difference() {
            for(r=[91:120:359]) {
                linear_extrude(pen_depth+2)
                sector(id+4, [r, r+20]);
            };
            move(z=-1)
            cylinder(pen_depth+4, r=slot_half+0.5);
        };


    };
    
    // radial cuts to make spring springy
    move(z=-1)
    difference() {
        for(r=[-32:120:359]) {
            linear_extrude(pen_depth+2)
            sector(od/2, [r, r+3]);
        };
        cylinder(pen_depth+4, r=id/2+2);
        tube(pen_depth+4, od, od-3.8);
    };

};


// raised friction bumps around perimeter
difference() {
    for(r=[91:120:359]) {
        linear_extrude(5)
        sector(od/2+0.5, [r, r+5]);
    };
    move(z=-1)
    cylinder(pen_depth, r=od/2-1.5);
};
