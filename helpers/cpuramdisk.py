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
CPU_UCODE = "☢"
RAM_UCODE = "🐏"

STATE = status_state.Status.get_instance()

def format_b_to_gb(numb):
    """b to gb"""
    numgb = numb / 1024 / 1024 / 1024
    return round(numgb, 1)

def get_state():
    """init"""
    cpu_pct = psutil.cpu_percent()
    cpu_state = f'{CPU_UCODE}{floor(cpu_pct)}%'

    virt_mem = psutil.virtual_memory()
    mem_pct = (virt_mem.used/virt_mem.total) * 100
    mem_state = f'{RAM_UCODE}{floor(mem_pct)}%'

    disk_pct = psutil.disk_usage('/').percent
    disk_state = f'{DISK_UCODE}{floor(disk_pct)}%'

    cpu_mem_state = f'{cpu_state} {mem_state} {disk_state}'
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
