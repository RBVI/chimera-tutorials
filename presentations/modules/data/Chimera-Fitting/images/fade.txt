# Show molecule flying into map.

# Set initial state
surft 50 #0
modeldisp #0
~modeldisp #2

movie record

# Fade out then hide map #0
surft 100 #0 25
wait 25
~modeldisp #0

# Fade in map #2
surft 100 #2
modeldisp #2
surft 50 #2 25
wait 25

movie encode output ~/Desktop/fade.avi
