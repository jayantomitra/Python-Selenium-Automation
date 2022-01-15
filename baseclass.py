import time
import unittest
import ConfigParser
from selenium import webdriver
import utils.custom_logger as cl
import logging


class BaseClass(unittest.TestCase):

    logger = cl.customlogger(logging.DEBUG)

    log_messages = []

    def __init__(self, configfile):
        self.configfile = configfile
        self.parser = ConfigParser.ConfigParser()
        self.parser.read(self.configfile)

    def set_up(self):
        browser = self.parser.get('browser_setup', 'browser_setup')
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--window-size=1920,1080")
        options.add_argument(browser)
        options.add_argument("user-agent=Shoptimize Healthcheck System")
        self.driver = webdriver.Chrome(options=options)

    def log(self, msg, console=True):
        msg = "[" + str(self.parser.get('store', 'code')) + "] " + str(msg)
        self.log_messages.append(msg)
        self.logger.info(msg)
        if console:
            print msg

    def get(self, url):
        start_time = time.time()
        self.driver.get(url=url)
        end_time = time.time()
        self.log(url + " " + str(end_time - start_time))

    def get_init(self):
        pass

    def tear_down(self):
        self.driver.close()

    def run(self):
        self.set_up()
        self._before_run()
        self.run_test()
        self._after_run()
        self.tear_down()

    def run_test(self):
        pass

    def _before_run(self):
        pass

    def _after_run(self):
        pass


