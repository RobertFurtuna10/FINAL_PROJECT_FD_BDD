Feature: Login Feature

  Background:
    Given I am on the login page

  @login_wrong_credentials
  Scenario Outline: Login with wrong credentials
    When I enter "<email>" in email field
    And I enter "<password>" in password field
    And I press autentifica-ma button
    Then I should see an error message

    Examples:
    |          email      |  password        |
    |   email@yahoo.com   | password10       |
    |wrong-email@gmail.com| parola123        |
    |  robert@email.ro    | wrongpass        |



  @login_wrong_email_format
  Scenario: Enter wrong email format
    When I enter "email.com" in email field
    And I press autentifica-ma button
    Then I should see an error for valid email request
    And I should see an error for password field

  @login_only_password
  Scenario: Enter only password
    When I enter "password2*" in password field
    And I press autentifica-ma button
    Then I should see an error under email field

  @login_empty_fields
  Scenario: Enter autentifica-ma button with email and password fields empty
    When I press autentifica-ma button
    Then I should see an error under email field
    And I should see an error for password field

  @login_only_email
  Scenario: Enter only email
    When I enter "robert@yahoo.com" in email field
    And I press autentifica-ma button
    Then I should see an error for password field

  @login_short_password
  Scenario: Enter short password
    When I enter "123" in password field
    And I press autentifica-ma button
    Then I should see an error for short password

