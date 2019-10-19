#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from framework.web.element import Element
from framework.utils import logger
import time

class Wait(WebDriverWait):
    """ 使用智能等待，重写 wait/wait not, 使用 Element 扩展避免直接在 selenium 中更改）"""

    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def until(self, method, message="Can't meet the {} condition"):
        """Calls the method provided with the driver as an argument until the \
        return value is not False."""
        screen = None
        stacktrace = None
        err = TimeoutException(message.format(method.__class__.__name__))

        end_time = time.time() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    if isinstance(value, WebElement):
                        return Element(value)
                    else:
                        return value
            except self._ignored_exceptions as e:
                err = e
            except Exception as e:
                err = e
                break
            time.sleep(self._poll)
            if time.time() > end_time:
                break
        message = getattr(err, 'msg', message)
        screen = getattr(err, 'screen', None)
        stacktrace = getattr(err, 'stacktrace', None)
        logger.error(message)
        raise err
        # self._driver.quit(err)

    def until_not(self, method, message="Can't meet the {} condition"):
        """Calls the method provided with the driver as an argument until the \
        return value is False."""
        err = TimeoutException(message.format(method.__class__.__name__))
        end_time = time.time() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if not value:
                    return value
            except self._ignored_exceptions:
                return True
            except Exception as e:
                err = e
                break
            time.sleep(self._poll)
            if time.time() > end_time:
                break

        message = getattr(err, 'msg', message)
        screen = getattr(err, 'screen', None)
        stacktrace = getattr(err, 'stacktrace', None)
        logger.error(message)
        raise err
        # self._driver.quit(err)

