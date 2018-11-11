# Morph both ParM map and molecule from closed to open state and back.

movie record

# Morph map
vop morph #3,0 playStep 0.05 frames 40 mod #5

# Morph molecule
coordset #4 1,41

wait 40

movie encode output ~/Desktop/parm_morph.avi
