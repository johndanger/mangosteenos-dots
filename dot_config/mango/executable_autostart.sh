#!/bin/bash

set +e

# obs
dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP=wlroots >/dev/null 2>&1 &

# dms shell
#dms run >/dev/null 2>&1 &

# launch kdeconnect
if [ -f /usr/bin/kdeconnect-indicator ]; then
   kdeconnectd >/dev/null 2>&1 &
   kdeconnect-indicator >/dev/null 2>&1 &
fi

#start apps
flatpak run com.bitwarden.desktop >/dev/null 2>&1 &
flatpak run dev.vencord.Vesktop >/dev/null> 2>&1 &
flatpak run io.github.justinrdonnelly.bouncer >/dev/null 2>&1 &
flatpak run com.github.zocker_160.SyncThingy >/dev/null 2>&1 &