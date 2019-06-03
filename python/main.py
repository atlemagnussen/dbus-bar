#!/usr/bin/env python
"""doc string for dbus-bar for dwm"""
# -*- coding: utf-8 -*-

from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
from helpers import networkmanager, pulse

def init():
    """init loop"""
    print('start up dbus-bar for dwm')
    DBusGMainLoop(set_as_default=True)
    loop = GLib.MainLoop()

    pulse_audio = pulse.Pulse()
    pulse_audio.init()
    networkmanager.init()
    try:
        print("now looping")
        loop.run()
    except KeyboardInterrupt:
        print("keyboard interrupt")
        loop.quit()

if __name__ == "__main__":
    init()
