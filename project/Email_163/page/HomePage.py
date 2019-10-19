#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from framework.web import BasePage
from framework.utils import logger
import time

class HomePage(BasePage):
    def __init__(self, driver, opened=False):
        self.url = "https://mail.163.com/"
        super().__init__(driver, opened)
        self.setup_elements()

    def setup_elements(self):
        """ 当前页面元素定位方式，后续改动只需要在这里更改即可， 定位方式统一使用 loc 开头，元素统一使用 ele 开头"""
        self.loc_shouxin = (By.CSS_SELECTOR, "#dvNavTop ul > li:first-child")
        self.loc_xiexin = (By.CSS_SELECTOR, "#dvNavTop ul > li:last-child")
        self.loc_shoujianren = (By.CSS_SELECTOR, ".dG0 input[class='nui-editableAddr-ipt']")
        self.loc_zhuti = (By.CSS_SELECTOR, ".dG0 input[class='nui-ipt-input']")
        self.loc_fujian = (By.CSS_SELECTOR, "div.by0")
        self.loc_frame_zhengwen = (By.CSS_SELECTOR, "iframe[class='APP-editor-iframe']")
        self.loc_zhengwen = (By.CSS_SELECTOR, ".nui-scroll")
        self.loc_gengduoxuanxiang = (By.CSS_SELECTOR, ".fq0 a")
        self.loc_youjianjiami = (By.CSS_SELECTOR, "div.mT0 .gm0 > span:nth-child(6")
        self.loc_mima = (By.CSS_SELECTOR, ".cq0 .nui-ipt-input")
        self.loc_fasong = (By.CSS_SELECTOR, "footer.jp0 > div:first-child")
        self.loc_fasongchengong = (By.CSS_SELECTOR, "section.sQ1 h1")

class Home(HomePage):

    def __init__(self, driver, opened=False):
        super().__init__(driver, opened)

    def write_email(self):
        self.find_element(self.loc_xiexin).click(sleep=1)
        self.find_element(self.loc_shoujianren).send_keys("test@163.com")
        self.find_element(self.loc_zhuti).send_keys("hello world")
        self.switch_to_frame(self.loc_frame_zhengwen)
        self.find_element(self.loc_zhengwen).send_keys("111111111111111")
        self.switch_to_parent_frame()
        self.find_element(self.loc_gengduoxuanxiang).click(sleep=1)
        self.find_element(self.loc_youjianjiami).click(sleep=1)
        self.find_element(self.loc_mima).send_keys("hahaha")
        # self.find_element(self.loc_gengduoxuanxiang).click(sleep=1)
        self.find_element(self.loc_fasong).click(sleep=1)
        self.find_element_with_visibility(self.loc_fasongchengong)
