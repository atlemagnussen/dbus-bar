#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib

def init():
    """init loop"""
    DBusGMainLoop(set_as_default=True)
    loop = GLib.MainLoop()

    DBusGMainLoop(set_as_default=True)

    bus = dbus.SystemBus()

    bus.add_signal_receiver(state_handler, 'StateChanged', 'org.freedesktop.NetworkManager')

    try:
        loop.run()
    except KeyboardInterrupt:
        loop.quit()

def state_handler(state):
    """handle"""
    print(state)

if __name__ == "__main__":
    init()
