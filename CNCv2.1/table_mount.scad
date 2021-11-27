use <../../scadlib/move.scad>
use <../../scadlib/tube.scad>
use <belt_grip.scad>

$fn = 180;

corner_length = 130;
corner_depth = 30;
corner_depth_half = corner_depth/2;

function pyth(x) = sqrt(x*x+x*x);

thickness = 5;

thickness_pyt = sqrt(thickness*thickness + thickness*thickness);
corner_depth_pyt = pyth(corner_depth/2);
corner_depth_half_pyt = sqrt(corner_depth_half*corner_depth_half*2);

depth = 30;

belt_offset = 23.75; // mm from table edge to belt

lip_offset = depth - 10;

echo("corner_depth height by pythagorean theorum = ", corner_depth_pyt);

module tflange() {
    


    difference() {
        union() {
            // horizontal part of T-flange
            move(z=-thickness, x=-corner_depth)
            cube([corner_depth, corner_length, thickness]);

            // vertical
            move(x=-thickness,z=-depth)
            cube([thickness,corner_length,depth*2]);
            // angled lip above tabletop
            move(ry=-45, x=-thickness, z=lip_offset)
            cube([thickness,corner_length,thickness]);
        };
        
        // cut off the top above the angled lip
        color("blue")
        move(
            y=-1,
            ry=-45,
            z=lip_offset,
            x=-thickness-thickness_pyt)
        cube([thickness*3, corner_length+2, thickness*3]);
        
        // 45deg miter near origin
        move(rz=-225, z=-depth-1)
        cube([depth*2, depth, depth*2+2 ]);

        // 45deg miter away from origin
        move(x=-35, y=-35)
        union() {
            color("red")
            move(rz=45, z=-depth-1, y=corner_length)
            cube([depth*2, depth, depth*2+2 ]);
        };

    };
};



union() {
    tflange();

    difference() {
        move(x=-depth, z=-depth, y=corner_length/2-thickness/2)
        cube([depth, thickness, depth]);

        move(rx=90, x=-depth-thickness, z=-depth-thickness, y=corner_length/2+thickness/2+1)
        cylinder(thickness+2, r=depth);
    };
};