# checkout_page.py
class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def enter_shipping_information(self, name, address, zip_code):
        self.page.fill("#first-name", name)
        self.page.fill("#last-name", address)
        self.page.fill("#postal-code", zip_code)

    # Add more methods as needed for interacting with elements on the checkout page
    def checkout(self):
        self.page.locator("[data-test=\"checkout\"]").click()
    def contin(self):
        self.page.locator('#continue').click()

    def finish(self):
        self.page.locator('#finish').click()
    @property
    def total_price_selector(self):
        return 'div.summary_info_label.summary_total_label'

    @property
    def item_price_selector(self):
        return 'div.summary_subtotal_label'

    @property
    def tax_price_selector(self):
        return 'div.summary_tax_label'


    def get_price(self, selector):
        price_element = self.page.query_selector(selector)
        if price_element:
            price_text = price_element.text_content()
            price = float(price_text.split('$')[1])
            return price
        else:
            return None
    def issuccessful(self):
        element= self.page.query_selector('h2:has-text("Thank you for your order!")')
        if  element:
            return True