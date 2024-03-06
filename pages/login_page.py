
from browser import Browser
from locators.LoginLocators import LoginLocators


class LoginPage(Browser):

    def navigate_to_login_page(self):
        self.driver.get("https://www.flanco.ro/customer/account/login/referer/aHR0cHM6Ly93d3cuZmxhbmNvLnJvLz9nYWRfc291cmNlPTE%3D/")

    def enter_email(self, email):
        self.driver.find_element(*LoginLocators.EMAIL_FIELD_SELECTOR).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*LoginLocators.PASSWORD_FIELD_SELECTOR).send_keys(password)

    def click_autentifica_ma_button(self):
        self.driver.find_element(*LoginLocators.LOGIN_BUTTON_SELECTOR).click()

    def get_error_message(self):
        return self.driver.find_element(*LoginLocators.ERROR_MESSAGE).text

    def get_field_error_message(self):
        return self.driver.find_element(*LoginLocators.FIELD_ERROR).text

    def get_invalid_mail_error_message(self):
        return self.driver.find_element(*LoginLocators.INVALID_MAIL_ERROR).text

    def get_short_password_error_message(self):
        return self.driver.find_element(*LoginLocators.SHORT_PASSWORD_ERROR).text
