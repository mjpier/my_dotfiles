#!/bin/sh
#xset s off -dpms &
setxkbmap latam &
#remaps &
#xsetroot -cursor_name left_ptr &
#setbg &
feh --bg-fill /home/mjpier/.local/share/wallpapers/cat-sound.png &
dwmblocks &
#usersv

autostart="picom mpd dunst unclutter"

for program in $autostart; do
  pidof -s "$program" || setsid -f "$program"
done >/dev/null 2>&1

exec dbus-run-session dwm
