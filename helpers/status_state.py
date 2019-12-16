# -*- coding: utf-8 -*-
"""module for status bar state"""
from subprocess import call
VOL_UCODE = u"\U0001F50A"
VOL_MUTED_UCODE = u"\U0001F507"
NETWORK_UCODE = u"\U0001F5A7"
POWER_UCODE = u"\U0001F5F2"
TIME_UCODE = u"\U0001F550"

class Status:
    """status state"""
    __instance = None
    @staticmethod
    def get_instance():
        """ Static access method. """
        if Status.__instance is None:
            Status()
        return Status.__instance

    def __init__(self):
        """ Virtually private constructor. """
        self.__vol = 0
        self.__vol_muted = False
        self.__network = 'disconnected'
        self.__time__ = ''
        self.__bat__ = '00%-'
        if Status.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Status.__instance = self

    def set_vol(self, vol):
        """setter vol"""
        self.__vol = vol
        self.set_bar()

    def set_vol_muted(self, muted):
        """set muted"""
        self.__vol_muted = bool(muted == 1)
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

    def set_network(self, network):
        """set network"""
        self.__network = network
        self.set_bar()

    def state_net(self):
        """state net"""
        return f'{NETWORK_UCODE}{self.__network}'

    def set_time(self, time):
        """time stat"""
        self.__time__ = time
        self.set_bar()

    def set_bat(self, bat):
        """bat set"""
        self.__bat__ = bat
        self.set_bar()

    def state_time(self):
        """time"""
        return f'{TIME_UCODE}{self.__time__}'

    def state_bat(self):
        """bat"""
        if self.__bat__ is None:
            return None
        return f'{POWER_UCODE}{self.__bat__}'

    def state(self):
        """get full state"""
        vol = self.state_vol()
        net = self.state_net()
        bat = self.state_bat()
        time = self.state_time()
        full_state = f'{net} '
        if bat is not None:
            full_state += f'{bat} '
        full_state += f'{vol} {time} '
        return full_state

    def set_bar(self):
        """set bar with state"""
        status = self.state()
        print(status)
        #call(['xsetroot', '-name', status], shell=False)
