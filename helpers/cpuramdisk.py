#!/usr/bin/env python
"""
cpu mem
"""
from threading import Thread
from time import sleep
from math import floor
import psutil
from helpers import status_state

STATE = status_state.Status.get_instance()

def format_b_to_gb(numb):
    """b to gb"""
    numgb = numb / 1024 / 1024 / 1024
    return round(numgb,1)

class CpuRamDisk(Thread):
    """time class"""
    def __init__(self):
        Thread.__init__(self)
        self.name = "CPU and memory thread"
        self.daemon = True

    def run(self):
        """init"""
        while True:
            cpu = floor(psutil.cpu_percent())
            virt_mem = psutil.virtual_memory()
            total = format_b_to_gb(virt_mem.total)
            used = format_b_to_gb(virt_mem.used)
            cpu_mem_state = f'cpu {cpu}% ram {used}/{total} gb'
            STATE.set_cpu_ram_disk_state(cpu_mem_state)
            sleep(5)
