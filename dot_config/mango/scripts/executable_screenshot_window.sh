#!/usr/bin/bash
grim -l 0 -g "$(mmsg -x | awk '/ x / {x=$3} / y / {y=$3} / width / {w=$3} / height / {h=$3} END {print x","y" "w"x"h}')" - | wl-copy
