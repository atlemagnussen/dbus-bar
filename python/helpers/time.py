#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""time bar"""
from threading import Thread
from time import sleep
from datetime import datetime
from helpers import status_state

STATE = status_state.Status.get_instance()
class Time(Thread):
    """time class"""
    def __init__(self):
        Thread.__init__(self)
        self.name = "Time thread"
        self.daemon = True

    def run(self):
        """init"""
        while True:
            time_state = datetime.now().strftime("%Y-%m-%d %H:%M")
            STATE.set_time(time_state)
            sleep(5)
