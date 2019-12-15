#!/usr/bin/env python3

from datetime import datetime
from psutil import disk_usage, sensors_battery
from psutil._common import bytes2human
from socket import gethostname, gethostbyname
from subprocess import check_output
from sys import stdout
from time import sleep

def write(data):
    stdout.write('%s\n' % data)
    stdout.flush()

def refresh():
    disk = bytes2human(disk_usage('/').free)
    #ip = gethostbyname(gethostname())
    #try:
    #    ssid = check_output("iwgetid -r", shell=True).strip().decode("utf-8")
    #    ssid = "(%s)" % ssid
    #except Exception:
    #    ssid = "None"
    battery = int(sensors_battery().percent)
    status = "+" if sensors_battery().power_plugged else "-"
    date = datetime.now().strftime('%d-%m-%Y %H:%M')
    format = "%s | ⭍%s%%%s | %s"
    write(format % (disk, battery, status, date))

while True:
    refresh()
    sleep(1)


# Additional emojis and characters for the status bar:
# Electricity: ⚡ ↯ ⭍ 
# Audio: 🔈 🔊 🎧 🎶 🎵 🔇 🔉
# Separators: \| ❘ ❙ ❚
# Misc:  💻 💡 ⭐ ↑ ↓ ✉ ✅ ❎
