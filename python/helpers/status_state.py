# -*- coding: utf-8 -*-
"""module for status bar state"""
from subprocess import call
VOL_UCODE = u"\U0001F50A"
VOL_MUTED_UCODE = u"\U0001F507"

class Status:
    """status state"""
    def __init__(self):
        self.__vol = 0
        self.__vol_muted = False

    def set_vol(self, vol):
        """setter vol"""
        self.__vol = vol
        self.set_bar()

    def set_vol_muted(self, muted):
        """set muted"""
        if muted == 1:
            self.__vol_muted = True
        else:
            self.__vol_muted = False
        self.set_bar()

    def state_vol(self):
        """state string vol"""
        vol_state = ""
        if self.__vol_muted:
            vol_state = VOL_MUTED_UCODE
        else:
            vol_state = VOL_UCODE
        vol_state = f'{vol_state}{self.__vol}%'
        return vol_state

    def state(self):
        """get full state"""
        vol = self.state_vol()
        return f'{vol}'

    def set_bar(self):
        """set bar with state"""
        status = self.state()
        print(status)
        call(['xsetroot', '-name', status], shell=False)
