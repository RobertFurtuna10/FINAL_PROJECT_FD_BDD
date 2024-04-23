from selenium.webdriver.common.by import By


class LoginLocators:

    EMAIL_FIELD_SELECTOR = (By.ID, 'email')
    PASSWORD_FIELD_SELECTOR = (By.CSS_SELECTOR, '[name="login[password]"]')
    LOGIN_BUTTON_SELECTOR = (By.CSS_SELECTOR, '#send2')
    ERROR_MESSAGE = (By.CLASS_NAME, 'textMessageAddToCard')
    FIELD_ERROR = (By.CSS_SELECTOR, '[class="mage-error"]')
    PASSWORD_FIELD_ERROR = (By.CSS_SELECTOR, '#pass-error')
    INVALID_MAIL_ERROR = (By.CSS_SELECTOR, '#email-error')

