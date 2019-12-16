# -*- coding: utf-8 -*-
"""module for status bar state"""
from subprocess import call
from sys import stdout
import yaml

VOL_UCODE = u"\U0001F50A"
VOL_MUTED_UCODE = u"\U0001F507"
NETWORK_UCODE = u"\U0001F5A7"
POWER_UCODE = u"\U0001F5F2"
TIME_UCODE = u"\U0001F550"

with open("config.yml", 'r') as ymlfile:
    CFG = yaml.load(ymlfile)

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
        self.__cpu_ram_disk__ = ''

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

    def set_cpu_ram_disk_state(self, cpu_ram_disk):
        """cpu_and_mem"""
        self.__cpu_ram_disk__ = cpu_ram_disk

    def cpu_ram_disk_state(self):
        """cpu_ram_mem_state"""
        return self.__cpu_ram_disk__

    def state(self):
        """get_full_state"""
        vol = self.state_vol()
        net = self.state_net()
        bat = self.state_bat()
        time = self.state_time()
        crd = self.cpu_ram_disk_state()
        full_state = f'{crd} {net} '
        if bat is not None:
            full_state += f'{bat} '
        full_state += f'{vol} {time} '
        return full_state

    def set_bar(self):
        """set bar with state"""
        status = self.state()
        self.write(status)
        if CFG['writeToXRoot']:
            call(['xsetroot', '-name', status], shell=False)

    def write(self, data):
        stdout.write('%s\n' % data)
        stdout.flush()

