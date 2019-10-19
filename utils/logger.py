#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import logging
from logging.handlers import TimedRotatingFileHandler
from framework.utils import config, LOG_PATH

class Logger(object):

    def __init__(self):
        logger_name = config.get("log").get("name", "framework")
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        self.init_log_message()

    def init_log_message(self):
        log_config = config.get("log")
        if not os.path.exists(LOG_PATH):
            os.makedirs(LOG_PATH)
        file_name = time.strftime("%Y-%m-%d", time.localtime()) + ".log"
        self.log_file = os.path.join(LOG_PATH, file_name)
        self.when = log_config["when"]
        self.interval = log_config["interval"]
        self.backupCount = log_config["backup"]
        self.console_output_level = log_config["console_level"]
        self.file_output_level = log_config["file_level"]
        self.formater = logging.Formatter(log_config["formater"])

    def get_logger(self):
        if not self.logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formater)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)
            file_handler = TimedRotatingFileHandler(self.log_file,
                                                            when=self.when,
                                                            interval=int(self.interval),
                                                            backupCount=int(self.backupCount),
                                                            delay=True,
                                                            encoding="utf-8")
            file_handler.setFormatter(self.formater)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger


logger = Logger().get_logger()

if __name__ == "__main__":
    logger.info(__file__)
