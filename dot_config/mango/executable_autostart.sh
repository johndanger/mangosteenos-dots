#!/bin/bash

set +e

AUTOSTART_JSON="${XDG_CONFIG_HOME:-$HOME/.config}/mangosteenos/.autostart_apps.json"

# Export env for systemd user units (D-Bus activation, DMS, etc.)
dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP=wlroots >/dev/null 2>&1 &

# dms
dms run >/dev/null 2>&1 &

# launch kdeconnect if user wants it
if [ -f "${XDG_CONFIG_HOME:-$HOME/.config}/mangosteenos/skip-kdeconnect" ]; then
   echo "Skipping kdeconnect"
else
   if [ -f /usr/bin/kdeconnect-indicator ]; then
      kdeconnectd >/dev/null 2>&1 &
      kdeconnect-indicator >/dev/null 2>&1 &
   else
      echo "kdeconnect-indicator not found"
   fi
fi

# Launch apps from JSON config (flatpak or executable in PATH)
# Run in background so script exits immediately; delay_seconds waits for tray to be ready
if [ -f "$AUTOSTART_JSON" ] && command -v jq >/dev/null 2>&1; then
   (
      count=$(jq -r '.apps | length' "$AUTOSTART_JSON" 2>/dev/null)
      [ -z "$count" ] || [ "$count" -le 0 ] 2>/dev/null && exit 0
      delay=$(jq -r '.delay_seconds // 0' "$AUTOSTART_JSON" 2>/dev/null)
      if [ -n "$delay" ] && [ "$delay" != "null" ] && [ "$delay" -gt 0 ] 2>/dev/null; then
         sleep "$delay"
      fi
      i=0
      while [ "$i" -lt "$count" ]; do
         type=$(jq -r ".apps[$i].type" "$AUTOSTART_JSON" 2>/dev/null)
         case "$type" in
            flatpak)
               id=$(jq -r ".apps[$i].id" "$AUTOSTART_JSON" 2>/dev/null)
               if [ -n "$id" ] && [ "$id" != "null" ]; then
                  flatpak run "$id" >/dev/null 2>&1 &
               fi
               ;;
            exec)
               cmd=$(jq -r ".apps[$i].command" "$AUTOSTART_JSON" 2>/dev/null)
               if [ -n "$cmd" ] && [ "$cmd" != "null" ]; then
                  sh -c "$cmd" >/dev/null 2>&1 &
               fi
               ;;
         esac
         i=$((i + 1))
      done
   ) &
fi
