import time

from selenium.webdriver.common.by import By

from browser import Browser


class LoginPage(Browser):
    EMAIL_FIELD_SELECTOR = (By.ID, 'email')
    PASSWORD_FIELD_SELECTOR = (By.CSS_SELECTOR, '#password')
    LOGIN_BUTTON_SELECTOR = (By.CSS_SELECTOR, '#pizokel_customer_submit')
    ERROR_MESSAGE = (By.XPATH,
                     '//div[contains(text(), "Adresa de email sau parola este incorecta. Te rugam sa introduci o alta combinatie.")]')
    FIELD_ERROR = (By.XPATH, '//div[contains(text(), "Acest camp este obligatoriu")]')
    INVALID_MAIL_ERROR = (By.XPATH, '//div[contains(text(), "Adresa de email este invalida.")]')

    def navigate_to_login_page(self):
        self.driver.get("https://www.fashiondays.ro/customer/authentication")

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL_FIELD_SELECTOR).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD_SELECTOR).send_keys(password)

    def click_intra_in_cont_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON_SELECTOR).click()

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text

    def get_field_error_message(self):
        return self.driver.find_element(*self.FIELD_ERROR).text

    def get_invalid_mail_error_message(self):
        return self.driver.find_element(*self.INVALID_MAIL_ERROR).text
