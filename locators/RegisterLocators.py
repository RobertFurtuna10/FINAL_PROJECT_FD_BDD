from selenium.webdriver.common.by import By


class RegisterLocators:

    LAST_NAME_FIELD_SELECTOR = (By.ID, 'lastname')
    FIRST_NAME_FIELD_SELECTOR = (By.CSS_SELECTOR, '#firstname')
    EMAIL_FIELD_SELECTOR = (By.CSS_SELECTOR, '#email_address')
    PASSWORD_FIELD_SELECTOR = (By.CSS_SELECTOR, '[title="Parolă"]')
    CONFIRM_PASSWORD_FIELD_SELECTOR = (By.CSS_SELECTOR, '#password-confirmation')
    REGISTER_BUTTON = (By.CLASS_NAME, 'rlogin-button')
    TERMS_AND_CONDITIONS_SELECTOR = (By.CSS_SELECTOR, '[for="privacyGDPR"]')
    WRONG_EMAIL_ERROR = (By.XPATH, '//div[contains(text(), "Introduceți o adresă email validă (Ex: johndoe@domain.com).")]')
    SHORT_PASSWORD_ERROR = (By.XPATH,'//div[contains(text(), "Lungimea minima a acestui camp trebuie sa fie egala sau mai mare de 8 simboluri. Spatiile vor fi ignorate.")]')
    CHARACTERS_PASSWORD_ERROR = (By.XPATH, '//div[contains(text(), "Minimul diferitelor clase de caractere din parola este de 3. Clase de caractere: litere mici, majuscule, cifre, caractere speciale.")]')
    SAME_VALUE_CONFIRMATION_PASSWORD_ERROR = (By.XPATH, '//div[contains(text(),"Va rugam sa introduceti din nou aceeasi valoare.")]')
    MANDATORY_FIELDS_ERROR = (By.XPATH, '//div[contains(text(), "Acesta este un câmp obligatoriu.")]')
    SUCCESSFUL_REGISTER_MESSAGE = (By.XPATH, '//div[contains(text(), "Vă mulțumim că v-ați înregistrat la Flanco")]')
    SAME_EMAIL_REGISTRATION_ERROR = (By.CSS_SELECTOR, '.textMessageAddToCard')