from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class MainPage(Base):

    url = "https://www.holodilnik.ru/"
    user_name = ""
    password = ""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    open_login_button = "//span[@class='site-header__user-item-link-icon']"
    password_login_link= "//div[@class='auth__link auth__link_sign-by-passw link']"
    user_name_input = "//input[@id='controlInput_15']"
    password_input = "//input[@id='controlInput_16']"
    login_button = "//div[@class='auth__btn']"
    modal_dialog = "//div[@id='auth-manzana'"
    catalog_button = "//div[@class='site-header__search-burger'"
    refrigerator_button = "//a[@href='/refrigerator/']"

    # Getters

    def get_auth_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.open_login_button)))

    def get_password_login_link(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.password_login_link)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.user_name_input)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.password_input)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_dialog_text(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.catalog_button)))


    def get_refrigerator(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.refrigerator_button)))

    # Actions

    def open_login_dialog(self):
        self.get_auth_button().click()
        print("Opened auth dialog")

    def open_password_login(self):
        self.get_password_login_link().click()
        print("Opened password login")

    def input_user_name(self, username):
        self.get_user_name().send_keys(username)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    def click_catalog_button(self):
        self.get_auth_button().click()
        print("Clicked on catalog button")

    def click_on_refrigerator(self):
        self.get_refrigerator().click()
        print("Clicked on 'Refrigerators'")

    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.open_login_dialog()
        self.open_password_login()
        self.input_user_name(self.user_name)
        self.input_password(self.password)
        self.click_login_button()
        self.assert_text(self.get_dialog_text(), "Авторизация прошла успешно")
        body = self.driver.find_element("tag name", "body")
        body.click()  # to close a modal
        print("Authorization successful")

    def open_catalog(self):
        #for now, before auth is fixed
        self.driver.get(self.url)
        self.driver.maximize_window()
        body = self.driver.find_element("tag name", "body")
        body.click() #to close a modal
        self.click_catalog_button()
        self.click_on_refrigerator()
        self.assert_url("https://www.holodilnik.ru/refrigerator/")
        print("Opened catalog")



