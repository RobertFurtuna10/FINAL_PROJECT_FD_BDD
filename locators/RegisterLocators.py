from selenium.webdriver.common.by import By


class RegisterLocators:

    LAST_NAME_FIELD_SELECTOR = (By.ID, 'lastname')
    FIRST_NAME_FIELD_SELECTOR = (By.CSS_SELECTOR, '#firstname')
    EMAIL_FIELD_SELECTOR = (By.CSS_SELECTOR, '#email_address')
    PASSWORD_FIELD_SELECTOR = (By.CSS_SELECTOR, '[title="Parolă"]')
    CONFIRM_PASSWORD_FIELD_SELECTOR = (By.CSS_SELECTOR, '#password-confirmation')
    REGISTER_BUTTON = (By.CLASS_NAME, 'rlogin-button')
    TERMS_AND_CONDITIONS_SELECTOR = (By.CSS_SELECTOR, '[for="privacyGDPR"]')
    WRONG_EMAIL_ERROR = (By.CSS_SELECTOR, '#email_address-error')
    PASSWORD_ERROR_MESSAGE = (By.CSS_SELECTOR, '#password-error')
    SAME_VALUE_CONFIRMATION_PASSWORD_ERROR = (By.CSS_SELECTOR, '#password-confirmation-error')
    MANDATORY_FIELDS_ERROR = (By.CSS_SELECTOR, '[class="mage-error"]')
    SUCCESSFUL_REGISTER_MESSAGE = (By.CSS_SELECTOR, '.message-success')
    SAME_EMAIL_REGISTRATION_ERROR = (By.CSS_SELECTOR, '.textMessageAddToCard')