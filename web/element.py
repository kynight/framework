#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.remote.webelement import WebElement
from framework.utils.tools import regist2class
import time
from pykeyboard import PyKeyboard

set_attribute_js = "arguments[0].setAttribute(arguments[1], arguments[2]);"
remove_attribute_js = "arguments[0].removeAttribute(arguments[1]);"
highlight_js = """
var element = arguments[0];
var orignal_style = element.getAttribute('style');
if (!orignal_style) {
    orignal_style = '';
}
element.setAttribute('style', original_style + arguments[1]);
setTimeout(function(){element.setAttribute('style', original_style);}, 5000)
"""

class Element(WebElement):

    def __init__(self, webElement):
        self._parent = webElement._parent
        self._id = webElement._id
        self._w3c = webElement._w3c

    def click(self, sleep=None):
        if sleep:
            time.sleep(sleep)
        super().click()

    def set_attribute(self, attrname, value):
        self._parent.execute_script(set_attribute_js, self, attrname, value)

    def remove_attribute(self, attrname):
        self._parent.execute_script(set_attribute_js, self, attrname)

    def highlight(self):
        self._parent.execute_script((highlight_js, self, "border: 1px solid red"))

    def upload(self, file_path):
        self.click()
        time.sleep(5)
        kk = PyKeyboard()
        kk.type_string(file_path)
        kk.tap_key(kk.enter_key)
