import time
from tests.baseclass import BaseClass


class HomePage(BaseClass):
    def __init__(self, configfile):
        BaseClass.__init__(self, configfile)

    def run_test(self):
        self.log("Started HomePage Test")
        super(HomePage, self).run_test()
        self.homepage()
        self.log("Finished HomePage Test")

    def homepage(self):
        url = self.parser.get('store','url')
        self.get(url)
        self.driver.maximize_window()
        time.sleep(5)
        try:
            print "waiting for pop-up to appear"
            pop_up_close = self.driver.find_element_by_css_selector('div[ class = "es-pop-up apexit open"]>a')
            pop_up_close.click()
            print "tried to close pop-up"
        except Exception:
            print"No pop -up"
            pass
        footnote = self.driver.find_element_by_xpath("//a[@href='http://www.shoptimize.in/']")
        link = footnote.get_attribute('href')
        self.assertEqual(link, 'http://www.shoptimize.in/')
        self.log('footnote link = ' + link)
        time.sleep(5)


