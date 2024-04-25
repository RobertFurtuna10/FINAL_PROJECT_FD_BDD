import time
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
    context.Register.get_random_email()

@when('I enter "{password}" in password field for registration')
def step_impl(context, password):
    context.Register.enter_password(password)

@when('I enter "{confpassw}" in confirmation password field for registration')
def step_impl(context, confpassw):
    context.Register.confirm_password(confpassw)

@when('I click on terms and conditions box')
def step_impl(context):
    context.Register.terms_and_conditions()

@when('I press on ma inregistrez button')
def step_impl(context):
    context.Register.press_ma_inregistrez_button()

@then('I should see an error message for using an email that has already been registered')
def step_impl(context):
    context.Register.verify_same_email_error()
    time.sleep(2)

@then('I should see a succsessful registration text message')
def step_impl(context):
    context.Register.verify_successful_register_message()
    time.sleep(2)

@then('I should see an error for email')
def step_impl(context):
    context.Register.verify_wrong_email_error()

@then('I should see an error message for short password')
def step_impl(context):
    context.Register.verify_short_password_error()

@then('I should see an error for wrong characters on password field')
def step_impl(context):
    context.Register.verify_characters_password_error()

@then('I should see an error for same password on confirm password field')
def step_impl(context):
    context.Register.verify_same_value_confirmation_password_error()

@then('I should see a mandatory fill field error for all the fields')
def step_impl(context):
    context.Register.verify_mandatory_fields_error()
