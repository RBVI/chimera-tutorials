# Start with b12movie.py session file which has saved positions
#  "spin", "far", "docked", "bound", "final"
#
# Models:
#  0 = unbound map
#  1 = unbound gp120
#  2 = bound map
#  3 = bound gp120 + FAB b12 
#

# Set initial scene
~modeldisp
~ribbon #3:.G
surft 50 #0

reset spin
modeldisp #0,1

# Start recording movie.
movie record

# Spin 360 degrees
turn y 3 120
wait 120

# Fly FAB b12 in to docked position
reset far 50
wait 50
modeldisp #3
reset docked 50
wait 50

# Fade out unbound map
surft 100 #0 25
wait 25
~modeldisp #0

# Fade in bound map
surft 100 #2
modeldisp #2
surft 50 #2 25
wait 25

# Hide unbound gp120 and show bound gp120
~modeldisp #1 ; ribbon #3:.G

# Rotate gp120 and b12 to bound fit position.
reset bound 50
wait 100
reset docked 50
wait 50
reset bound 50
wait 50

# Different view angle.
reset final 50
wait 50

# Write movie file.
movie encode output ~/Desktop/b12movie.avi
