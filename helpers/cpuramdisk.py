#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
cpu mem
"""
from threading import Thread
from time import sleep
from math import floor
import psutil
from helpers import status_state, colors

DISK_UCODE = u"\U0001F5AB"
CPU_UCODE = "☢"
RAM_UCODE = u"\U0001F5A5"
DEGREE_UCODE = u"\u2103"

STATE = status_state.Status.get_instance()

def format_b_to_gb(numb):
    """b to gb"""
    numgb = numb / 1024 / 1024 / 1024
    return round(numgb, 1)

def pct_color_text(pct, text):
    """pct to color"""
    if pct > 80:
        return f"{colors.FAIL}{text}{colors.RESET}"
    if pct > 50:
        return f"{colors.WARN}{text}{colors.RESET}"
    return text

def get_state():
    """init"""
    cpu_pct = psutil.cpu_percent()
    cpu_state = pct_color_text(cpu_pct, f'{CPU_UCODE}{floor(cpu_pct)}%')

    temps = psutil.sensors_temperatures()
    try:
        cpu_temp = temps['coretemp'][0].current
        cpu_state = f'{cpu_state} {floor(cpu_temp)}{DEGREE_UCODE}'
    except Exception:
        cpu_temp = f'n/a'

    virt_mem = psutil.virtual_memory()
    mem_pct = (virt_mem.used/virt_mem.total) * 100
    mem_state = pct_color_text(mem_pct, f'{RAM_UCODE}{floor(mem_pct)}%')

    disk_pct = psutil.disk_usage('/').percent
    disk_state = pct_color_text(disk_pct, f'{DISK_UCODE}{floor(disk_pct)}%')

    cpu_mem_state = f'{cpu_state} {mem_state} {disk_state}'
    return cpu_mem_state

class CpuRamDisk(Thread):
    """crd class"""
    def __init__(self):
        Thread.__init__(self)
        self.name = "CPU and memory thread"
        self.daemon = True
        self.__running__ = True

    def run(self):
        """init"""
        while self.__running__:
            current_state = get_state()
            STATE.set_cpu_ram_disk_state(current_state)
            sleep(5)
    def stop(self):
        """stop"""
        self.__running__ = False

if __name__ == "__main__":
    print(get_state())
