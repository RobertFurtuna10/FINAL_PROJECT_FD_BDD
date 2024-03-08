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
    - [Run the Test Suite](#run-the-test-suite)
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

  
