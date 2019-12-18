"""network manager dbus"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dbus
from helpers import status_state, colors

STATE = status_state.Status.get_instance()
NETWORK_UCODE = u"\U0001F5A7"

def init():
    """init network"""
    sys_bus = dbus.SystemBus()
    get_network_state(70)
    sys_bus.add_signal_receiver(get_network_state, 'StateChanged', 'org.freedesktop.NetworkManager')

def get_network_state(code):
    """network state"""
    if code <= 20:
        network_state = f"{colors.FAIL}disconnected{colors.RESET}"
    elif 20 < code < 70:
        network_state = f"{colors.WARN}connecting{colors.RESET}"
    else:
        network_state = get_state()
    network_state = f'{NETWORK_UCODE}{network_state}'
    STATE.set_network(network_state)

def get_bus_object(name, path):
    """bus object"""
    bus = dbus.SystemBus()
    return bus.get_object(name, path)

def get_interface(bus_obj, interfacename):
    """interface"""
    return dbus.Interface(bus_obj, dbus_interface=interfacename)

def get_state():
    """network manager state"""
    try:
        act_con_name = get_active_connection_name()
        ip4conf = get_connection(act_con_name)
        ip4add = get_ip_address(ip4conf)
        return ip4add
    except Exception:
        print('Network manager not active probably')
    return None

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
    spec = props.get("Ip4Config")
    return str(spec)

def get_ip_address(path):
    """get address"""
    bus_obj = get_bus_object("org.freedesktop.NetworkManager", path)
    props_iface = dbus.Interface(bus_obj, dbus_interface='org.freedesktop.DBus.Properties')
    props = props_iface.GetAll("org.freedesktop.NetworkManager.IP4Config")
    address = props.get("AddressData")
    return str(address[0].get('address'))

def print_all_props(props):
    """print props"""
    for prop in props:
        val = str(props.get(prop))
        print(f'{prop}={val}')

if __name__ == "__main__":
    print(get_state())
