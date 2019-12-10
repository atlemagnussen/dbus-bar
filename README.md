# dbus bar
So far only tested in [dwm](https://dwm.suckless.org/)

![demo gif of dbus-bar](https://storage.googleapis.com/atle-static/dbus-bar-v.0.1.gif)

only the python version is working  
Not everything is done with dbus, but as much as possible

## Features
### Volume
Via `Pulse Audio` dbus interface: immediately responds to volum changes and mute.

### Network
Via `Network manager` dbus interface: immediately responds to connectivity changes. Will show ip address if connected. Else disconnected or connecting is shown

### Power
Runs a thread and loop. Gets battery % and charging state via `Upower` dbus interface: If there is no battery it will exit.

```sh
sudo pacman -S upower
```

### Time and date
Runs a thread and loop that updates time and date stamp
