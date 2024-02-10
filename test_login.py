# test_login.py
import time

import pytest
from playwright_base import browser, context, page
# test_login.py
from pages.Loginpage import LoginPage
from Excelreader import read_test_data
from pages.Helper import helper

test_data_autharized = read_test_data('data/Login_test_data.xlsx', 'valid')
test_data_invaliduser = read_test_data('data/Login_test_data.xlsx', 'invalid')
test_data_locked = read_test_data('data/Login_test_data.xlsx', 'locked')

@pytest.mark.parametrize("username, password", [(data['username'], data['password']) for data in test_data_locked])
def test_lockedlogin(page,username,password):
    Log =  LoginPage(page)
    Log.login(username.strip(), password)
    time.sleep(5)
    assert Log.is_locked()

@pytest.mark.parametrize("username, password", [(data['username'], data['password']) for data in test_data_autharized])
def test_successful_login(page,username,password):
    Log =  LoginPage(page)
    Log.login(username, password)
    assert Log.is_logged_in()
@pytest.mark.parametrize("username, password", [(data['username'], data['password']) for data in test_data_invaliduser])
def test_failed_login(page,username,password):
    Log =  LoginPage(page)
    Log.login(str(username), str(password))
    assert not Log.is_logged_in()

def test_login_validation(page):
    Log = LoginPage(page)
    helper(page).navigate_to('https://www.saucedemo.com/inventory.html')
    assert not Log.is_logged_in()


