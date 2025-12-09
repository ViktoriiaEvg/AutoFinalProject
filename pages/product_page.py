from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class ProductPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    add_to_cart_button = "//button[text()='В корзину']"
    product_name = "//h1"
    cart_counter = "//span[@data-testid='cart-counter-count']"
    open_cart_button = "(//a[@href='/personal/cart/'])[3]"

    # Getters
    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_product_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_name)))

    def get_cart_counter(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_counter)))

    def get_open_cart_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.open_cart_button)))

    # Actions
    def add_to_cart(self):
        self.get_add_to_cart_button().click()
        print("Clicked add to cart button")

    def open_cart(self):
        self.get_open_cart_button().click()

    # Methods
    def add_product_to_cart(self):
        self.add_to_cart()
        self.assert_text(self.get_cart_counter(), "1")
        print("Added product to cart")

    def open_cart_page(self):
        self.open_cart()
        self.assert_url("https://www.petshop.ru/personal/cart/")
