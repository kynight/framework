#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from framework.web import BasePage
from framework.utils import logger
import time

class SearchPage(BasePage):
    def __init__(self, driver, opened=False):
        self.url = "https://www.baidu.com/"
        super().__init__(driver, opened)
        self.setup_elements()

    def setup_elements(self):
        """ 当前页面元素定位方式，后续改动只需要在这里更改即可， 定位方式统一使用 loc 开头，元素统一使用 ele 开头"""
        self.loc_input = (By.ID, "kw")
        self.loc_submit = (By.ID, "su")

class Search(SearchPage):
    """ 搜索逻辑类 """
    def __init__(self, driver, opened=False):
        super().__init__(driver, opened)
        self.element_init()

    def element_init(self):
        self.ele_input = self.find_element_can_be_clickable(self.loc_input)
        self.ele_submit = self.find_element_can_be_clickable(self.loc_submit)

    def input(self, text):
        self.ele_input.clear()
        self.ele_input.click(sleep=1)
        self.ele_input.send_keys(text)
        self.ele_submit.click(sleep=1)
        self.url_should_change(self.url)

if __name__ == "__main__":
    from framework.web import Browser
    driver = Browser("chrome")
    try:
        search = Search(driver)
        search.input("hello world !")
        time.sleep(5)
    except Exception as e:
        print(e)
    finally:
        driver.quit()
