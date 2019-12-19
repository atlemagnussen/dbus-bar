# -*- coding: utf-8 -*-
"""colors"""
from helpers import config_bar

WARN = '\033[93m'
FAIL = '\033[91m'
RESET = '\033[0m'

CFG = config_bar.get_config()
if not CFG['useColors']:
    WARN = ''
    FAIL = ''
    RESET = ''
