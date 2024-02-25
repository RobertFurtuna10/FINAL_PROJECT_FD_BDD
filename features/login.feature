Feature: Login Feature
  Background:
    Given I am on the login page


  @first
  Scenario: Login with wrong credentials
    When I enter "email@yahoo.com" in email field
    And I enter "password10" in password field
    And I press login button
    Then I should see an error message

  @second
  Scenario: Enter wrong email format
    When I enter "email.com" in email field
    And I press login button
    Then I should see an error for email field
    And I should see an error for password field

  @third
  Scenario: Enter only password
    When I enter "password2*" in password field
    And I press login button
    Then I should see an error under email field

  @fourth
  Scenario: Enter Intra in cont button with email and password fields empty
    When I press login button
    Then I should see an error under email field
    And I should see an error for password field



