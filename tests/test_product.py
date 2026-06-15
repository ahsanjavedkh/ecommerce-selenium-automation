from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import EMAIL, PASSWORD

from pages.login_page import LoginPage
from pages.products_page import ProductsPage

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://maelano.com/login")

# Login
login = LoginPage(driver)

login.login(
    EMAIL,
    PASSWORD
)

wait = WebDriverWait(driver, 20)

wait.until(
    EC.url_contains("dashboard")
)

print("Current URL after login:")
print(driver.current_url)

# Open landing page
driver.get("https://maelano.com/landingpage")

print("URL after get():")
print(driver.current_url)

# Create ProductsPage object
product = ProductsPage(driver)

# Search product
product.search_product("shirt")

# Open first product
product.open_product()

# Add to cart
product.add_to_cart()

# Open cart
product.open_cart()
# checkout
product.proceed_to_checkout()
product.proceed_to_payment_method()
product.fill_recipient_details(
    "Musa Bajwa",
    "3369958739"
)

product.proceed_to_finalize()
product.place_order()

input("Press Enter to close browser...")

driver.quit()


