#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
cpu mem
"""
from threading import Thread
from time import sleep
from math import floor
import psutil
from helpers import status_state

DISK_UCODE = u"\U0001F5AB"

STATE = status_state.Status.get_instance()

def format_b_to_gb(numb):
    """b to gb"""
    numgb = numb / 1024 / 1024 / 1024
    return round(numgb, 1)

def get_state():
    """init"""
    cpu = floor(psutil.cpu_percent())
    virt_mem = psutil.virtual_memory()
    total = format_b_to_gb(virt_mem.total)
    used = format_b_to_gb(virt_mem.used)
    disk = psutil.disk_usage('/').percent
    cpu_mem_state = f'{cpu}% {used}/{total}gb {DISK_UCODE}{disk}%'
    return cpu_mem_state
        
class CpuRamDisk(Thread):
    """time class"""
    def __init__(self):
        Thread.__init__(self)
        self.name = "CPU and memory thread"
        self.daemon = True

    def run(self):
        """init"""
        while True:
            current_state = get_state()
            STATE.set_cpu_ram_disk_state(current_state)
            sleep(5)

if __name__ == "__main__":
    print(get_state())
