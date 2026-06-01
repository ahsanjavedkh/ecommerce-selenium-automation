from selenium import webdriver
from pages.login_page import LoginPage
from config import EMAIL, PASSWORD
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://maelano.com/login")

# Create object
login = LoginPage(driver)

# Call reusable login function
from config import EMAIL, PASSWORD

login.login(
    EMAIL,
    PASSWORD
)

print("Login flow executed successfully!")

time.sleep(10)

input("Press Enter to close browser...")

driver.quit()