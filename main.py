#!/usr/bin/env python
"""doc string for dbus-bar for dwm"""
# -*- coding: utf-8 -*-
import signal
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
from helpers import networkmanager, pulse, time, power, cpuramdisk
threads = []
loop = None

def signal_handler(signal, frame):
    """signal handler"""
    print(f"{signal} signal was received")
    stop()

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

def init():
    """init loop"""
    print('start up dbus-bar')
    DBusGMainLoop(set_as_default=True)
    global loop
    loop = GLib.MainLoop()

    pulse_audio = pulse.PulseAudio()
    pulse_audio.start()
    threads.append(pulse_audio)

    networkmanager.init()

    time_thread = time.Time()
    time_thread.start()
    threads.append(time_thread)

    power_thread = power.Power()
    power_thread.start()
    threads.append(power_thread)

    cpuramdisk_thread = cpuramdisk.CpuRamDisk()
    cpuramdisk_thread.start()
    threads.append(cpuramdisk_thread)

    print("init ok")

    try:
        #print("now looping")
        loop.run()
    except KeyboardInterrupt:
        print("keyboard interrupt")
        stop()

def stop():
    """stop"""
    for t in threads:
        if t.is_alive():
            print(f"thread {t.name} is alive, stop")
            t.stop()
        else:
            print(f"thread {t.name} was not alive")

    for t in threads:
        t.join()
        print(f"thread {t.name} was joined")
        loop.quit()

if __name__ == "__main__":
    init()
