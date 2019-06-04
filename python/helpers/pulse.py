#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Testing dbus with pulseaudio"""
import os
import dbus
# from pulsectl import Pulse
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

STATE = status_state.Status.get_instance()

class PulseAudio:
    """pulse class"""
    def __init__(self):
        self.pulse_bus = dbus.connection.Connection(self.pulse_bus_address())
        try:
            print("init pulse audio dbus")
            pulse_core = self.pulse_bus.get_object(object_path='/org/pulseaudio/core1')
            pulse_core.ListenForSignal(MAIN + '.' + STATSIG, dbus.Array(signature='o'), dbus_interface=IFACE)
            pulse_core.ListenForSignal(MAIN + '.' + VOLSIG, dbus.Array(signature='o'), dbus_interface=IFACE)
            pulse_core.ListenForSignal(MAIN + '.' + MUTESIG, dbus.Array(signature='o'), dbus_interface=IFACE)

            self.pulse_bus.add_signal_receiver(self.sig_handler_state, 'StateUpdated')
            self.pulse_bus.add_signal_receiver(self.sig_handler_vol, 'VolumeUpdated')
            self.pulse_bus.add_signal_receiver(self.sig_handler_mute, 'MuteUpdated')
        except Exception as ex:
            print(ex)

    # def initial_volume(self):
    #    """initial volume and mute"""
    #    pulse_ctl = Pulse()
    #    sinks = pulse_ctl.sink_list()
    #    sink = sinks[0]

    #    STATE.set_vol_muted(sink.mute)
    #    STATE.set_vol(round(sink.volume.value_flat * 100))

    def pulse_bus_address(self):
        """address"""
        if 'PULSE_DBUS_SERVER' in os.environ:
            address = os.environ['PULSE_DBUS_SERVER']
        else:
            bus = dbus.SessionBus()
            server_lookup = bus.get_object(SERVICE, LPATH)
            address = server_lookup.Get(LNAME, "Address", dbus_interface=FDPROP)

        return address

    def sig_handler_state(self, state):
        """handler"""
        print("State changed to %s" % state)
        if state == 0:
            print("Pulseaudio running.")
        elif state == 1:
            print("Pulseaudio idle.")
        elif state == 2:
            print("Pulseaudio suspended")

    def sig_handler_vol(self, vol):
        """handler"""
        perc = (vol[0] / 65536) * 100
        STATE.set_vol(round(perc))

    def sig_handler_mute(self, muted):
        """handler"""
        STATE.set_vol_muted(muted)

# if __name__ == "__main__":
#    init()
