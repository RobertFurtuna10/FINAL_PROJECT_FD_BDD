from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


from browser import Browser


class Register(Browser):

    EMAIL_FIELD_SELECTOR = (By.CLASS_NAME, 'pizokel_customer_register_email')
    PASSWORD_FIELD_SELECTOR = (By.ID, 'pizokel_customer_register_password')
    CREEAZA_CONT_BUTTON_SELECTOR = (By.CSS_SELECTOR, '#pizokel_customer_register_submit')
    TERMS_AND_CONDITIONS_SELECTOR = (By.XPATH, '//input[@id="register-termscheck"]')
    REGISTER_ALERT_SELECTOR = (By.XPATH, '//h4[contains(text(), "Ne pare rau dar nu putem finaliza procesul de creare cont pentru aceasta adresa de email. Folosește una din metodele existente de social login precum eMAG , Facebook, Google sau Apple.")]')
    TERMS_AND_CONDITIONS_ERROR = (By.XPATH, '//div[contains(text(), "Te rugam sa accepti termenii si conditiile pentru a putea continua cu crearea contului")]')
    WRONG_EMAIL_ERROR = (By.XPATH, '//div[contains(text(), "Adresa de Email nu este completata corect (exemplu: nume@exemplu.com)")]')
    SHORT_PASSWORD_ERROR = (By.XPATH, '//div[contains(text(), "Te rugam sa introduci minim 6 caractere. Spatiile de la inceputul sau finalul acestora vor fi ignorate.")]')
    MANDATORY_FIELD_ERROR = (By.XPATH, '//div[contains(text(), "Acest camp este obligatoriu")]')


    def navigate_to_register_page(self):
        self.driver.get('https://www.fashiondays.ro/customer/authentication/register')

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL_FIELD_SELECTOR).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD_SELECTOR).send_keys(password)

    def press_creeaza_cont_button(self):
        self.driver.find_element(*self.CREEAZA_CONT_BUTTON_SELECTOR).click()

    def get_register_option_alert(self):
        return self.driver.find_element(*self.REGISTER_ALERT_SELECTOR).text

    def terms_and_conditions(self):
        # action = ActionChains(self.driver)
        # terms_conditions = self.driver.find_element(*self.TERMS_AND_CONDITIONS_SELECTOR)
        # action.move_to_element_with_offset(terms_conditions, 1, 1).click().perform()
        self.driver.find_element(*self.TERMS_AND_CONDITIONS_SELECTOR).click()

    def get_terms_and_conditions_error(self):
        return self.driver.find_element(*self.TERMS_AND_CONDITIONS_ERROR).text

    def get_wrong_email_error(self):
        return self.driver.find_element(*self.WRONG_EMAIL_ERROR).text

    def get_short_password_error(self):
        return self.driver.find_element(*self.SHORT_PASSWORD_ERROR).text

    def get_mandatory_field_error(self):
        return self.driver.find_element(*self.MANDATORY_FIELD_ERROR).text


