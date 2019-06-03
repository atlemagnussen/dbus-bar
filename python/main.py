#!/usr/bin/env python
"""doc string for dbus-bar for dwm"""
# -*- coding: utf-8 -*-

from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib

from helpers import networkmanager

def init():
    """init loop"""
    print('start up dbus-bar for dwm')
    DBusGMainLoop(set_as_default=True)
    loop = GLib.MainLoop()

    networkmanager.init()

    try:
        loop.run()
    except KeyboardInterrupt:
        loop.quit()

if __name__ == "__main__":
    init()
