#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""time bar"""
from time import sleep
from datetime import datetime
from helpers import status_state

STATE = status_state.Status.get_instance()

def init():
    """init"""
    while True:
        time_state = datetime.now().strftime("%Y-%m-%d %H:%M")
        STATE.set_time(time_state)
        sleep(5)
