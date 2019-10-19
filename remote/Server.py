import time
import os
from selenium.webdriver.common import service
from framework.utils import DRIVER_PATH

class Service(service.Service):
    def __init__(self, executable_path="chromedriver", port=0,service_args=None,service_log_path=None, env=None):

        """
        Creates a new instance of the Service
        :Args:
         - executable_path : Path to the ChromeDriver
         - port : Port the service is running on
         - service_args : List of args to pass to the chromedriver service
         - log_path : Path for the chromedriver service to log to"""
        self.service_args = service_args or []
        if service_log_path:
            self.service_args.append('--log-path=%s' % service_log_path)
            self.service_args.append('--verbose')

        service.Service.__init__(self, executable_path, port=port, env=env,
                                 start_error_message="Please see https://sites.google.com/a/chromium.org/chromedriver/home")

        self.start()
        print("service start on: ",self.service_url)

    def command_line_args(self):
        return ["--port=%d" % self.port] + self.service_args

if __name__ == "__main__":
    service = Service(os.path.join(DRIVER_PATH, "chromedriver.exe"), port=9515, service_log_path="log.txt")
    try:
        while True:
            time.sleep(20)
            if service.process.poll():
                print("program has crashed ！ again running....")
                break
    except Exception as e:
        service.process.terminate()
        print("something wrong !", e)
        raise
