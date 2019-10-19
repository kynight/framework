#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.chrome.remote_connection import ChromeRemoteConnection

class Chrome(RemoteWebDriver):
    """
    Creates a new instance of the chrome driver.
    Starts the service and then creates new instance of chrome driver.
    :Args:
     - executable_path - path to the executable. If the default is used it assumes the executable is in the $PATH
     - port - port you would like the service to run, if left as 0, a free port will be found.
     - options - this takes an instance of ChromeOptions
     - service_args - List of args to pass to the driver service
     - desired_capabilities - Dictionary object with non-browser specific
       capabilities only, such as "proxy" or "loggingPref".
     - service_log_path - Where to log information from the driver.
     - chrome_options - Deprecated argument for options
     - keep_alive - Whether to configure ChromeRemoteConnection to use HTTP keep-alive.
    """
    def __init__(self, service_url="http://localhost:9515",options=None,desired_capabilities=None, chrome_options=None, keep_alive=True,debug=False,logger_name=None):

        if chrome_options:
            warnings.warn('use options instead of chrome_options',
                          DeprecationWarning, stacklevel=2)
            options = chrome_options

        if options is None:
            # desired_capabilities stays as passed in
            if desired_capabilities is None:
                desired_capabilities = self.create_options().to_capabilities()
        else:
            if desired_capabilities is None:
                desired_capabilities = options.to_capabilities()
            else:
                desired_capabilities.update(options.to_capabilities())

        try:
            self.remote= RemoteWebDriver.__init__(
                self,command_executor=ChromeRemoteConnection(
                    remote_server_addr=service_url,
                    keep_alive=keep_alive,
                    debug=debug,
                    logger_name=logger_name),
                    desired_capabilities=desired_capabilities)
        except Exception:
            self.quit()
            raise

    def __getattr__(self, attr):
        return object.__getattribute__(self.remote, attr)

if __name__ == "main":
    driver = Chrome()
    driver.quit()
