# Automated Testing Project for Flanco.ro Website :computer:
Welcome to the documentation for the automated testing project designed for the Flanco.ro website. This project contains the source code and specifications, utilizing Behavior-Driven Development (BDD) principles to drive development, ensuring the functionality and reliability of Flanco.ro's webshop.
## Table of Contents

1. [Introduction/Tools and version](#tools-and-versions)
2. [Project Structure](#project-structure)
    - [Features](#features)
    - [Locators](#locators)
    - [Pages](#pages)
    - [Steps](#steps)
    - [Browser file](#browser-file)
    - [Environment file](#environment-file)
    - [Venv, behave.ini, Requirements.txt](#directories-and-files)
    - [Behave Script](#behave-script)
3. [Features Under Testing](#features-under-testing)
    - [Login Functionality Testing](#login-functionality-testing)
    - [Register Functionality Testing](#register-functionality-testing)
4. [Getting Started](#getting-started)
    - [Clone the Repository](#clone-the-repository)
    - [Install Dependencies](#install-dependencies)
    - [Activate the Virtual Environment](#activate-the-virtual-environment)
    - [Run the tests](#run-the-tests)
5. [Conclusion](#conclusion)

# Introduction :notebook:

This project aims to implement automated tests for the Flanco.ro website using BDD framework. The primary objectives include simulating user login and register options through the webshop's functionalities.

- **editor code used: pycharm**
- **Library Versions:**
    ```bash
     behave == 1.2.6
	 selenium == 4.18.1
	 webdriver-manager == 4.0.1
     behave-html-formatter == 0.9.10
     Faker == 24.0.0
    ```

# Project Structure

This project follows the Behavior-Driven Development (BDD) design pattern, enhancing modularity and maintainability The pages directory encapsulates classes representing specific pages on the Flanco.ro website, each handling interactions and elements unique to that page.

- **features**: Hold the specifications or scenarios written in Gherkin syntax. Gherkin is a human-readable format that describes the behavior of the software in plain language. Each feature file typically represents a feature or a user story of the application being developed, and it contains one or more scenarios that describe the various behaviors or functionalities of that feature.
```python
Feature: Login Feature

  Background:
    Given I am on the login page

  @login_wrong_credentials
  Scenario: Login with wrong credentials
    When I enter "email@yahoo.com" in email field
    And I enter "password10" in password field
    And I press login button
    Then I should see an error message

  @login_wrong_email_format
  Scenario: Enter wrong email format
    When I enter "email.com" in email field
    And I press login button
    Then I should see an error for valid email request
    And I should see an error for password field

  @login_only_password
  Scenario: Enter only password
    When I enter "password2*" in password field
    And I press login button
    Then I should see an error under email field

  @login_empty_fields
  Scenario: Enter Intra in cont button with email and password fields empty
    When I press login button
    Then I should see an error under email field
    And I should see an error for password field

  @login_only_email
  Scenario: Enter only email
    When I enter "robert@yahoo.com" in email field
    And I press login button
    Then I should see an error for password field

  @login_short_password
  Scenario: Enter short password
    When I enter "123" in password field
    And I press login button
    Then I should see an error for short password
```
```python
Feature: Register Feature

  Background:
    Given I am on the register page

  @register_with_empty_fields
  Scenario: Press ma inregistrez button with all the fields empty
    When I press on ma inregistrez button
    Then I should see a mandatory fill field error for all the fields

  @register_with_correct_credentials
  Scenario: Register with wrong credentials
    When I enter "Andrei" in lastname field for registration
    And I enter "George" in firstname field for registration
    And I enter a new email address in email field for registration
    And I enter "parola1234*" in password field for registration
    And I enter "parola1234*" in confirmation password field for registration
    And I click on terms and conditions box
    And I press on ma inregistrez button
    Then I should see a succsessful registration text message

  @register_with_same_email
  Scenario: Register with same email
    When I enter "Mario" in lastname field for registration
    And I enter "Alexandru" in firstname field for registration
    And I enter "mario@yahoo.com" in email field for registration
    And I enter "1234*mario" in password field for registration
    And I enter "1234*mario" in confirmation password field for registration
    And I click on terms and conditions box
    And I press on ma inregistrez button
    Then I should see an error message for using an email that has already been registered

  @register_with_wrong_email_format
  Scenario: Enter wrong email format
    When I enter "robert.yahoo.com" in email field for registration
    And I press on ma inregistrez button
    Then I should see an error for email

  @register_with_short_password
  Scenario: Enter less than 8 characters on password field
    When I enter "abc12" in password field for registration
    Then I should see an error message for short password

  @register_with_wrong_password_characters
  Scenario: Enter wrong characters on password field
    When I enter "12345678" in password field for registration
    Then I should see an error for wrong characters on password field

  @register_with_different_password_and_confirmation_password
  Scenario: Enter different passwords in password and confirmation password fiels
    When I enter "furtuna12345*" in password field for registration
    And I enter "abc" in confirmation password field for registration
    And I press on ma inregistrez button
    Then I should see an error for same password on confirm password field
```
- **locators**: Holds locator classes that store all the locators (CSS selectors, XPath ,etc.) used in the project. This separation ensures easy maintenance and updates if the locators change.
```python
from selenium.webdriver.common.by import By


class LoginLocators:

    EMAIL_FIELD_SELECTOR = (By.ID, 'email')
    PASSWORD_FIELD_SELECTOR = (By.CSS_SELECTOR, '[name="login[password]"]')
    LOGIN_BUTTON_SELECTOR = (By.CSS_SELECTOR, '#send2')
    ERROR_MESSAGE = (By.CLASS_NAME, 'textMessageAddToCard')
    FIELD_ERROR = (By.XPATH, '//div[contains(text(), "Acesta este un câmp obligatoriu.")]')
    INVALID_MAIL_ERROR = (By.CSS_SELECTOR, '#email-error')
    SHORT_PASSWORD_ERROR = (By.XPATH, '//div[contains(text(), "Please enter 6 or more characters. Leading and trailing spaces will be ignored.")]')
```
```python
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
```
By: Enumeration class provided by the Selenium WebDriver library. It is used to specify the mechanism by which elements on a web page will be located. These locators will be used by the test automation code to find and interact with the corresponding elements on the web page. Using By ensures a consistent and reliable way to locate elements across different web pages and browsers.
- **pages**: Contains classes representing specific pages on the Flanco.ro website. Each class encapsulates interactions and elements unique to that page.
```python
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
```
```python
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
```
- **steps**: Are written in the Gherkin syntax and correspond to scenarios described in feature files. Each step has a specific keyword (Given, When, Then) that signifies the type of action being performed. These steps are then implemented in code as step definitions, which execute the corresponding actions on the system under test and perform assertions to verify expected outcomes. The steps_login file contains step definitions that implement the actions described in the login feature's scenarios. These step definitions interact with the LoginPage class, which represents the login page of the application, to perform actions and validate expected outcomes during test execution.
```python
from behave import *

@given('I am on the login page')
def step_impl(context):
    context.LoginPage.navigate_to_login_page()

@when('I enter "{email}" in email field')
def step_impl(context, email):
    context.LoginPage.enter_email(email)

@when('I enter "{password}" in password field')
def step_impl(context, password):
    context.LoginPage.enter_password(password)

@when('I press login button')
def step_impl(context):
    context.LoginPage.click_autentifica_ma_button()

@then('I should see an error for valid email request')
def step_impl(context):
    actual_error_message = context.LoginPage.get_invalid_mail_error_message()
    expected_error_message = 'Introduceți o adresă email validă (Ex: johndoe@domain.com).'
    assert actual_error_message in expected_error_message

@then('I should see an error for password field')
def step_impl(context):
    actual_error_message = context.LoginPage.get_field_error_message()
    expected_error_message = 'Acesta este un câmp obligatoriu.'
    assert actual_error_message in expected_error_message

@then('I should see an error message')
def step_impl(context):
    actual_error_message = context.LoginPage.get_error_message()
    expected_error_message = 'Conectarea la cont a fost incorectă sau contul dvs. este dezactivat temporar. Vă rugăm să așteptați și să încercați din nou mai târziu.'
    assert actual_error_message in expected_error_message

@then('I should see an error under email field')
def step_impl(context):
    actual_error_message = context.LoginPage.get_field_error_message()
    expected_error_message = 'Acesta este un câmp obligatoriu.'
    assert actual_error_message in expected_error_message

@then('I should see an error for short password')
def step_imp(context):
    actual_error_message = context.LoginPage.get_short_password_error_message()
    expected_error_message = 'Please enter 6 or more characters. Leading and trailing spaces will be ignored.'
    assert actual_error_message in expected_error_message
```
The following steps are tailored to the specific registration process of the Flanco.ro website, allowing for automated testing and validation of the registration feature.
```python
import time
from faker import Faker
from behave import *


@given('I am on the register page')
def step_impl(context):
    context.Register.navigate_to_register_page()

@when('I enter "{lastname}" in lastname field for registration')
def step_impl(context, lastname):
    context.Register.get_last_name(lastname)

@when('I enter "{firstname}" in firstname field for registration')
def step_impl(context, firstname):
    context.Register.get_first_name(firstname)

@when('I enter "{emails}" in email field for registration')
def step_impl(context, emails):
    context.Register.enter_email(emails)

@when('I enter a new email address in email field for registration')
def step_impl(context):
    fake = Faker()
    email = fake.email()
    context.Register.enter_email(email)

@when('I enter "{passwword}" in password field for registration')
def step_impl(context, passwword):
    context.Register.enter_password(passwword)

@when('I enter "{confpassw}" in confirmation password field for registration')
def step_impl(context, confpassw):
    context.Register.confirm_password(confpassw)

@when('I click on terms and conditions box')
def step_impl(context):
    context.Register.terms_and_conditions()
    time.sleep(2)

@when('I press on ma inregistrez button')
def step_impl(context):
    context.Register.press_ma_inregistrez_button()
    time.sleep(2)

@then('I should see an error message for using an email that has already been registered')
def step_impl(context):
    actual_message = context.Register.same_email_error()
    expected_message = 'Există deja un cont înregistrat cu această adresă de emails. Dacă sunteți sigur că este adresa dumneavoastră de email, faceți click aici pentru a obține parola și a vă accesa contul.'
    assert actual_message in expected_message
    time.sleep(2)

@then('I should see a succsessful registration text message')
def step_impl(context):
    actual_alert_mesasge = context.Register.get_successful_register_message()
    expected_alert_message = 'Vă mulțumim că v-ați înregistrat la Flanco'
    assert actual_alert_mesasge in expected_alert_message

@then('I should see an error for email')
def step_impl(context):
    expected_error_message = context.Register.get_wrong_email_error()
    actual_error_message = "Introduceți o adresă email validă (Ex: johndoe@domain.com)."
    assert expected_error_message in actual_error_message

@then('I should see an error message for short password')
def step_impl(context):
    expected_error_message = context.Register.get_short_password_error()
    actual_error_message = "Lungimea minima a acestui camp trebuie sa fie egala sau mai mare de 8 simboluri. Spatiile vor fi ignorate."
    assert expected_error_message in actual_error_message

@then('I should see an error for wrong characters on password field')
def step_impl(context):
    expected_error_message = context.Register.get_characters_password_error()
    actual_error_message = "Minimul diferitelor clase de caractere din parola este de 3. Clase de caractere: litere mici, majuscule, cifre, caractere speciale."
    assert expected_error_message in actual_error_message

@then('I should see an error for same password on confirm password field')
def step_impl(context):
    expected_error_message = context.Register.get_same_value_confirmation_password_error()
    actual_error_message = "Va rugam sa introduceti din nou aceeasi valoare."
    assert expected_error_message in actual_error_message

@then('I should see a mandatory fill field error for all the fields')
def step_impl(context):
    expected_error_message = context.Register.get_mandatory_fields_error()
    actual_error_message = "Acesta este un câmp obligatoriu."
    assert expected_error_message in actual_error_message
```
time: Used for introducing delays in the test execution, providing a pause between actions.

faker: This library is used to generate fake data such as names and email addresses. In this particular case, the fake library is used to generate a new email address each time the registration functionality is tested with valid credentials. Without this library, the test would not pass because if the same email is entered twice, the account registration cannot be successful.

behave: This is the primary BDD testing framework for Python.
- **browser-file**: The following Browser class defines a simple wrapper around the Selenium WebDriver to manage the browser instance. It initializes a Chrome WebDriver instance, maximizes the window, and sets an implicit wait time of 3 seconds for finding elements before throwing an exception.
```python
from selenium import webdriver

class Browser:

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)

    def close(self):
        self.driver.quit()
```
- **environment-file**: This environment.py file is used in conjunction with Behave, the BDD testing framework, to set up and tear down test environments before and after test execution. It imports necessary modules, initializes objects, and defines hooks to execute setup and teardown actions.
```python
from browser import Browser
from pages.login_page import LoginPage
from pages.register_page import Register


def before_all(context):
    context.browser = Browser()
    context.LoginPage = LoginPage()
    context.Register = Register()

def after_all(context):
    context.browser.close()
```

- **venv**: The virtual environment directory.
- **behave.ini**: Serves as a configuration file for Behave, the behavior-driven development (BDD) testing framework in Python. It allows to specify various settings and options for Behave, including options related to formatters, logging, and other behavior settings.
- **requirements.txt**: Lists all the required dependencies for the project. Install these dependencies before running the tests.
- **behave-script**: Parses the feature files, matches steps to their corresponding step definitions, and executes the tests. It provides detailed reports on the execution status of each scenario and step, helping to understand which tests passed, failed, or encountered issues.

## Feature under testing
 ### Login Functionality Testing:
1. Login with wrong credentials.
2. Login with wrong email format.
3. Login with only password
4. Enter Intra in cont button with email and password fields empty
5. Enter only email
6. Enter short password

 ### Register Functionality Testing:
1. Register with empty fiels
2. Register with correct credentials
3. Register with same email
4. Register with wrong email format
5. Enter short password
6. Register with wrong password characters
7. Register with different password and confirmation password characters

## Getting Started  :pushpin:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/RobertFurtuna10/FINAL_PROJECT_FLANCO_BDD.git
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Activate the Virtual Environment:**

    ```bash
    venv/Scripts/Activate
    ```

4. **Run the tests:**

    ```bash
    behave - run all the tests without generating any raport
    behave --format html -o test-reports/execution_report.html  #generate a report called execution report with all tests, saving it in the test-reports folder
    behave --format html -o test-reports/register_tag_report_wrong_email_format.html --tags=@register_with_wrong_email_format #generate a report based on tag, in this example it will generate a report of the test that has the tag @register_with_worng_email_format
    ```

# Usage

Execute the automated tests to verify the Flanco.ro website's login and register functionalities.

# Reports

The project automatically generates detailed reports for each test scenario executed by Behave, offering comprehensive insights into the results of individual tests. These reports meticulously document the outcomes of each scenario, facilitating thorough analysis and easy identification of any encountered issues.

- Here's the execution report generated for the Login and Register functionalities on March 6, 2024.

![Execution Report](https://github.com/RobertFurtuna10/FINAL_PROJECT_FLANCO_BDD/blob/master/execution%20report.pdf)


- And some reports generated by tags
 


