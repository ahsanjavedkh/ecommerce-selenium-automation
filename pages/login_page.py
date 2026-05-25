from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # Locators
    login_user_btn = (By.XPATH, "//label[contains(text(),'Login as User')]")
    email_input = (By.XPATH, "//input[@name='loginEmail']")
    password_input = (By.XPATH, "//input[@type='password']")
    terms_checkbox = (By.XPATH, "//input[@id='terms']")
    login_button = (By.XPATH, "//button[@type='submit']")

    def click_login_user(self):
        self.wait.until(
            EC.element_to_be_clickable(self.login_user_btn)
        ).click()

    def enter_email(self, email):
        self.wait.until(
            EC.presence_of_element_located(self.email_input)
        ).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(
            *self.password_input
        ).send_keys(password)

    def click_checkbox(self):
        self.driver.find_element(
            *self.terms_checkbox
        ).click()

    def click_login(self):
        self.driver.find_element(
            *self.login_button
        ).click()

    def login(self, email, password):

        self.click_login_user()

        self.enter_email(email)

        self.enter_password(password)

        self.click_checkbox()

        self.click_login()