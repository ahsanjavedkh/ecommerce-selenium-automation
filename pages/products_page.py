from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # ======================
    # Locators
    # ======================

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

    cart_button = (
        By.XPATH,
        "//p[normalize-space()='Cart']"
    )

    checkout_button = (
        By.XPATH,
        "//button[contains(.,'Proceed to Checkout')]"
    )

    payment_method_button = (
        By.XPATH,
        "//button[contains(.,'Proceed to Payment Method')]"
    )

    recipient_name = (
        By.XPATH,
        "//input[@placeholder='Recipient Name']"
    )

    recipient_phone = (
        By.XPATH,
        "//input[@placeholder='Recipient Phone Number']"
    )

    finalize_button = (
        By.XPATH,
        "//button[contains(.,'Proceed to Finalize')]"
    )

    place_order_button = (
        By.XPATH,
        "//button[normalize-space()='Place Order']"
    )

    # ======================
    # Methods
    # ======================

    def search_product(self, product_name):

        search = self.wait.until(
            EC.visibility_of_element_located(
                self.search_box
            )
        )

        search.clear()
        search.send_keys(product_name)
        search.send_keys(Keys.ENTER)

        print("Search executed")

    def open_product(self):

        product = self.wait.until(
            EC.element_to_be_clickable(
                self.product_card
            )
        )

        product.click()

        print("Product opened")

    def add_to_cart(self):

        add_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.add_to_cart_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            add_btn
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            add_btn
        )

        print("Product added to cart")

    def open_cart(self):

        self.driver.execute_script(
            "window.scrollTo(0, 0);"
        )

        time.sleep(2)

        cart = self.wait.until(
            EC.presence_of_element_located(
                self.cart_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            cart
        )

        time.sleep(3)

        print("Cart opened")

    def proceed_to_checkout(self):

        checkout = self.wait.until(
            EC.element_to_be_clickable(
                self.checkout_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            checkout
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            checkout
        )

        time.sleep(3)

        print("Proceeded to checkout")

    def proceed_to_payment_method(self):

        payment_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.payment_method_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            payment_btn
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            payment_btn
        )

        time.sleep(3)

        print("Moved to Payment Method")

    def fill_recipient_details(self, name, phone):

        name_field = self.wait.until(
            EC.visibility_of_element_located(
                self.recipient_name
            )
        )

        phone_field = self.wait.until(
            EC.visibility_of_element_located(
                self.recipient_phone
            )
        )

        name_field.clear()
        name_field.send_keys(name)

        phone_field.clear()
        phone_field.send_keys(phone)

        time.sleep(2)

        print("Recipient details entered")

    def proceed_to_finalize(self):

        finalize_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.finalize_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            finalize_btn
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            finalize_btn
        )

        time.sleep(3)

        print("Moved to Finalize")

    def place_order(self):

        place_btn = self.wait.until(
            EC.presence_of_element_located(
                self.place_order_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            place_btn
        )

        time.sleep(3)

        print("Displayed:", place_btn.is_displayed())
        print("Enabled:", place_btn.is_enabled())

        try:
            place_btn.click()

        except Exception as e:

            print("Normal click failed:", e)

            try:
                self.driver.execute_script(
                    "arguments[0].click();",
                    place_btn
                )

            except Exception as e:

                print("JS click failed:", e)

                ActionChains(self.driver) \
                    .move_to_element(place_btn) \
                    .click() \
                    .perform()

        time.sleep(5)

        print("Order placed successfully")