import time

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
    context.LoginPage.click_intra_in_cont_button()

@then('I should see an error for email field')
def step_impl(context):
    actual_error_message = context.LoginPage.get_invalid_mail_error_message()
    expected_error_message = 'Adresa de email este invalida.'
    assert actual_error_message in expected_error_message

@then('I should see an error for password field')
def step_impl(context):
    actual_error_message = context.LoginPage.get_field_error_message()
    expected_error_message = 'Acest camp este obligatoriu'
    assert actual_error_message in expected_error_message

@then('I should see an error message')
def step_impl(context):
    actual_error_message = context.LoginPage.get_error_message()
    expected_error_message = 'Adresa de email sau parola este incorecta. Te rugam sa introduci o alta combinatie.'
    assert actual_error_message in expected_error_message

@then('I should see an error under email field')
def step_impl(context):
    actual_error_message = context.LoginPage.get_field_error_message()
    expected_error_message = 'Acest camp este obligatoriu'
    assert actual_error_message in expected_error_message
