# login_page.py
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://www.saucedemo.com/"

    def navigate_to_login_page(self):
        self.page.goto(self.url)

    def enter_username(self, username):
        self.page.fill("#user-name", username)

    def enter_password(self, password):
        self.page.fill("#password", password)


    def click_login_button(self):
        self.page.click("#login-button")

    def login(self, username, password):
        self.navigate_to_login_page()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def is_logged_in(self):
        return self.page.url == "https://www.saucedemo.com/inventory.html"

    def is_locked(self):
        error= self.page.locator("[data-test=\"error\"]").text_content()
        print(error)
        if 'locked' in str(error):
            return True
        else:
            return False