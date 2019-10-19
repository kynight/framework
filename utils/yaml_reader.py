#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import yaml

class YamlReader(object):
    def __init__(self, yaml_path):
        if os.path.exists(yaml_path):
            self.path = yaml_path
        else:
            raise FileNotFoundError('配置文件不存在！')
        self._data = None

    @property
    def data(self):
        if not self._data:
            with open(self.path, encoding="utf-8") as f:
                self._data = list(yaml.safe_load_all(f))
        return self._data
