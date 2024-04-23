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

@when('I press autentifica-ma button')
def step_impl(context):
    context.LoginPage.click_autentifica_ma_button()

@then('I should see an error for valid email request')
def step_impl(context):
    context.LoginPage.verify_valid_email_error()

@then('I should see an error for password field')
def step_impl(context):
    context.LoginPage.verify_password_field_error_message()

@then('I should see an error message')
def step_impl(context):
    context.LoginPage.verify_general_error_message()

@then('I should see an error under email field')
def step_impl(context):
    context.LoginPage.verify_email_field_error()

@then('I should see an error for short password')
def step_imp(context):
    context.LoginPage.verify_short_password_error()

