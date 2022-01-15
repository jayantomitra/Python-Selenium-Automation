import time
from tests.baseclass import BaseClass


class LoginPage(BaseClass):

    URL_LOGIN = "customer/account/login/"

    def __init__(self, configfile):
        BaseClass.__init__(self, configfile)

    def run_test(self):
        super(LoginPage, self).run_test()
        self.log("Started LoginPage Test")
        store_url = self.parser.get('store', 'url')
        #login_url = self.parser.get('url', 'login_url')
        login_url =  store_url + "customer/account/login/"
        self.get(login_url)
        self.driver.maximize_window()
        self.driver.refresh()
        time.sleep(5)
        self.username = self.parser.get('user', 'username')
        self.password = self.parser.get('user', 'password')
        self.login()
        self.log("Finished LoginPage Test")

    def login(self):
        # locators
        _field_email = '//input[@id = "email"]'
        _field_password = '//input[@name="login[password]"]'
        _field_loginbutton = '//button[@class="action login primary" and @type="submit"]'
        try:
            email_fields = self.driver.find_elements_by_xpath(_field_email)
            email = email_fields.__getitem__(1)
            email.send_keys(self.username)
            self.log('Entered Email')

        except Exception:
            email_fields = self.driver.find_elements_by_xpath(_field_email)
            email = email_fields.__getitem__(0)
            email.send_keys(self.username)
            self.log('Entered Email')
        password_field = self.driver.find_element_by_xpath(_field_password)
        password = password_field
        password.send_keys(self.password)
        self.log('Entered Password')
        login_button = self.driver.find_element_by_xpath(_field_loginbutton)
        try:
            login_button.submit()
            self.log('clicked login button')
        except Exception:
            login_button.submit()
            print "could not click button"
        time.sleep(5)
