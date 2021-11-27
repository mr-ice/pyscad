use <../../scadlib/move.scad>
use <../../scadlib/tube.scad>

$fn = 180;

width=10;
pitch=2;
length = 19;

wall_t = 2;

t = 1;

module gate(t, length, width, pitch=pitch) {
    union() {
        cube([1, length, width]);
        move(x=1)
        for(i=[0:pitch:length]) {
            move(y=i)
            cube([1,1,width]);
        };
    };

    move(x = t*3)
    cube([2, length, width]);
};

move(x=5)
gate(t, length, width);

