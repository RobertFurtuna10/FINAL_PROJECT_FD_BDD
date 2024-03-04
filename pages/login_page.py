from selenium.webdriver.common.by import By

from browser import Browser


class LoginPage(Browser):

    EMAIL_FIELD_SELECTOR = (By.ID, 'email')
    PASSWORD_FIELD_SELECTOR = (By.CSS_SELECTOR, '[name="login[password]"]')
    LOGIN_BUTTON_SELECTOR = (By.CSS_SELECTOR, '#send2')
    ERROR_MESSAGE = (By.CLASS_NAME, 'textMessageAddToCard')
    FIELD_ERROR = (By.XPATH, '//div[contains(text(), "Acesta este un câmp obligatoriu.")]')
    INVALID_MAIL_ERROR = (By.XPATH, '//div[contains(text(), "Introduceți o adresă email validă (Ex: johndoe@domain.com).")]')
    SHORT_PASSWORD_ERROR = (By.XPATH, '//div[contains(text(), "Please enter 6 or more characters. Leading and trailing spaces will be ignored.")]')

    def navigate_to_login_page(self):
        self.driver.get("https://www.flanco.ro/customer/account/login/referer/aHR0cHM6Ly93d3cuZmxhbmNvLnJvLz9nYWRfc291cmNlPTE%3D/")

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL_FIELD_SELECTOR).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD_SELECTOR).send_keys(password)

    def click_autentifica_ma_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON_SELECTOR).click()

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text

    def get_field_error_message(self):
        return self.driver.find_element(*self.FIELD_ERROR).text

    def get_invalid_mail_error_message(self):
        return self.driver.find_element(*self.INVALID_MAIL_ERROR).text

    def get_short_password_error_message(self):
        return self.driver.find_element(*self.SHORT_PASSWORD_ERROR).text
