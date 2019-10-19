#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from framework.utils.yaml_reader import YamlReader

__all__= ["BASE_PATH", "PROJECT_PATH", "CONFIG_PATH", "DRIVER_PATH", "LOG_PATH", "REPORT_PATH", "config"]

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
PROJECT_PATH = os.path.join(BASE_PATH, 'project')
CONFIG_PATH = os.path.join(BASE_PATH, 'config', 'config.yml')
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')

class Config(object):

    # __instance = None
    # def __new__(cls, *args, **kwargs):
    #     if cls.__instance is None:
    #         cls.__instance = object.__new__(cls)
    #     return cls.__instance

    def __init__(self, config_path=CONFIG_PATH):
        self.config = YamlReader(config_path).data

    def get(self, element, index=0):
        return self.config[index].get(element, "undefined")

config = Config(config_path=CONFIG_PATH)

if __name__ == "__main__":
    import pprint
    pprint.pprint(config.config)

