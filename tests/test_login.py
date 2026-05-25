from selenium import webdriver
from pages.login_page import LoginPage
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://maelano.com/login")

# Create object
login = LoginPage(driver)

# Call reusable login function
login.login(
    "nodejsdevelopertsp@gmail.com",
    "123456"
)

print("Login flow executed successfully!")

time.sleep(10)

input("Press Enter to close browser...")

driver.quit()