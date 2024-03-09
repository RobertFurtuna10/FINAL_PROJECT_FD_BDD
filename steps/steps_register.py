import time
from faker import Faker
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
    fake = Faker()
    email = fake.email()
    context.Register.enter_email(email)

@when('I enter "{passwword}" in password field for registration')
def step_impl(context, passwword):
    context.Register.enter_password(passwword)

@when('I enter "{confpassw}" in confirmation password field for registration')
def step_impl(context, confpassw):
    context.Register.confirm_password(confpassw)

@when('I click on terms and conditions box')
def step_impl(context):
    context.Register.terms_and_conditions()
    time.sleep(2)

@when('I press on ma inregistrez button')
def step_impl(context):
    context.Register.press_ma_inregistrez_button()
    time.sleep(2)

@then('I should see an error message for using an email that has already been registered')
def step_impl(context):
    actual_message = context.Register.same_email_error()
    expected_message = 'Există deja un cont înregistrat cu această adresă de emails. Dacă sunteți sigur că este adresa dumneavoastră de email, faceți click aici pentru a obține parola și a vă accesa contul.'
    assert actual_message in expected_message
    time.sleep(2)

@then('I should see a succsessful registration text message')
def step_impl(context):
    actual_alert_mesasge = context.Register.get_successful_register_message()
    expected_alert_message = 'Vă mulțumim că v-ați înregistrat la Flanco'
    assert actual_alert_mesasge in expected_alert_message
    time.sleep(2)

@then('I should see an error for email')
def step_impl(context):
    expected_error_message = context.Register.get_wrong_email_error()
    actual_error_message = "Introduceți o adresă email validă (Ex: johndoe@domain.com)."
    assert expected_error_message in actual_error_message

@then('I should see an error message for short password')
def step_impl(context):
    expected_error_message = context.Register.get_short_password_error()
    actual_error_message = "Lungimea minima a acestui camp trebuie sa fie egala sau mai mare de 8 simboluri. Spatiile vor fi ignorate."
    assert expected_error_message in actual_error_message

@then('I should see an error for wrong characters on password field')
def step_impl(context):
    expected_error_message = context.Register.get_characters_password_error()
    actual_error_message = "Minimul diferitelor clase de caractere din parola este de 3. Clase de caractere: litere mici, majuscule, cifre, caractere speciale."
    assert expected_error_message in actual_error_message

@then('I should see an error for same password on confirm password field')
def step_impl(context):
    expected_error_message = context.Register.get_same_value_confirmation_password_error()
    actual_error_message = "Va rugam sa introduceti din nou aceeasi valoare."
    assert expected_error_message in actual_error_message

@then('I should see a mandatory fill field error for all the fields')
def step_impl(context):
    expected_error_message = context.Register.get_mandatory_fields_error()
    actual_error_message = "Acesta este un câmp obligatoriu."
    assert expected_error_message in actual_error_message