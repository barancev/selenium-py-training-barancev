from model.user import User
from selenium import webdriver
from selenium.common.exceptions import *
from selenium_fixture import app


def test_login_with_invalid_credentials(app):
    app.login(User.random())
    assert app.is_not_logged_in()


def test_login_with_valid_credentials(app):
    app.login(User.Admin())
    assert app.is_logged_in()
    app.logout()
    assert app.is_not_logged_in()


