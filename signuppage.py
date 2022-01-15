from tests.baseclass import BaseClass
import time
import logging


class SignUp(BaseClass):

    #URL_SIGNUP = "customer/account/create/"

    def __init__(self, configfile):
        BaseClass.__init__(self, configfile)

    def run_test(self):
        super(SignUp, self).run_test()
        self.log("Started SignUp Test")
        store_url = self.parser.get('store', 'url')
        #signup_url = store_url + self.URL_SIGNUP
        signup_url = self.parser.get('url', 'signup_url')
        self.get(signup_url)
        self.driver.maximize_window()
        self.firstname = self.parser.get('user', 'firstname')
        self.lastname = self.parser.get('user', 'lastname')
        self.email = self.parser.get('user', 'email')
        self.password = self.parser.get('user', 'password')
        self.confirmpassword = self.parser.get('user', 'confirmpassword')
        self.SignUp()
        self.log("Finished SignUp Test")

    def SignUp(self):
        #  locators
        _field_firstname = './/input[@id="firstname" and @name="firstname"]'
        _field_lastname = 'input[id ="lastname"]'
        _field_email = 'input[id*="email"][title="Email"]'
        _field_password = 'input[name="password"][id="password"]'
        _field_confirmpassword = 'input[id="password-confirmation"][title*="Confirm Pass"]'
        _field_phonenumber = 'input[title*="Phone Number"]'
        _field_createaccount_button = 'button[title="Create an Account"][type="submit"]'

        first_name = self.driver.find_elements_by_xpath(_field_firstname).__getitem__(1)
        first_name.send_keys(self.firstname)
        last_name = self.driver.find_elements_by_css_selector(_field_lastname).__getitem__(1)
        last_name.send_keys(self.lastname)
        time.sleep(2)
        script = "window.scrollBy(0,20);"
        self.driver.execute_script(script)
        email = self.driver.find_elements_by_css_selector(_field_email).__getitem__(2)
        email.send_keys(self.email)
        pass_word = self.driver.find_element_by_css_selector(_field_password)
        pass_word.send_keys(self.password)
        confirmation = self.driver.find_element_by_css_selector(_field_confirmpassword)
        confirmation.send_keys(self.confirmpassword)

        try:
            phonenumber = self.driver.find_element_by_css_selector(_field_phonenumber)
            phonenumber.send_keys('1234567890')
        except Exception:
            pass
        createAccount = self.driver.find_element_by_css_selector(_field_createaccount_button)
        try:
            createAccount.submit()
        except Exception:
            createAccount.click()
            pass
        time.sleep(5)
