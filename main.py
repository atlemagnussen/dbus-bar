#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This script checks dbus for spotify information and writes it to xroot
also tries to subscribe for the Seeked signal"""
import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib

DBusGMainLoop(set_as_default=True)

BUSNAME = 'org.mpris.MediaPlayer2.spotify'
PATH = '/org/mpris/MediaPlayer2'
INTERFACENAME = 'org.mpris.MediaPlayer2.Player'

def init():
    """init"""
    DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()
    bus_object = bus.get_object(BUSNAME, PATH)
    interface = dbus.Interface(bus_object, dbus_interface=INTERFACENAME)

    loop = GLib.MainLoop()
    def handler(sender=None):
        """handler"""
        print("got signal from %r" % sender)
    
    interface.connect_to_signal(None, handler, sender_keyword='sender')
    print("interface connected to Seeked signal, now loop")
    try:
        loop.run()
    except KeyboardInterrupt:
        loop.quit()


def get_info():
    """main"""
    bus = dbus.SessionBus()

    bus_object = bus.get_object(BUSNAME, PATH)
    interface = dbus.Interface(bus_object, dbus_interface=INTERFACENAME)
    interface.PlayPause()

    props_iface = dbus.Interface(bus_object, dbus_interface='org.freedesktop.DBus.Properties')
    props = props_iface.GetAll("org.mpris.MediaPlayer2.Player")
    metadata = props.get('Metadata')
    artist = metadata.get('xesam:artist')
    title = metadata.get('xesam:title')
    print(artist)
    print(title)

def handler2():
    """handler"""
    print("got signal")

if __name__ == "__main__":
    init()
