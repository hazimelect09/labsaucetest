
class helper:
    def __init__(self, page):
        self.page = page
    def navigate_to(self,url):
        self.page.goto(url)

    def is_at_url(self,url):
        current_url =self.page.url
        if current_url == url:
            return True
        else:
            return False