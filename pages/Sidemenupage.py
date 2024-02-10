# login_page.py
from . import Helper
import time
class Sidemenu:
    def __init__(self, page):
        self.page = page
        self.helper = Helper.helper(page)  # Create an instance of the Helper class

    def open_sidemenu(self):
        self.page.get_by_role("button", name="Open Menu").click()

    def open_about(self):
        self.page.get_by_role("link", name="About").click()

    def logout(self):
        self.page.get_by_role("link", name="Logout").click()

    def is_loggedout(self):
        return self.helper.is_at_url('https://www.saucedemo.com/')
    def open_resetapp(self):
        self.page.get_by_role("link", name="Reset App State").click()

    def open_allitem(self):
        self.page.get_by_role("link", name="All Items").click()

    def is_about_works(self):
        return self.helper.is_at_url('https://saucelabs.com/')

    def open_twitter(self):
        context = self.page.context
        with context.expect_page() as popup_info:
            self.page.get_by_role("link", name="Twitter").click()
        new_page = popup_info.value
        new_page.wait_for_load_state()
        print(new_page.title())
        print(new_page.url)
        self.helper = Helper.helper(new_page)
        return self.helper.is_at_url('https://twitter.com/saucelabs')


    def open_LinkedIn(self):
        context = self.page.context
        with context.expect_page() as popup_info:
            self.page.get_by_role("link", name="LinkedIn").click()
        new_page = popup_info.value
        new_page.wait_for_load_state()
        print(new_page.title())
        print(new_page.url)
        self.helper = Helper.helper(new_page)
        return self.helper.is_at_url('https://www.LinkedIn.com/saucelabs')
    def open_Facebook(self):
        context = self.page.context
        with context.expect_page() as popup_info:
            self.page.get_by_role("link", name="Facebook").click()
        new_page = popup_info.value
        new_page.wait_for_load_state()
        print(new_page.title())
        print(new_page.url)
        self.helper = Helper.helper(new_page)
        return self.helper.is_at_url('https://www.facebook.com/saucelabs')


    def is_at_twitter(self):
        self.driver.switch_to.new_window()  # Switch to the new tab
        self.helper = Helper.helper(self.page)
        return self.helper.is_at_url('https://twitter.com/saucelabs')
