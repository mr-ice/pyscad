
radius:
	for r in $$(seq 60 -10 10); do \
		./SpellTemplates.py --shape=radius --radius=$$r --output=$$r-ft-radius.scad && \
		/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD -o $$r-ft-radius.stl $$r-ft-radius.scad; \
	done


