#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Testing dbus with pulseaudio"""
import os
import dbus
# import math
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib

from helpers import status_state

SERVICE = 'org.PulseAudio1'
LPATH = '/org/pulseaudio/server_lookup1'
LNAME = 'org.PulseAudio.ServerLookup1'
FDPROP = 'org.freedesktop.DBus.Properties'
MAIN = 'org.PulseAudio.Core1.Device'
IFACE = 'org.PulseAudio.Core1'
STATSIG = 'StateUpdated'
VOLSIG = 'VolumeUpdated'
MUTESIG = 'MuteUpdated'

STATE = status_state.Status()

def pulse_bus_address():
    """address"""
    if 'PULSE_DBUS_SERVER' in os.environ:
        address = os.environ['PULSE_DBUS_SERVER']
    else:
        bus = dbus.SessionBus()
        server_lookup = bus.get_object(SERVICE, LPATH)
        address = server_lookup.Get(LNAME, "Address", dbus_interface=FDPROP)
        print(address)

    return address

def sig_handler_state(state):
    """handler"""
    print("State changed to %s" % state)
    if state == 0:
        print("Pulseaudio running.")
    elif state == 1:
        print("Pulseaudio idle.")
    elif state == 2:
        print("Pulseaudio suspended")

def sig_handler_vol(vol):
    """handler"""
    perc = (vol[0] / 65536) * 100
    STATE.set_vol(round(perc))

def sig_handler_mute(muted):
    """handler"""
    STATE.set_vol_muted(muted)

def init():
    """init"""
    DBusGMainLoop(set_as_default=True)
    pulse_bus = dbus.connection.Connection(pulse_bus_address())
    pulse_core = pulse_bus.get_object(object_path='/org/pulseaudio/core1')
    pulse_core.ListenForSignal(MAIN + '.' + STATSIG, dbus.Array(signature='o'), dbus_interface=IFACE)
    pulse_core.ListenForSignal(MAIN + '.' + VOLSIG, dbus.Array(signature='o'), dbus_interface=IFACE)
    pulse_core.ListenForSignal(MAIN + '.' + MUTESIG, dbus.Array(signature='o'), dbus_interface=IFACE)
    interface = dbus.Interface(pulse_bus, dbus_interface='org.PulseAudio.Core1')

    loop = GLib.MainLoop()

    pulse_bus.add_signal_receiver(sig_handler_state, 'StateUpdated')
    pulse_bus.add_signal_receiver(sig_handler_vol, 'VolumeUpdated')
    pulse_bus.add_signal_receiver(sig_handler_mute, 'MuteUpdated')
    print("interface connected to Seeked signal, now loop")
    try:
        loop.run()
    except KeyboardInterrupt:
        loop.quit()

if __name__ == "__main__":
    init()
