#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Testing dbus with spotify"""
import os
import dbus

BUSNAME = 'org.PulseAudio1'
PATH = '/org/mpris/MediaPlayer2'
INTERFACENAME = 'org.mpris.MediaPlayer2.Player'

def test():
    """test"""
    bus = dbus.SessionBus()
    bus_object = bus.get_object(BUSNAME, PATH)
    interface = dbus.Interface(bus_object, dbus_interface=INTERFACENAME)
    # interface.PlayPause()

    props_iface = dbus.Interface(bus_object, dbus_interface='org.freedesktop.DBus.Properties')
    props = props_iface.GetAll(INTERFACENAME)
    metadata = props.get('Metadata')
    artist = metadata.get('xesam:artist')
    title = metadata.get('xesam:title')
    print(artist[0])
    print(title)
    # os.system("xsetroot" + " -name " + title)

if __name__ == "__main__":
    test()
