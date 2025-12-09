from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class CatalogPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    brand_filter = "//button[@data-group-id='-1']"
    brand_checkbox = "//input[@id='369']"

    age_filter = "//button[@data-group-id='2']"
    age_checkbox = "//input[@id='783']"

    ingredient_filter = "//button[@data-group-id='4']"
    ingredient_checkbox = "//input[@id='808']"

    price_filter = "//button[@data-group-id='-2']"
    max_price_input = "//input[@name='field-max']"

    size_filter = "//button[@data-group-id='3']"
    size_checkbox = "//input[@id='787']"

    type_filter = "//button[@data-group-id='6']"
    type_checkbox = "//input[@id='865']"

    confirm_button = "//button[@class='BaseButton_root__67Mgg Button_root__Z8ate Button_fullWidth__ad0Xe Button_gradientVariant__FpASN']"
    reset_button = "//button[@class='BaseButton_root__67Mgg Button_root__Z8ate list-selected-filter_resetButton__5oJwH Button_textVariant__gub3S Button_preventAnimation__9Rvli']"

    product_card = "/html/body/div[1]/main/div[5]/section/div[1]/span/a"

    # Getters

    def get_brand_filter(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.brand_filter)))

    def get_brand_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.brand_checkbox)))

    def get_age_filter(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.age_filter)))

    def get_age_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.age_checkbox)))

    def get_ingredient_filter(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.ingredient_filter)))

    def get_ingredient_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.ingredient_checkbox)))

    def get_price_filter(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_filter)))

    def get_max_price_input(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.max_price_input)))

    def get_size_filter(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.size_filter)))

    def get_size_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.size_checkbox)))

    def get_type_filter(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.type_filter)))

    def get_type_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.type_checkbox)))

    def get_confirm_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.confirm_button)))

    def get_reset_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.reset_button)))


    def get_product_card(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_card)))


    # Actions

    def apply_brand_filter(self):
        self.get_brand_filter().click()
        self.get_brand_checkbox().click()
        self.get_confirm_button().click()
        print("Applied the brand filter")

    def apply_age_filter(self):
        self.get_age_filter().click()
        self.get_age_checkbox().click()
        self.get_confirm_button().click()
        print("Applied age filter")

    def apply_ingredient_filter(self):
        self.get_ingredient_filter().click()
        self.get_ingredient_checkbox().click()
        self.get_confirm_button().click()
        print("Applied ingredient filter")

    def apply_price_filter(self):
        self.get_price_filter().click()
        max_price = self.get_max_price_input()
        max_price.clear()
        max_price.click()
        max_price.send_keys("1500")
        self.get_confirm_button().click()
        print("Applied the price filter")

    def apply_size_filter(self):
        self.get_size_filter().click()
        self.get_size_checkbox().click()
        self.get_confirm_button().click()
        print("Applied size filter")

    def apply_type_filter(self):
        self.get_type_filter().click()
        self.get_type_checkbox().click()
        self.get_confirm_button().click()
        print("Applied type filter")

    def click_product_card(self):
        self.get_product_card().click()
        print("Clicked on the product")

    # Methods
    def apply_filters(self):
        self.get_current_url()
        try:
            self.apply_brand_filter()
        except ElementClickInterceptedException:
            self.close_promo()
            self.apply_brand_filter()
        self.apply_age_filter()
        self.apply_ingredient_filter()
        self.apply_price_filter()
        self.apply_size_filter()
        self.apply_type_filter()
        self.assert_text(self.get_reset_button(), "Сбросить фильтры")
        print("Filters applied")

    def open_product_page(self):
        self.click_product_card()
        self.get_current_url()
