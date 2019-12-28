# dbus-bar

*Still kind of beta*  

Works for [dwm](https://dwm.suckless.org/) and [i3](https://i3wm.org/) / [sway](https://swaywm.org/)

![demo picture of dbus-bar](https://storage.googleapis.com/atle-static/pics/dbusbar-v.0.2.jpg)

## config
See [dbusbar.yml](https://github.com/atlemagnussen/dbus-bar/blob/master/dbusbar.yml) in this repository, copy into `~/.config/dbusbar.yml` if you want to start using dbus-bar and need to change behavior.  

I.e. to use it with `dwm` you must set
```yaml
writeToXroot: true
```

Config for i3/sway:
```
bar {
    status_command ~/dev/dbus-bar/main.py;
}
```

- Need Python3.5+
- Not everything is done with dbus, but as much as possible

## Features
### Volume
Via `Pulse Audio` dbus interface: immediately responds to volum changes and mute.

### Network
Via `Network manager` dbus interface: immediately responds to connectivity changes. Will show ip address if connected. Else disconnected or connecting is shown

### Power
Runs a thread and loop. Gets battery % and charging state via `Upower` dbus interface: If there is no battery the info will not show and the thread will exit.

```sh
sudo pacman -S upower
```

### Time and date
Runs a thread and loop that updates time and date stamp

### CPU, RAM and DISK percentage in use
Runs a thread that reads those numbers via `psutil`

## python

### sys dependencies
```sh
sudo pacman -S python-dbus  
sudo pacman -S python-gobject  
```

### venv for development
```sh
python3 -m venv env --system-site-packages

source env/bin/activate

pip install --upgrade pip

pip install -r requirements.txt
```
