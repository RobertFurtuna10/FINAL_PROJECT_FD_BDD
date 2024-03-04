from selenium.webdriver.common.by import By


from browser import Browser

class Register(Browser):

    LAST_NAME_FIELD_SELECTOR = (By.ID, 'lastname')
    FIRST_NAME_FIELD_SELECTOR = (By.CSS_SELECTOR, '#firstname')
    EMAIL_FIELD_SELECTOR = (By.CSS_SELECTOR, '#email_address')
    PASSWORD_FIELD_SELECTOR = (By.CSS_SELECTOR, '[title="Parolă"]')
    CONFIRM_PASSWORD_FIELD_SELECTOR = (By.CSS_SELECTOR, '#password-confirmation')
    REGISTER_BUTTON = (By.CLASS_NAME, 'rlogin-button')
    TERMS_AND_CONDITIONS_SELECTOR = (By.CSS_SELECTOR, '[for="privacyGDPR"]')
    WRONG_EMAIL_ERROR = (By.XPATH, '//div[contains(text(), "Introduceți o adresă email validă (Ex: johndoe@domain.com).")]')
    SHORT_PASSWORD_ERROR = (By.XPATH, '//div[contains(text(), "Lungimea minima a acestui camp trebuie sa fie egala sau mai mare de 8 simboluri. Spatiile vor fi ignorate.")]')
    CHARACTERS_PASSWORD_ERROR = (By.XPATH, '//div[contains(text(), "Minimul diferitelor clase de caractere din parola este de 3. Clase de caractere: litere mici, majuscule, cifre, caractere speciale.")]')
    SAME_VALUE_CONFIRMATION_PASSWORD_ERROR = (By.XPATH, '//div[contains(text(),"Va rugam sa introduceti din nou aceeasi valoare.")]')
    MANDATORY_FIELDS_ERROR = (By.XPATH, '//div[contains(text(), "Acesta este un câmp obligatoriu.")]')
    SUCCESSFUL_REGISTER_MESSAGE = (By.XPATH, '//div[contains(text(), "Vă mulțumim că v-ați înregistrat la Flanco")]')
    SAME_EMAIL_REGISTRATION_ERROR = (By.CSS_SELECTOR, '.textMessageAddToCard')


    def navigate_to_register_page(self):
        self.driver.get('https://www.flanco.ro/customer/account/create/?referer=aHR0cHM6Ly93d3cuZmxhbmNvLnJvLz9nYWRfc291cmNlPTE=')

    def get_last_name(self, lastname):
        self.driver.find_element(*self.LAST_NAME_FIELD_SELECTOR).send_keys(lastname)

    def get_first_name(self, firstname):
        self.driver.find_element(*self.FIRST_NAME_FIELD_SELECTOR).send_keys(firstname)

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL_FIELD_SELECTOR).send_keys(email)

    def same_email_error(self):
        return self.driver.find_element(*self.SAME_EMAIL_REGISTRATION_ERROR).text

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD_SELECTOR).send_keys(password)

    def confirm_password(self, confpassw):
        self.driver.find_element(*self.CONFIRM_PASSWORD_FIELD_SELECTOR).send_keys(confpassw)

    def press_ma_inregistrez_button(self):
        self.driver.find_element(*self.REGISTER_BUTTON).click()

    def terms_and_conditions(self):
        self.driver.find_element(*self.TERMS_AND_CONDITIONS_SELECTOR).click()

    def get_wrong_email_error(self):
        return self.driver.find_element(*self.WRONG_EMAIL_ERROR).text

    def get_short_password_error(self):
        return self.driver.find_element(*self.SHORT_PASSWORD_ERROR).text

    def get_characters_password_error(self):
        return self.driver.find_element(*self.CHARACTERS_PASSWORD_ERROR).text

    def get_same_value_confirmation_password_error(self):
        return self.driver.find_element(*self.SAME_VALUE_CONFIRMATION_PASSWORD_ERROR).text

    def get_mandatory_fields_error(self):
        return self.driver.find_element(*self.MANDATORY_FIELDS_ERROR).text

    def get_successful_register_message(self):
        return self.driver.find_element(*self.SUCCESSFUL_REGISTER_MESSAGE).text


