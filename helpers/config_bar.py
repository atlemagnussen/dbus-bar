#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
config
"""
import os
import yaml

CWD = os.getcwd()
CFG_PATH = '/home/atle/.config/dbusbar.yml'

DEFAULT_CONFIG = dict([
    ('writeToXRoot', False)
])

def get_config():
    """get config public method"""
    try:
        cfg_file = read_yaml_file(CFG_PATH)
        return cfg_file
    except FileNotFoundError:
        return DEFAULT_CONFIG

def read_yaml_file(file_path):
    """read file"""
    with open(file_path, 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
    return cfg

if __name__ == "__main__":
    print(get_config())
