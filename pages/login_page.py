from selenium.common import NoSuchElementException
from browser import Browser
from locators.LoginLocators import LoginLocators


class LoginPage(Browser):

    def navigate_to_login_page(self):
        self.driver.get("https://www.flanco.ro/customer/account/login/referer/aHR0cHM6Ly93d3cuZmxhbmNvLnJvLz9nYWRfc291cmNlPTE%3D/")

    def enter_email(self, email):
        try:
            self.driver.find_element(*LoginLocators.EMAIL_FIELD_SELECTOR).send_keys(email)
        except NoSuchElementException:
            print("Email field not found")

    def enter_password(self, password):
        try:
            self.driver.find_element(*LoginLocators.PASSWORD_FIELD_SELECTOR).send_keys(password)
        except NoSuchElementException:
            print("Password field not found")

    def click_autentifica_ma_button(self):
        try:
            self.driver.find_element(*LoginLocators.LOGIN_BUTTON_SELECTOR).click()
        except NoSuchElementException:
            print("Autentifica-ma button not found")

    def get_error_message(self):
        return self.driver.find_element(*LoginLocators.ERROR_MESSAGE).text

    def get_password_field_error_message(self):
        return self.driver.find_element(*LoginLocators.PASSWORD_FIELD_ERROR).text

    def get_field_error_message(self):
        return self.driver.find_element(*LoginLocators.FIELD_ERROR).text

    def get_invalid_mail_error_message(self):
        return self.driver.find_element(*LoginLocators.INVALID_MAIL_ERROR).text

    def verify_valid_email_error(self):
        actual_error_message = self.get_invalid_mail_error_message()
        expected_error_message = 'Introduceți o adresă email validă (Ex: johndoe@domain.com).'
        assert actual_error_message in expected_error_message

    def verify_password_field_error_message(self):
        actual_error_message = self.get_password_field_error_message()
        expected_error_message = 'Acesta este un câmp obligatoriu.'
        assert actual_error_message in expected_error_message

    def verify_general_error_message(self):
        actual_error_message = self.get_error_message()
        expected_error_message = 'Conectarea la cont a fost incorectă sau contul dvs. este dezactivat temporar. Vă rugăm să așteptați și să încercați din nou mai târziu.'
        assert actual_error_message in expected_error_message

    def verify_email_field_error(self):
        actual_error_message = self.get_field_error_message()
        expected_error_message = 'Acesta este un câmp obligatoriu.'
        assert actual_error_message in expected_error_message

    def verify_short_password_error(self):
        actual_error_message = self.get_password_field_error_message()
        expected_error_message = 'Please enter 6 or more characters. Leading and trailing spaces will be ignored.'
        assert actual_error_message in expected_error_message
