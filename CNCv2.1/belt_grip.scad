use <../../scadlib/move.scad>
use <../../scadlib/tube.scad>

$fn = 180;

module belt_grip(t=1, length=19, width=10, pitch=2) {
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
belt_grip(t, length, width);

