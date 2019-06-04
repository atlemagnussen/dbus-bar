"""upower dbus"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
from threading import Thread
import dbus
from helpers import status_state

STATE = status_state.Status.get_instance()
MAIN_NAME = "org.freedesktop.UPower"
DD_PATH = "/org/freedesktop/UPower/devices/DisplayDevice"
DBUS_PROPS = "org.freedesktop.DBus.Properties"
class Power(Thread):
    """power class"""
    def __init__(self):
        Thread.__init__(self)
        self.name = "Time thread"
        self.daemon = True
        self.__counter_none__ = 0

    def run(self):
        """run"""
        while self.__counter_none__ < 5:
            bat = get_state()
            if bat is None:
                self.__counter_none__ += 1
            STATE.set_bat(bat)
            sleep(10)

def get_state():
    """battery state"""
    sys_bus = dbus.SystemBus()
    bus_obj = sys_bus.get_object(MAIN_NAME, DD_PATH)
    props_iface = dbus.Interface(bus_obj, dbus_interface=DBUS_PROPS)
    props = props_iface.GetAll("org.freedesktop.UPower.Device")
    perc = round(props.get("Percentage"))
    state = props.get("State")
    if state == 0:
        return None
    if state == 1:
        charge = '+'
    else:
        charge = '-'
    return f'{perc}%{charge}'

def print_all_props(props):
    """print props"""
    for prop in props:
        val = str(props.get(prop))
        print(f'{prop}={val}')

if __name__ == "__main__":
    print(f'state={get_state()}')
