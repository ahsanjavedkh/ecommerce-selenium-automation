from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from config import EMAIL, PASSWORD
import time

from pages.login_page import LoginPage
from pages.products_page import ProductsPage

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://maelano.com/login")

login = LoginPage(driver)

login.login(
    EMAIL,
    PASSWORD
)

wait = WebDriverWait(driver,20)

wait.until(
    EC.url_contains("dashboard")
)

print("Current URL after login:")
print(driver.current_url)

driver.get("https://maelano.com/landingpage")

print("URL after get():")
print(driver.current_url)

time.sleep(5)

product = ProductsPage(driver)

# Search shirt
product.search_product("shirt")
product.open_product()
# Add to cart
product.add_to_cart()
input("Press Enter...")
driver.quit()