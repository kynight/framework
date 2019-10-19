#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import unittest
from framework.web import Browser
from framework.project.Email_163.page.LoginPage import Login
from framework.project.Email_163.page.HomePage import Home
from framework.utils import logger

def setUpModule():
    logger.info(">>>> run case: %s" % (os.path.split(os.path.abspath(__file__))[1]))

class Email_163(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Browser(browser_type="chrome")
        cls.page = Login(cls.driver)

    def setUp(self):
        time.sleep(1)

    # @unittest.skip("无条件放弃")
    # def test_1_login_without_usr_pw(self, username="", password=""):
    #     """演示用，实际编程时自动化用例优先覆盖与后台存在数据交互的功能，像这种单纯的前端检测，手工即可"""
    #     self.page.login_without_usr_pw(username=username, password=password)

    # def test_2_login_without_usr(self, username="", password="test"):
    #     """演示用，实际编程时自动化用例优先覆盖与后台存在数据交互的功能，像这种单纯的前端检测，手工即可"""
    #     self.page.login_without_usr(username=username, password=password)

    # def test_3_login_without_pw(self, username="test", password=""):
    #     """演示用，实际编程时自动化用例优先覆盖与后台存在数据交互的功能，像这种单纯的前端检测，手工即可"""
    #     self.page.login_without_pw(username=username, password=password)

    # def test_4_login_incorrect_usr_or_pw(self, username="test", password="test_wrong"):
    #     self.page.login_incorrect_usr_or_pw(username=username, password=password)

    def test_5_login_and_write_email(self, username="test", password="test"):
        self.page.login_sucess(username=username, password=password)
        self.page = Home(self.driver, opened=True)
        self.page.write_email()

    def tearDown(self):
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

def tearDownModule():
    logger.info("<<<< exit case: %s" % (os.path.split(os.path.abspath(__file__))[1]))

if __name__ == '__main__':
    unittest.main()

