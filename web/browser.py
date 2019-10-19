#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from framework.utils import logger, config, DRIVER_PATH
from framework.remote.WebDriver import Chrome
import time
import os

TYPES = {
    "chrome": webdriver.Chrome
}

EXECUTABLE_PATH  = {
    "chrome": os.path.join(DRIVER_PATH, "chromedriver.exe")
}

class Browser(object):
    def __init__(self, browser_type="chrome"):
        self._state = "unopen"
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.webdriver = TYPES[self._type]
            logger.info("You had select %s browser." % browser_type)
        else:
            logger.info("only support %s !" % ", ".join(TYPES.keys()))
            logger.error("can't supoort %s browser." % browser_type)
            self.quit()

        chrome_options = ChromeOptions()
        if config.get(self._type).get("is_headless", False):
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
        self.driver = self.webdriver(executable_path=EXECUTABLE_PATH[self._type], chrome_options=chrome_options)

        # elif config.get(self._type).get("is_remote",False):
        #     options = ChromeOptions()
        #     options.update(config.get(self._type)["remote"])
        #     debug = config.get("selenium").get("debug",False)
        #     logger_name = config.get("selenium").get("logger",None)
        #     self.driver = Chrome(options=options, debug=debug, logger_name=logger_name)

        if config.get(self._type)["simple"].get("maximize_window", False):
            try:
                self.driver.maximize_window()
                logger.info("Maximize the current window.")
            except Exception as e:
                logger.warning(e.msg)

        implicitly_wait_timeout = config.get(self._type)["simple"].get("implicitly_wait", False)
        if implicitly_wait_timeout:
            self.driver.implicitly_wait(implicitly_wait_timeout)
            logger.info("Set implicitly wait %s seconds." % implicitly_wait_timeout)

    def get(self, url):
        self._state = "open"
        logger.info("Now, open url: %s" % url)
        self.driver.get(url)

    def quit(self, err=None):
        if self._state != "dead":
            logger.info("Now, quit the browser.")
            self._state = "dead"
            self.driver.quit()
        else:
            logger.warning("Some error has occurred and Browser has been closed !")
        if err:
            raise err

    def __getattr__(self, attr):
        return object.__getattribute__(self.driver, attr)

if __name__ == '__main__':
    browser = Browser("chrome")
    try:
        browser.get("https://www.baidu.com")
        time.sleep(5)
    except Exception as e:
        print(e)
    finally:
        browser.quit()
