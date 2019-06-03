"""upower dbus"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dbus
from time import sleep
from helpers import status_state

STATE = status_state.Status.get_instance()

def init():
    """init"""
    while True:
        bat = get_state()
        STATE.set_bat(bat)
        sleep(10)


def get_state():
    """battery state"""
    sys_bus = dbus.SystemBus()
    bus_obj = sys_bus.get_object("org.freedesktop.UPower", "/org/freedesktop/UPower/devices/DisplayDevice")
    props_iface = dbus.Interface(bus_obj, dbus_interface='org.freedesktop.DBus.Properties')
    props = props_iface.GetAll("org.freedesktop.UPower.Device")
    perc = round(props.get("Percentage"))
    state = props.get("State")
    if state == 1:
        charge = '+'
    else:
        charge = '-'
    return f'{perc}%{charge}'


if __name__ == "__main__":
    print(get_state())