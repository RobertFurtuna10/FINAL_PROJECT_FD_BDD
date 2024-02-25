from browser import Browser
from pages.login_page import LoginPage
from pages.register_page import Register


def before_all(context):
    context.browser = Browser()
    context.LoginPage = LoginPage()
    context.Register = Register()

def after_all(context):
    context.browser.close()