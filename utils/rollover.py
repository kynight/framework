#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
from stat import ST_MTIME
from framework.utils import logger
import traceback

class Hander(object):
    def __init__(self, filename):
        self.baseFilename = os.path.abspath(filename)

    def rotation_filename(self, default_name):
        result = default_name
        return result

    def rotate(self, source, dest):
        if os.path.exists(source):
            os.rename(source, dest)

    def emit(self):
        try:
            ret = self.doRollover()
            return ret
        except:
            logger.warning(traceback.format_exc())
            return self.baseFilename

class RotatingFileHandler(Hander):
    def __init__(self, filename, backupCount=0):
        super().__init__(filename)
        self.backupCount = backupCount
        self.pattern = "%Y-%m-%d-%H-%M-%S"
        self.splitFileName()

    def splitFileName(self):
        self.dirName, self.baseName = os.path.split(self.baseFilename)
        prefix, suffix = self.baseName.split(".")
        self.prefix = prefix + "_"
        self.suffix = "." + suffix

    def getFilesToDelete(self):
        result = []
        pre_len = len(self.prefix)
        suf_len = -len(self.suffix)
        fileNames = os.listdir(self.dirName)
        for fileName in fileNames:
            if fileName[:pre_len] == self.prefix:
                fp_time = fileName[pre_len: suf_len]
                result.append(os.path.join(self.dirName, fileName))
        result.sort()
        if len(result) < self.backupCount:
            result = []
        else:
            result = result[:len(result) - self.backupCount]
        return result

    def doRollover(self):
        if os.path.exists(self.baseFilename):
            t = os.stat(self.baseFilename)[ST_MTIME]
        else:
            return self.baseFilename
        dfn = self.rotation_filename(self.dirName + "\\" + self.prefix + time.strftime(self.pattern,time.localtime(t)) + self.suffix)
        if os.path.exists(dfn):
            os.remove(dfn)
        self.rotate(self.baseFilename, dfn)
        if self.backupCount > 0:
            for s in self.getFilesToDelete():
                os.remove(s)
        return self.baseFilename
