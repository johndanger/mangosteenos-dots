#!/usr/bin/bash
# Move all windows from laptop screen to external monitors.
# Usage: move_to_external.sh [laptop-output] [direction]
#   laptop-output: output name for the laptop/internal screen (default: eDP-1)
#   direction:     direction towards external monitors (default: left)
#
# If mmsg -O output format differs, check it manually and adjust the awk parsing below.

LAPTOP_OUTPUT="${1:-eDP-1}"
DIRECTION="${2:-left}"
MAX_ITER=50

# Parse laptop monitor x origin and width from mmsg -O.
# Assumes output format has "name : <output>" followed by "x : <n>" and "width : <n>".
LAPTOP_X=$(mmsg -O 2>/dev/null | awk -v out="$LAPTOP_OUTPUT" '
    /name/ && $3 == out { found=1 }
    found && / x /      { print $3; exit }
')
LAPTOP_W=$(mmsg -O 2>/dev/null | awk -v out="$LAPTOP_OUTPUT" '
    /name/ && $3 == out { found=1 }
    found && / width /  { print $3; exit }
')

if [ -z "$LAPTOP_X" ] || [ -z "$LAPTOP_W" ]; then
    echo "Error: Could not find monitor '$LAPTOP_OUTPUT'."
    echo "Run 'mmsg -O' to check available monitors and adjust LAPTOP_OUTPUT."
    exit 1
fi

LAPTOP_X_MAX=$((LAPTOP_X + LAPTOP_W))
moved=0
stalls=0

echo "Moving windows from $LAPTOP_OUTPUT (x:$LAPTOP_X–$LAPTOP_X_MAX) → $DIRECTION..."

for i in $(seq 1 $MAX_ITER); do
    # Attempt to switch focus to the laptop monitor
    mmsg -o "$LAPTOP_OUTPUT" -s 2>/dev/null

    # Get focused window x position
    win_x=$(mmsg -g -x 2>/dev/null | awk '/ x / { print $3; exit }')

    if [ -z "$win_x" ] || ! [[ "$win_x" =~ ^-?[0-9]+$ ]] || \
       [ "$win_x" -lt "$LAPTOP_X" ] || [ "$win_x" -ge "$LAPTOP_X_MAX" ]; then
        # No window on laptop screen — try cycling, stop after 3 consecutive misses
        stalls=$((stalls + 1))
        [ "$stalls" -ge 3 ] && break
        mmsg -d "focusstack,next" 2>/dev/null
    else
        # Window is on laptop screen — move it to the external monitor
        mmsg -d "tagmon,$DIRECTION" 2>/dev/null
        moved=$((moved + 1))
        stalls=0
    fi
done

echo "Done. Moved $moved window(s) from $LAPTOP_OUTPUT."
