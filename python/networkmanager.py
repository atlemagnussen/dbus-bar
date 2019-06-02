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
        act_con_name = get_active_connection_name()
        # print(act_con_name)
        con = get_connection(act_con_name)
        print(con)
    except Exception as ex:
        print('Network manager not active probably')

def get_active_connection_name():
    """active connections names"""
    bus_obj = get_bus_object("org.freedesktop.NetworkManager", "/org/freedesktop/NetworkManager")
    props_iface = dbus.Interface(bus_obj, dbus_interface='org.freedesktop.DBus.Properties')
    props = props_iface.GetAll("org.freedesktop.NetworkManager")
    active = props.get('ActiveConnections')
    return str(active[0])

def get_connection(path):
    """get connection"""
    bus_obj = get_bus_object("org.freedesktop.NetworkManager", path)
    props_iface = dbus.Interface(bus_obj, dbus_interface='org.freedesktop.DBus.Properties')
    props = props_iface.GetAll("org.freedesktop.NetworkManager.Connection.Active")
    # for prop in props:
    #    val = str(props.get(prop))
    #    print(f'{prop}={val}')
    spec = props.get("Ip4Config")
    return str(spec)
if __name__ == "__main__":
    test()
