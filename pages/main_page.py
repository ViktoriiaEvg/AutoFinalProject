from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class MainPage(Base):

    url = "https://www.petshop.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    catalog_button = "//nav/a[@href='/catalog/dogs/']" #in the top menu
    treats_button = "//a[@href='/catalog/dogs/food/lakomstva-dlya-sobak/']"
    close_tutorial_button = "//button[@class='TutoringEcoTooltip_button__zhTqX']"

    # Getters

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.catalog_button)))


    def get_treats_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.treats_button)))

    def get_tutorial_close_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.close_tutorial_button)))

    # Actions

    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Clicked on catalog button")

    def click_on_treats(self):
        self.get_treats_button().click()
        print("Clicked on 'Treats'")

    def close_tutorial(self):
        self.get_tutorial_close_button().click()
        print("Closed tutorial")

    # Methods

    def open_catalog(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.close_tutorial()
        self.click_catalog_button()
        self.close_promo()
        self.click_on_treats()
        self.assert_url("https://www.petshop.ru/catalog/dogs/food/lakomstva-dlya-sobak/")
        print("Opened the catalog")



