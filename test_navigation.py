# test_login.py
import time

import pytest
from playwright_base import browser, context, page
# test_login.py
from pages.Loginpage import LoginPage
from pages.Sidemenupage import Sidemenu
from Excelreader import read_test_data

test_data_singleuser = read_test_data('data/Login_test_data.xlsx', 'valid')
first_row_data = test_data_singleuser[0]
@pytest.mark.parametrize("username, password", [(first_row_data['username'], first_row_data['password'])])
def test_logout(page,username,password):
    Log =  LoginPage(page)
    Log.login(username,password)
    Sidemen = Sidemenu(page)
    Sidemen.open_sidemenu()
    Sidemen.logout()
    assert Sidemen.is_loggedout()
@pytest.mark.parametrize("username, password", [(first_row_data['username'], first_row_data['password'])])
def test_open_twitter(page,username,password):
    Log =  LoginPage(page)
    Log.login(username, password)
    Sidemen = Sidemenu(page)
    assert Sidemen.open_twitter()
@pytest.mark.parametrize("username, password", [(first_row_data['username'], first_row_data['password'])])
def test_open_linkedIn(page,username,password):
    Log =  LoginPage(page)
    Log.login(username, password)
    Sidemen = Sidemenu(page)
    assert Sidemen.open_LinkedIn()
@pytest.mark.parametrize("username, password", [(first_row_data['username'], first_row_data['password'])])
def test_open_Facebook(page,username,password):
    Log =  LoginPage(page)
    Log.login(username, password)
    Sidemen = Sidemenu(page)
    assert Sidemen.open_Facebook()

@pytest.mark.parametrize("username, password", [(first_row_data['username'], first_row_data['password'])])
def test_navigate_about(page,username,password):
    Log =  LoginPage(page)
    Log.login(username, password)
    Sidemen = Sidemenu(page)
    Sidemen.open_sidemenu()
    Sidemen.open_about()
    assert Sidemen.is_about_works()

@pytest.mark.parametrize("username, password", [(first_row_data['username'], first_row_data['password'])])
def test_allitem(page,username,password):
    Log =  LoginPage(page)
    Log.login(username,password)
    Sidemen = Sidemenu(page)
    Sidemen.open_sidemenu()
    Sidemen.open_resetapp()








