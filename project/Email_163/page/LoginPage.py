#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from framework.web import BasePage
from framework.utils import logger
import time

class LoginPage(BasePage):
    def __init__(self, driver, opened=False):
        self.url = "https://mail.163.com/"
        super().__init__(driver, opened)
        self.setup_elements()

    def setup_elements(self):
        """ 当前页面元素定位方式，后续改动只需要在这里更改即可， 定位方式统一使用 loc 开头，元素统一使用 ele 开头"""
        self.loc_normal_frame = (By.CSS_SELECTOR, "iframe[id^=x-URS-iframe]")
        self.loc_appLoginTab = (By.ID, "appLoginTab")
        self.loc_normalLoginTab = (By.ID, "normalLoginTab")
        self.loc_username_input = (By.CSS_SELECTOR, "#login-form input[name=email]")
        self.loc_password_input = (By.CSS_SELECTOR, "#login-form input[name=password]")
        self.loc_login_button = (By.ID, "dologin")
        self.loc_error = (By.CSS_SELECTOR, "#nerror > div.ferrorhead")

class Login(LoginPage):
    """ 登录逻辑类 """
    def __init__(self, driver, opened=False):
        super().__init__(driver, opened)
        self.normal_login_init()

    # only once to check tab
    def normal_login_init(self):
        """ 只演示简单的用户名密码登录操作
        ps: ui自动化逻辑尽量简单，不宜复杂，优先覆盖与后台存在数据交互的核心功能
        """
        self.find_element(self.loc_appLoginTab).set_attribute("style", "display: none")
        self.find_element(self.loc_normalLoginTab).set_attribute("style", "display: block")
        self.switch_to_frame(self.loc_normal_frame)
        self.ele_usr = self.find_element_can_be_clickable(self.loc_username_input)
        self.ele_pw = self.find_element_can_be_clickable(self.loc_password_input)
        self.ele_button = self.find_element_can_be_clickable(self.loc_login_button)

    def prepare_login(self, username, password):
        """
        为什么要加个点击动作，那是因为 send_keys 并不会移动鼠标，只是一个 focus 动作，而有的输入框同时可能存在 click 时间，因此强烈建议在输入框优先 click，在保证用例健壮性的时候，用例运行时长会增加，但这个问题可以上分布式解决
        """
        self.ele_usr.clear()
        self.ele_pw.clear()
        self.ele_usr.click(sleep=1)
        self.ele_usr.send_keys(username)
        self.ele_pw.click(sleep=1)
        self.ele_pw.send_keys(password)
        self.ele_button.click(sleep=1)

    def login_without_usr_pw(self, username, password):
        """演示用，实际编程时自动化用例优先覆盖与后台存在数据交互的功能，像这种单纯的前端检测，手工即可"""
        logger.debug("login_without_usr_pw")
        self.prepare_login(username, password)
        self.check_text_to_be_present_in_element(self.loc_error, "请输入帐号")

    def login_without_usr(self, username, password):
        """演示用，实际编程时自动化用例优先覆盖与后台存在数据交互的功能，像这种单纯的前端检测，手工即可"""
        logger.debug("login_without_usr")
        self.prepare_login(username, password)
        self.check_text_to_be_present_in_element(self.loc_error, "请输入帐号")

    def login_without_pw(self, username, password):
        """演示用，实际编程时自动化用例优先覆盖与后台存在数据交互的功能，像这种单纯的前端检测，手工即可"""
        logger.debug("login_without_pw")
        self.prepare_login(username, password)
        self.check_text_to_be_present_in_element(self.loc_error, "请输入密码")

    def login_incorrect_usr_or_pw(self, username, password):
        logger.debug("login_incorrect_usr_or_pw")
        self.prepare_login(username, password)
        self.check_text_to_be_present_in_element(self.loc_error, "帐号或密码错误")

    def login_sucess(self, username, password):
        logger.debug("login sucess")
        self.prepare_login(username, password)
        self.url_should_change(self.url)


if __name__ == "__main__":
    from framework.web import Browser
    driver = Browser("chrome")
    try:
        login = Login(driver)
        login.login_sucess("test", "11111")
        time.sleep(5)
    except Exception as e:
        print(e)
    finally:
        driver.quit()
