from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # Locators
    search_box = (
        By.XPATH,
        "//input[@placeholder='Looking for something specific?']"
    )

    product_card = (
        By.XPATH,
        "//div[contains(@class,'ProductCard_card')]"
    )

    add_to_cart_button = (
        By.XPATH,
        "//button[contains(text(),'ADD TO CART')]"
    )

    # Methods
    def search_product(self, product_name):

        search = self.wait.until(
            EC.visibility_of_element_located(self.search_box)
        )

        search.clear()
        search.send_keys(product_name)
        search.send_keys(Keys.ENTER)

        print("Search executed")


    def open_product(self):

        product = self.wait.until(
            EC.element_to_be_clickable(self.product_card)
        )

        product.click()

        print("Product opened")


    def add_to_cart(self):

        add_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.add_to_cart_button
            )
        )
        time.sleep(3)
        add_btn.click()

        print("Product added to cart")