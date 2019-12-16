#!/usr/bin/env python
"""
cpu mem
"""
import psutil, time

while(True):
    cpu = psutil.cpu_percent()
    print(f'cpu {cpu}%')

    vm = psutil.virtual_memory()
    total = vm.total / 1024 / 1024 / 1024
    print(f'mem total {round(total, 1)}gb')
    used = vm.used / 1024 / 1024 / 1024
    print(f'mem used {round(used, 1)}gb')
    time.sleep(1)
