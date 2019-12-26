#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Testing dbus with pulseaudio"""
import os
from time import sleep
import dbus
from helpers import status_state
from threading import Thread

SERVICE = 'org.PulseAudio1'
LPATH = '/org/pulseaudio/server_lookup1'
LNAME = 'org.PulseAudio.ServerLookup1'
FDPROP = 'org.freedesktop.DBus.Properties'
MAIN = 'org.PulseAudio.Core1.Device'
IFACE = 'org.PulseAudio.Core1'
STATSIG = 'StateUpdated'
VOLSIG = 'VolumeUpdated'
MUTESIG = 'MuteUpdated'

STATE = status_state.Status.get_instance()

class PulseAudio(Thread):
    """pulse class"""
    def __init__(self):
        Thread.__init__(self)
        self.name = "Pulse Init thread"
        self.daemon = True
        self.__is_initialized__ = False
        self.__running__ = True

    def run(self):
        """run"""
        while self.__is_initialized__ is not True and self.__running__:
            self.__is_initialized__ = self.init()
            sleep(10)

    def stop(self):
        """stop"""
        self.__running__ = False

    def init(self):
        """init"""
        try:
            print("init pulse audio dbus")
            self.pulse_bus = dbus.connection.Connection(pulse_bus_address())
            pulse_core = self.pulse_bus.get_object(object_path='/org/pulseaudio/core1')
            pulse_core.ListenForSignal(MAIN + '.' + STATSIG, dbus.Array(signature='o'), dbus_interface=IFACE)
            pulse_core.ListenForSignal(MAIN + '.' + VOLSIG, dbus.Array(signature='o'), dbus_interface=IFACE)
            pulse_core.ListenForSignal(MAIN + '.' + MUTESIG, dbus.Array(signature='o'), dbus_interface=IFACE)

            self.pulse_bus.add_signal_receiver(sig_handler_state, 'StateUpdated')
            self.pulse_bus.add_signal_receiver(sig_handler_vol, 'VolumeUpdated')
            self.pulse_bus.add_signal_receiver(sig_handler_mute, 'MuteUpdated')
            return True
        except Exception as ex:
            return False

def pulse_bus_address():
    """address"""
    if 'PULSE_DBUS_SERVER' in os.environ:
        address = os.environ['PULSE_DBUS_SERVER']
    else:
        bus = dbus.SessionBus()
        server_lookup = bus.get_object(SERVICE, LPATH)
        address = server_lookup.Get(LNAME, "Address", dbus_interface=FDPROP)

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
