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

