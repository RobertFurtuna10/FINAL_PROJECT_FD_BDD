Feature: Register Feature

  Background:
    Given I am on the register page

  @register_with_empty_fields
  Scenario: Press ma inregistrez button with all the fields empty
    When I press on ma inregistrez button
    Then I should see a mandatory fill field error for all the fields


#  @register_correct_credentials
#  Scenario: Register with wrong credentials
#    When I enter "Andrei" in lastname field for registration
#    And I enter "George" in firstname field for registration
#    And I enter "marius232@yahoo.com" in email field for registration
#    And I enter "parola1234*" in password field for registration
#    And I enter "parola1234*" in confirmation password field for registration
#    And I click on terms and conditions box
#    And I press on ma inregistrez button
#    Then I should see a succsessful registration text message

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


  @register_wrong_email_format
  Scenario: Enter wrong email format
    When I enter "robert.yahoo.com" in email field for registration
    And I press on ma inregistrez button
    Then I should see an error for email

  @register_short_password
  Scenario: Enter less than 8 characters on password field
    When I enter "abc12" in password field for registration
    Then I should see an error message for short password

  @register_wrong_characters_password
  Scenario: Enter wrong characters on password field
    When I enter "12345678" in password field for registration
    Then I should see an error for wrong characters on password field

  @register_different_password_and_confirmation_password
  Scenario: Enter different passwords in password and confirmation password fiels
    When I enter "furtuna12345*" in password field for registration
    And I enter "abc" in confirmation password field for registration
    And I press on ma inregistrez button
    Then I should see an error for same password on confirm password field






