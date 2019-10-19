#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import unittest
from framework.web import Browser
from framework.project.Baidu.page.SearchPage import Search
from framework.utils import logger

def setUpModule():
    logger.info(">>>> run case: %s" % (os.path.split(os.path.abspath(__file__))[1]))

class BaiduSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Browser(browser_type="chrome")
        cls.page = Search(cls.driver)

    def setUp(self):
        pass

    def test_1_bai_search(self, text="hello world !"):
        self.page.input(text)

    def tearDown(self):
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

def tearDownModule():
    logger.info("<<<< exit case: %s" % (os.path.split(os.path.abspath(__file__))[1]))

if __name__ == '__main__':
    unittest.main()

