#!/usr/bin/env python
"""doc string for dbus-bar for dwm"""
# -*- coding: utf-8 -*-

def get_network_state(code):
    """network state"""
    print(f'statecode={code}')
    if code <= 20:
        network_state = "disconnected"
    elif 20 < code < 70:
        network_state = "connecting"
    else:
        network_state = "192.168.1.145"
    print(network_state)

if __name__ == "__main__":
    get_network_state(20)
    get_network_state(30)
    get_network_state(70)
