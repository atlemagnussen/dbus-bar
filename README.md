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

If you don't have these you need to install them. Though you probably have PulseAudio, if not it might take some more work in addition to installing it. For this you can use `pavucontrol`

```sh
#arch
sudo pacman -S pulseaudio
sudo pacman -S upower
sudo pacman -S networkmanager

#debian
sudo apt install pulseaudio
sudo apt install upower
sudo apt install network-manager
```

### Time and date
Runs a thread and loop that updates time and date stamp

### CPU, RAM and DISK percentage in use
Runs a thread that reads those numbers via `psutil`

## python

### sys dependencies
```sh
#arch
sudo pacman -S python-dbus
sudo pacman -S python-gobject
sudo pacman -S python-psutil
sudo pacman -S python-yaml

#debian
sudo apt install pyhton3-dbus
sudo apt install python3-gi
sudo apt install python3-psutil
sudo apt install python3-yaml
```
Not all debian based flavours have got the version 5.1 of `pyYAML` which is required. So install it with pip:
```sh
pip3 install -U pyYAML
```

### venv for development
```sh
python3 -m venv env --system-site-packages

source env/bin/activate

pip install --upgrade pip

pip install -r requirements.txt
```
