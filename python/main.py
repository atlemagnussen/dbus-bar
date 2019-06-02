#!/usr/bin/env python
"""doc string for dbus-bar for dwm"""
# -*- coding: utf-8 -*-

import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib

from helpers import networkmanager, status_state

STATE = status_state.Status()

def init():
    """init loop"""
    print('start up dbus-bar for dwm')
    DBusGMainLoop(set_as_default=True)
    loop = GLib.MainLoop()

    DBusGMainLoop(set_as_default=True)

    sys_bus = dbus.SystemBus()

    sys_bus.add_signal_receiver(get_network_state, 'StateChanged', 'org.freedesktop.NetworkManager')

    get_initial_state()

    try:
        loop.run()
    except KeyboardInterrupt:
        loop.quit()

def get_initial_state():
    """get all initial state"""
    get_network_state(70)

def get_network_state(code):
    """network state"""
    print(f'statecode={code}')
    if code <= 20:
        network_state = "disconnected"
    elif 20 < code < 70:
        network_state = "connecting"
    else:
        network_state = networkmanager.get_state()
    STATE.set_network(network_state)

if __name__ == "__main__":
    init()
