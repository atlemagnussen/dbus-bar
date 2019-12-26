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
        self.__running__ = True

    def run(self):
        """init"""
        while self.__running__:
            time_state = datetime.now().strftime("%Y-%m-%d %H:%M")
            STATE.set_time(time_state)
            sleep(5)

    def stop(self):
        """stop"""
        self.__running__ = False
