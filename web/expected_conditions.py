#!/usr/bin/env python
# -*- coding: utf-8 -*-

class url_is(object):
    """An expectation for checking the title of a page.
    title is the expected title, which must be an exact match
    returns True if the title matches, false otherwise."""
    def __init__(self, url):
        self.url = url

    def __call__(self, driver):
        return self.url == driver.current_url

class url_contains(object):
    """An expectation for checking the title of a page.
    title is the expected title, which must be an exact match
    returns True if the title matches, false otherwise."""
    def __init__(self, title):
        self.url = url

    def __call__(self, driver):
        return self.url in driver.current_url
