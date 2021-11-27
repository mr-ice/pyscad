use <../../scadlib/move.scad>

length = 65;
depth = 5;
width = 20;

difference() {
    cube([length, length, depth]);
    
    color("red")
    move(z=-1, x=-1, y=-1)
    cube([length-width+1, length-width+1, depth+2]);
};