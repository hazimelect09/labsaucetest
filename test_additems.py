# test_login.py
import time
import logging
import time
import pytest
from  playwright_base import browser, context, page
from pages.Loginpage import LoginPage
from pages.Items import Items
from pages.Checkoutpage import CheckoutPage
from pages.Helper import helper
from Excelreader import read_test_data

# Read test data from Excel file
test_data_1 = read_test_data('data/test_data.xlsx', 'Sheet1')
test_data_2 = read_test_data('data/test_data.xlsx', 'Sheet1')
test_data_3 = read_test_data('data/test_data.xlsx', 'Sheet1')


@pytest.mark.parametrize("username, password, item_name, expected_tax,first_name,last_name,zip_code", [(data['username'], data['password'], data['item_name'], data['expected_tax'],data['first_name'],data['last_name'],data['zip_code']) for data in test_data_3])

def test_addremove_items(page, username, password, item_name, expected_tax, first_name, last_name, zip_code):
    login_page = LoginPage(page)
    login_page.login(username, password)
    item = Items(page)
    item.add_item(item_name)
    new_cart_count = item.show_items_count()
    assert new_cart_count == 1
    item.remove_item(item_name)
    item.show_cart()
    assert item.is_cart_empty()


# Read test data from CSV file
@pytest.mark.parametrize("username, password, item_name, expected_tax,first_name,last_name,zip_code", [(data['username'], data['password'], data['item_name'], data['expected_tax'],data['first_name'],data['last_name'],data['zip_code']) for data in test_data_1])
def test_checkout(page, username, password, item_name, expected_tax,first_name,last_name,zip_code):
    login_page = LoginPage(page)
    login_page.login(username, password)
    item = Items(page)
    item.add_item(item_name)
    new_cart_count = item.show_items_count()
    assert new_cart_count == 1
    item.show_cart()
    check = CheckoutPage(page)
    check.checkout()
    check.enter_shipping_information(first_name, last_name, str(zip_code))
    check.contin()
    tax = check.get_price(check.tax_price_selector)
    assert tax == float(expected_tax)
    check.finish()
    assert check.issuccessful()
    time.sleep(3)

@pytest.mark.parametrize("username, password, item_name, expected_tax",[(data['username'], data['password'], data['item_name'], data['expected_tax']) for data in test_data_1])
def test_order_items_by_price_high_to_low(page, username, password, item_name, expected_tax):
    login_page = LoginPage(page)
    login_page.login(username, password)
    item = Items(page)
    item_prices_before_order = item.get_item_prices()
    item.order_pricehtl()
    item_prices_after_order =item.get_item_prices()
    sorted_prices = sorted(item_prices_before_order, reverse=True)
    # Verify that the items are displayed in descending order of price
    assert item_prices_after_order == sorted_prices, "Items are not ordered by price high to low"

