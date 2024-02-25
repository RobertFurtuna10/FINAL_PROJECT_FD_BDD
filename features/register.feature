Feature: Register Feature

  Background:
    Given I am on the register page

  @register_wrong_credentials
  Scenario: Register with wrong credentials
    When I enter "robert@yahoo.com" in email field for registration
    And I enter "furtuna96" in password field for registration
    And I click on terms and conditions box
    And I press on creeaza cont button
    Then I should see an alert for register option


  @terms_and_conditions
  Scenario: Register without accepting terms and conditions
    When I enter "robert96@gmail.com" in email field for registration
    And I enter "robert10" in password field for registration
    And I press on creeaza cont button
    Then I should see an error for terms and conditions box

  @register_wrong_email_format
  Scenario: Enter wrong email format
    When I enter "robert.yahoo.com" in email field for registration
    And I press on creeaza cont button
    Then I should see an error for email

  @register_short_password
  Scenario: Enter less than 6 characters on password field
    When I enter "abc12" in password field for registration
    And I press on creeaza cont button
    Then I should see an error for password

  @register_with_empty_fields
  Scenario: Press creeaza cont button with all the fields empty
    When I press on creeaza cont button
    Then I should see a mandatory fill field error for email and password fields
    And I should see an error for terms and conditions box


