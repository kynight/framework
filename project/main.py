#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import time
import unittest
from framework.utils import config, logger, HTMLTestRunner, RotatingFileHandler,REPORT_PATH, PROJECT_PATH
from framework.utils import collect_case

def generate_suite(case_path):
    suite = unittest.TestSuite()
    loader = unittest.defaultTestLoader
    for path in case_path:
        suite.addTest(loader.discover(start_dir=path, top_level_dir=PROJECT_PATH))
    return suite

def run():
    suite = generate_suite(collect_case())
    if not os.path.exists(REPORT_PATH):
        os.makedirs(REPORT_PATH)
    report_path = os.path.join(REPORT_PATH, "report.html")
    backupCount = config.get("report").get("backup", 10)
    report_title = config.get("report").get("title", "Test Report")
    report_description = config.get("report").get("description", "Test Description")
    fileHandler = RotatingFileHandler(filename=report_path,backupCount=int(backupCount))
    fileName = fileHandler.emit()
    with open(fileName, "w", encoding="utf-8") as f:
        runner = HTMLTestRunner(stream=f, title=report_title, description=report_description)
        result = runner.run(suite)
    logger.info("generate report to %s" % (os.path.basename(fileName)))
    return result

def email(title, message, report_path):
    """ 使用Jenkins 集成，本机就不需要配置了"""
    config = ConfigReader()
    server = config.get("email","server")
    sender = config.get("email","sender")
    password = config.get("email","password")
    receiver = config.get("email","receiver")
    mail = Email(title=title,
                 message=message,
                 server=server,
                 sender=sender,
                 password=password,
                 receiver=receiver,
                 path=report_path)
    mail.send()

if __name__ == "__main__":
    logger.info("******** TEST START ********")
    result = run()
    if result.error_count or result.failure_count:
        raise Exception("本次构建过程存在失败用例")
    logger.info("********* TEST END *********")
