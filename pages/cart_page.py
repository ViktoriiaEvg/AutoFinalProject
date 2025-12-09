import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    add_more_button = "//button[@data-testid='counterIncrement']"
    product_counter = "//input[@data-testid='counterInput']"
    checkout_button = "//button[text()='Перейти к оформлению']"

    # Getters

    def get_add_more_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.add_more_button)))

    def get_product_counter(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_counter)))

    def get_checkout_button(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.checkout_button)))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element


    # Actions

    def click_add_product(self):
        self.get_add_more_button().click()
        print("Clicked add more")

    def click_checkout(self):
        checkout_button = self.get_checkout_button()
        time.sleep(3)
        checkout_button.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.title_is("Оформление заказа")) #Wainting for the next page to load
        print("Opened Checkout")


    # Methods
    def increase_product_count(self):
        self.click_add_product()
        assert self.get_product_counter().get_attribute("value") == "2"
        print("The product quantity is increased")

    def product_confirmation(self):
        self.get_current_url()
        self.click_checkout()
        self.assert_url("https://www.petshop.ru/personal/order/make/")
