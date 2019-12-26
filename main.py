#!/usr/bin/env python
"""doc string for dbus-bar for dwm"""
# -*- coding: utf-8 -*-

from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
from helpers import networkmanager, pulse, time, power, cpuramdisk

def init():
    """init loop"""
    print('start up dbus-bar')
    DBusGMainLoop(set_as_default=True)
    loop = GLib.MainLoop()

    pulse_audio = pulse.PulseAudio()
    pulse_audio.start()

    networkmanager.init()

    time_thread = time.Time()
    time_thread.start()

    power_thread = power.Power()
    power_thread.start()

    cpuramdisk_thread = cpuramdisk.CpuRamDisk()
    cpuramdisk_thread.start()

    print("init ok")

    pulse_audio.join()
    print("pulse audio thread joined")
    time_thread.join()
    print("time thread joined")
    power_thread.join()
    print("power thread joined")
    cpuramdisk_thread.join()
    print("crd thread joined")

    try:
        #print("now looping")
        loop.run()
    except KeyboardInterrupt:
        print("keyboard interrupt")

        if pulse_audio.isAlive():
            print("pulse audio thread alive, stop")
            pulse_audio.stop()
        else:
            print("pulse audio thread not alive")
        print("pulse audio thread stopped")

        if time_thread.isAlive():
            print("time thread alive, stop")
            time_thread.stop()
        else:
            print("time thread not alive")
        print("time thread stopped")

        if power_thread.isAlive():
            print("power thread alive, stop")
            power_thread.stop()
        else:
            print("power thread not alive")
        print("power thread stopped")

        if cpuramdisk_thread.isAlive():
            print("crd thread alive, stop")
            cpuramdisk_thread.stop()
        else:
            print("crd thread not alive")
        print("crd thread stopped")

        loop.quit()

if __name__ == "__main__":
    init()
