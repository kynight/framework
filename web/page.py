#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from .expected_conditions import *
from selenium.common.exceptions import *
from framework.web import Browser, Wait
from framework.utils import logger

class BasePage(object):
    def __init__(self, driver=None, opened=False):
        self.driver = driver
        self.wait = Wait(self.driver, timeout=5)
        if not opened:
            self.open()

    def open(self):
        """针对页面跳转情形，由于页面已经打开，只需要一个依附动作"""
        if self.url is None:
            logger.error("please enter the url !")
        self.driver.get(self.url)

    @property
    def current_window(self):
        return self.driver.current_window_handle

    @property
    def window_handles(self):
        return self.driver.window_handles

    @property
    def title(self):
        return self.driver.title

    @property
    def page_source(self):
        return self.driver.page_source

    @property
    def current_url(self):
        return self.driver.current_url

    def set_implicitly_wait(self, seconds=5):
        self.driver.implicitly_wait(seconds)

    def set_script_timeout(self, seconds=30):
        self.driver.set_script_timeout(seconds)

    def set_page_load_timeout(self, secongs=10):
        self.driver.set_page_load_timeout(seconds)

    ############################# title ################################
    def title_should_is(self,title):
        self.wait.until(EC.title_is(title))

    def title_should_change(self, title):
        self.wait.until_not(EC.title_is(title))

    def title_should_contains(self,title):
        self.wait.until(EC.title_contains(title))

    ############################# title ################################
    def url_should_is(self, url):
        self.wait.until(url_is(url))

    def url_should_change(self, url):
        self.wait.until_not(url_is(url))

    def url_should_contains(self, url):
        self.wait.until(url_contains(url))

    ############################# text & value ################################
    def check_text_to_be_present_in_element(self, locator, text):
        self.wait.until(EC.text_to_be_present_in_element(locator, text))

    def check_text_to_be_present_in_element_value(self, locator, text):
        self.wait.until(EC.text_to_be_present_in_element_value(locator, text))

    ############################# selected ################################
    def check_element_to_be_selected(self, element):
        self.wait.until(EC.element_to_be_selected(element))

    # def element_located_to_be_selected(self, locator):
    #     self.wait.until(EC.element_located_to_be_selected(locator))

    def check_element_selection_state_to_be(self, element, is_selected):
        self.wait.until(EC.element_selection_state_to_be(element, is_selected))

    # def element_located_selection_state_to_be(self, locator, is_selected):
    #     self.wait.until(EC.element_located_selection_state_to_be(locator, is_selected))

    ############################# find_element ################################
    def find_element(self, locator):
        """ 保证元素存在 """
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_element_with_visibility(self, locator):
        """ 保证元素存在且可见"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_element_can_be_clickable(self, locator):
        """针对 button/input/checkbox/radio/select 可操作"""
        return self.wait.until(EC.element_to_be_clickable(locator))

    ############################# check_elements ################################
    def element_should_be_visible(self, element):
        self.wait.until(EC.visibility_of(element))

    def element_should_not_be_visible(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    def text_to_be_present_in_element(self, locator):
        return self.wait.until(EC.text_to_be_present_in_element(locator))

    def text_to_be_present_in_element_value(self, locator):
        return self.wait.until(EC.text_to_be_present_in_element_value(locator))

    def element_should_be_staleness(self, element):
        self.wait.until(EC.staleness_of(element))

    ############################# find_elements ################################
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def visibility_of_any_elements_located(self, locator):
        return self.wait.until(EC.visibility_of_any_elements_located(locator))

    def visibility_of_all_elements_located(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    ############################# windows ################################
    def check_number_of_windows(self, num_windows):
        self.wait.until(EC.number_of_windows_to_be(num_windows))

    def check_new_window_is_opened(self, current_handles):
        self.wait.until(EC.new_window_is_opened(current_handles))

    def switch_to_window(self, partial_url='', partial_title=''):
        """切换窗口
            如果窗口数<3,不需要传入参数，切换到当前窗口外的窗口；
            如果窗口数>=3，则需要传入参数来确定要跳转到哪个窗口
        """
        all_windows = self.driver.window_handles
        if len(all_windows) == 1:
            logger.warning('only one window!')
        elif len(all_windows) == 2:
            other_window = all_windows[1 - all_windows.index(self.current_window)]
            self.driver.switch_to.window(other_window)
        else:
            for window in all_windows:
                self.driver.switch_to.window(window)
                if partial_url in self.driver.current_url or partial_title in self.driver.title:
                    break
        logger.debug(self.driver.current_url, self.driver.title)

    ############################# frame ################################
    def switch_to_frame(self, frame_locator):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(frame_locator))

    def switch_to_parent_frame(self):
        self.driver.switch_to.parent_frame()

    def switch_to_top_frame(self):
        self.driver.switch_to.default_content()

    ############################# alert ################################
    def switch_to_alert(self):
        """
        text
        dismiss()
        accept()
        send_keys(self, keysToSend)
        """
        return self.wait.until(EC.alert_is_present())

    ######################################################################
    def switch_to_active_element(self):
        return self.driver.switch_to_active_element

    def close(self):
        self.driver.close()

    def refresh(self):
        self.driver.refresh()

    ######################################################################
    def input_text(self, locator, text):
        element = self.find_element_can_be_clickable(locator)
        element.clear()
        element.send_keys(text)

    # page 类没有此方法就去 browser 中寻找
    def __getattr__(self, attr):
        return object.__getattribute__(self.driver, attr)

if __name__== "__main__":
    page = BasePage("chrome", "https://www.bing.com")
    from selenium.webdriver.common.by import By
    page.switch_to_frame((By.ID, "test"))
    time.sleep(10)
    page.quit()
