#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Testing dbus with spotify"""
import os
import dbus

BUSNAME = 'org.mpris.MediaPlayer2.spotify'
PATH = '/org/mpris/MediaPlayer2'
INTERFACENAME = 'org.mpris.MediaPlayer2.Player'

def get_bus_object(name, path):
    """bus object"""
    bus = dbus.SessionBus()
    return bus.get_object(name, path)

def get_interface(bus_obj, interfacename):
    """interface"""
    return dbus.Interface(bus_obj, dbus_interface=interfacename)

def get_song(bus_obj):
    props_iface = dbus.Interface(bus_obj, dbus_interface='org.freedesktop.DBus.Properties')
    props = props_iface.GetAll("org.mpris.MediaPlayer2.Player")
    metadata = props.get('Metadata')
    artist = metadata.get('xesam:artist')
    title = metadata.get('xesam:title')
    print(artist[0])
    print(title)

def test():
    """test"""
    try:
        bus_obj = get_bus_object(BUSNAME, PATH)
        get_song(bus_obj)
        # interface = get_interface(bus_obj, INTERFACENAME)
        # interface.PlayPause()
    except Exception as ex:
        print('Spotify not active probably')

    # os.system("xsetroot" + " -name " + title)

if __name__ == "__main__":
    test()
