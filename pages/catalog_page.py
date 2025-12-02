from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class CatalogPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    category_link = "(//a[@href='/refrigerator/two_chambered_refrigerators/'])[2]"
    max_price_input = "//input[@id='max_txt_price']"
    type_tag = "//a[@href='/refrigerator/two_chambered_refrigerators/tags/color_bejevie/']"
    model_checkbox = "//input[@alias='haier']"
    country_checkbox = "//input[@alias='2138']"
    apply_button = "//input[@id='cfilter_btnsubmit']"
    item_link = "//input[@href='/refrigerator/two_chambered_refrigerators/haier/c4f640ccgu1/']"

    # Getters
    def get_category_link(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.category_link)))

    def get_type_tag(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.type_tag)))

    def get_max_price_input(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.max_price_input)))

    def get_model_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.model_checkbox)))

    def get_country_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.country_checkbox)))

    def get_apply_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.apply_button)))

    def get_close_banner(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.close_banner)))

    # Actions
    def click_category_link(self):
        self.get_category_link().click()
        print("Clicked category")

    def click_type_tag(self):
        self.get_type_tag().click()
        print("Opened a tag")

    def input_max_price(self):
        self.get_max_price_input().click()
        self.get_max_price_input().clear()
        self.get_max_price_input().send_keys('140000')
        print("Input max price")

    def click_model_checkbox(self):
        self.get_model_checkbox().click()
        print("Clicked on a model")

    def click_country_checkbox(self):
        self.get_country_checkbox().click()
        print("Clicked on a country")

    def click_apply_button(self):
        self.get_apply_button().click()
        print("Applied filters")

    # Methods
    def pick_an_item(self):
        self.click_category_link()
        self.click_type_tag()
        self.input_max_price()
        self.click_model_checkbox()
        self.click_country_checkbox()
        self.click_apply_button()
