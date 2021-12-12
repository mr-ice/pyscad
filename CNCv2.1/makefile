openscad := /Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD

all: belt_tensioner_top.stl belt_tensioner_bottom.stl

%.stl: %.scad
	$(openscad) $< -o $@

%bottom.scad: belt_grip.py
	./belt_grip.py --part bottom --out $@

%top.scad: belt_grip.py
	./belt_grip.py --part top --out $@