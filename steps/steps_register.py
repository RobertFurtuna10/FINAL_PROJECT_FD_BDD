import time

from behave import *

@given('I am on the register page')
def step_impl(context):
    context.Register.navigate_to_register_page()

@when('I enter "{email}" in email field for registration')
def step_impl(context, email):
    context.Register.enter_email(email)
    time.sleep(2)

@when('I enter "{passw}" in password field for registration')
def step_impl(context, passw):
    context.Register.enter_password(passw)
    time.sleep(2)

@when('I click on terms and conditions box')
def step_impl(context):
    context.Register.terms_and_conditions()
    time.sleep(2)


@when('I press on creeaza cont button')
def step_impl(context):
    context.Register.press_creeaza_cont_button()
    time.sleep(2)

@then('I should see an alert for register option')
def step_impl(context):
    actual_alert_mesasge = context.Register.get_register_option_alert()
    expected_alert_message = 'Ne pare rau dar nu putem finaliza procesul de creare cont pentru aceasta adresa de email. Folosește una din metodele existente de social login precum eMAG , Facebook, Google sau Apple.'
    assert actual_alert_mesasge in expected_alert_message

@then('I should see an error for terms and conditions box')
def step_impl(context):
    expected_error_message = context.Register.get_terms_and_conditions_error()
    actual_error_message = "Te rugam sa accepti termenii si conditiile pentru a putea continua cu crearea contului"
    assert expected_error_message in actual_error_message

@then('I should see an error for email')
def step_impl(context):
    expected_error_message = context.Register.get_wrong_email_error()
    actual_error_message = "Adresa de Email nu este completata corect (exemplu: nume@exemplu.com)"
    assert expected_error_message in actual_error_message


@then('I should see an error for password')
def step_impl(context):
    expected_error_message = context.Register.get_short_password_error()
    actual_error_message = "Te rugam sa introduci minim 6 caractere. Spatiile de la inceputul sau finalul acestora vor fi ignorate."
    assert expected_error_message in actual_error_message

@then('I should see a mandatory fill field error for email and password fields')
def step_impl(context):
    expected_error_message = context.Register.get_mandatory_field_error()
    actual_error_message = "Acest camp este obligatoriu"
    assert expected_error_message in actual_error_message