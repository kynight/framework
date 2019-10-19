#!/usr/bin/env python
# -*- coding: utf-8 -*-
import types

def regist2class(method, cls):
    if not isinstance(method, types.FunctionType):
        raise Exception("The method must be a function")
    if not cls.__dict__:
        raise Exception("The cls can't support add custom method !")
    if method in cls.__dict__:
        raise Exception("The method already exists !")
    else:
        setattr(cls, method.__name__, method)
