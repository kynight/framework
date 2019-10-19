#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from . import PROJECT_PATH

def collect_case():
    """用例收集，只有一层嵌套，创建工程时请使用 setup.py 一键生成"""
    ret = []
    files = os.listdir(PROJECT_PATH)
    for name in files:
        if "." in name:
            continue
        elif name == "__pycache__":
            continue
        else:
            dir_path = os.path.join(PROJECT_PATH, name, "testcase")
            if os.path.isdir(dir_path):
                ret.append(dir_path)
            else:
                continue
    return ret
