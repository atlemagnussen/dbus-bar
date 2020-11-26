"""network psutil"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psutil

ifad = psutil.net_if_addrs()
ipwlan = ifad["wlan0"][0].address
print(f'ipwlan={ipwlan}')
