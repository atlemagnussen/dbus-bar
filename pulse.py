#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Testing dbus with pulseaudio"""
import os
import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib

def pulse_bus_address():
    """address"""
    if 'PULSE_DBUS_SERVER' in os.environ:
        address = os.environ['PULSE_DBUS_SERVER']
    else:
        bus = dbus.SessionBus()
        server_lookup = bus.get_object("org.PulseAudio1", "/org/pulseaudio/server_lookup1")
        address = server_lookup.Get("org.PulseAudio.ServerLookup1", "Address", dbus_interface="org.freedesktop.DBus.Properties")
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
    print("Volume changed to %s" % vol)

def sig_handler_mute(muted):
    """handler"""
    print("Mute changed to %s" % muted)

def init():
    """init"""
    DBusGMainLoop(set_as_default=True)
    pulse_bus = dbus.connection.Connection(pulse_bus_address())
    pulse_core = pulse_bus.get_object(object_path='/org/pulseaudio/core1')
    pulse_core.ListenForSignal('org.PulseAudio.Core1.Device.StateUpdated', dbus.Array(signature='o'), dbus_interface='org.PulseAudio.Core1')
    pulse_core.ListenForSignal('org.PulseAudio.Core1.Device.VolumeUpdated', dbus.Array(signature='o'), dbus_interface='org.PulseAudio.Core1')
    pulse_core.ListenForSignal('org.PulseAudio.Core1.Device.MuteUpdated', dbus.Array(signature='o'), dbus_interface='org.PulseAudio.Core1')
    #interface = dbus.Interface(bus_object, dbus_interface=INTERFACENAME)

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
