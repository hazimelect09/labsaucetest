
class Items:
    def __init__(self, page):
        self.page = page
        self.url = "https://www.saucedemo.com/"

    def find_item(self,elm):
        selector = f'a:has-text("{elm}")'
        item = self.page.locator(selector)
        item.click()
    def is_item_available(self,partial_text):
        selector = f'div.inventory_item a[id^="item_"] .inventory_item_name'
        item_element = self.page.query_selector(selector)
        if item_element and partial_text in item_element.text_content():
            return True
        else:
            return False


    def add_item(self, partial_name):
        items = self.page.query_selector_all('.inventory_item')  # Get all inventory items
        for item in items:
            name_element = item.query_selector('.inventory_item_name')  # Get the name element
            if name_element:
                item_name = name_element.text_content()  # Get the text content of the name element
                if partial_name in item_name:  # Check if the partial name is in the item name
                    add_to_cart_button = item.query_selector('.btn_inventory')  # Get the "Add to cart" button
                    if add_to_cart_button:
                        add_to_cart_button.click()  # Click on the "Add to cart" button
                        print(f"Item '{item_name}' added to cart.")
                        return  # Exit the function after adding the item to cart
        print(f"Item with partial name '{partial_name}' not found.")


    def remove_item(self,partial_name):
        items = self.page.query_selector_all('.inventory_item')  # Get all inventory items
        for item in items:
            name_element = item.query_selector('.inventory_item_name')  # Get the name element
            if name_element:
                item_name = name_element.text_content()  # Get the text content of the name element
                if partial_name in item_name:  # Check if the partial name is in the item name
                    remove_item = item.query_selector('.btn_inventory')  # Get the "Add to cart" button
                    if remove_item:
                        remove_item.click()  # Click on the "Add to cart" button
                        return  # Exit the function after adding the item to cart
    def show_cart(self):
        self.page.locator("#shopping_cart_container a").click()
    def order_alphatz(self):
        self.page.locator("[data-test=\"product_sort_container\"]").select_option("az")
    def is_cart_empty(self):
        element = self.page.query_selector('div.cart_item')
        if not element:
            return True
        else:
            return False

    def get_total_price(self):
        total_element = self.page.query_selector('div.summary_info_label.summary_total_label')
        if total_element:
            total_text = total_element.text_content()
            total_price = float(total_text.split('$')[1])
            return total_price
        else:
            return None
    def get_item_price(self):
        total_element = self.page.query_selector('div.summary_subtotal_label')
        if total_element:
            total_text = total_element.text_content()
            total_price = float(total_text.split('$')[1])
            return total_price
        else:
            return None
    def get_tax_price(self):
        total_element = self.page.query_selector('div.summary_tax_label')
        if total_element:
            total_text = total_element.text_content()
            total_price = float(
                total_text.split('$')[1])
            return total_price
        else:
            return None

    def order_alphatz(self):
        self.page.locator("[data-test=\"product_sort_container\"]").select_option("za")
    def show_items_count(self):
        return int(self.page.locator("#shopping_cart_container a").text_content())
    def order_pricehtl(self):
        self.page.locator("[data-test=\"product_sort_container\"]").select_option("hilo")
    def order_pricelth(self):
        self.page.locator("[data-test=\"product_sort_container\"]").select_option("lohi")
    def get_item_prices(self):
        item_prices = []
        items = self.page.query_selector_all('.inventory_item')
        for item in items:
            price_element = item.query_selector('.inventory_item_price')
            if price_element:
                price_text = price_element.text_content().replace('$', '')
                item_prices.append(float(price_text))
        return item_prices