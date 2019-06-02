#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib

DBusGMainLoop(set_as_default=True)
loop = GLib.MainLoop()

def new_connection_handler(device):
    print(device)

NM_DBUS_SERVICE = "org.freedesktop.NetworkManager"
NM_DBUS_OBJECT_PATH = "/org/freedesktop/NetworkManager"
NM_DBUS_INTERFACE = NM_DBUS_SERVICE

DBusGMainLoop(set_as_default=True)

bus = dbus.SystemBus()

bus.add_signal_receiver(new_connection_handler, 'StateChanged', 'org.freedesktop.NetworkManager')

try:
    loop.run()
except KeyboardInterrupt:
    loop.quit()

