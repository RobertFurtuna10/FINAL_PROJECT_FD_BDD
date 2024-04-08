from faker import Faker

from browser import Browser
from locators.RegisterLocators import RegisterLocators


class Register(Browser):

    def navigate_to_register_page(self):
        self.driver.get('https://www.flanco.ro/customer/account/create/?referer=aHR0cHM6Ly93d3cuZmxhbmNvLnJvLz9nYWRfc291cmNlPTE=')

    def get_last_name(self, lastname):
        self.driver.find_element(*RegisterLocators.LAST_NAME_FIELD_SELECTOR).send_keys(lastname)

    def get_first_name(self, firstname):
        self.driver.find_element(*RegisterLocators.FIRST_NAME_FIELD_SELECTOR).send_keys(firstname)

    def enter_email(self, emails):
        self.driver.find_element(*RegisterLocators.EMAIL_FIELD_SELECTOR).send_keys(emails)

    def same_email_error(self):
        return self.driver.find_element(*RegisterLocators.SAME_EMAIL_REGISTRATION_ERROR).text

    def enter_password(self, password):
        self.driver.find_element(*RegisterLocators.PASSWORD_FIELD_SELECTOR).send_keys(password)

    def confirm_password(self, confpassw):
        self.driver.find_element(*RegisterLocators.CONFIRM_PASSWORD_FIELD_SELECTOR).send_keys(confpassw)

    def press_ma_inregistrez_button(self):
        self.driver.find_element(*RegisterLocators.REGISTER_BUTTON).click()

    def terms_and_conditions(self):
        self.driver.find_element(*RegisterLocators.TERMS_AND_CONDITIONS_SELECTOR).click()

    def get_wrong_email_error(self):
        return self.driver.find_element(*RegisterLocators.WRONG_EMAIL_ERROR).text

    def get_short_password_error(self):
        return self.driver.find_element(*RegisterLocators.SHORT_PASSWORD_ERROR).text

    def get_characters_password_error(self):
        return self.driver.find_element(*RegisterLocators.CHARACTERS_PASSWORD_ERROR).text

    def get_same_value_confirmation_password_error(self):
        return self.driver.find_element(*RegisterLocators.SAME_VALUE_CONFIRMATION_PASSWORD_ERROR).text

    def get_mandatory_fields_error(self):
        return self.driver.find_element(*RegisterLocators.MANDATORY_FIELDS_ERROR).text

    def get_successful_register_message(self):
        return self.driver.find_element(*RegisterLocators.SUCCESSFUL_REGISTER_MESSAGE).text

    def get_random_email(self):
        fake = Faker()
        email = fake.email()
        self.enter_email(email)
