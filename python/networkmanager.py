"""network manager dbus"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from pydbus import SystemBus
import dbus
# from gi.repository import GLib

def get_bus_object(name, path):
    """bus object"""
    bus = dbus.SystemBus()
    return bus.get_object(name, path)

def get_interface(bus_obj, interfacename):
    """interface"""
    return dbus.Interface(bus_obj, dbus_interface=interfacename)

def test():
    """test"""
    try:
        bus_obj = get_bus_object("org.freedesktop.NetworkManager", "/org/freedesktop/NetworkManager")
        props_iface = dbus.Interface(bus_obj, dbus_interface='org.freedesktop.DBus.Properties')
        props = props_iface.GetAll("org.freedesktop.NetworkManager")
        active = props.get('ActiveConnections')
        print(active[0])
        # interface = get_interface(bus_obj, INTERFACENAME)
        # interface.PlayPause()
    except Exception as ex:
        print('Network manager not active probably')


if __name__ == "__main__":
    test()
