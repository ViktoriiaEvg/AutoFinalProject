import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class ClientInfoPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    phone_number_input = "//input[@name='root_phone']"
    delivery_method_button = "//div[@data-id='27']"
    delivery_point_button = "//li[@id='point-1']"
    confirm_point_button = "(//span[text()='Заберу отсюда'])[1]"
    payment_method_button = "//div[@data-id='3']"
    confirmation_method_button = "//input[@id='notify-2']"
    call_time_selector = "//div[@data-testid='Select__label']"
    cookie_button = "//button[@title='Закрыть']"
    init_button = "//span[text()='Оформить заказ']"


    # Getters

    def get_phone_input(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.phone_number_input)))

    def get_delivery_method_button(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.delivery_method_button)))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    def get_delivery_point_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.delivery_point_button)))

    def get_confirm_point_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.confirm_point_button)))

    def get_payment_method_button(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.payment_method_button)))
        self.driver.execute_script("""
                arguments[0].scrollIntoView({block: 'start', behavior: 'auto'});
                window.scrollBy(0, -120); 
            """, element)
        WebDriverWait(self.driver, 5).until(
            lambda d: d.execute_script("return arguments[0].getBoundingClientRect().top > 0;", element))
        return element

    def get_confirmation_method_button(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.confirmation_method_button)))
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, self.confirm_point_button)))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    def get_call_time_selector(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.call_time_selector)))

    def get_cookie_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.cookie_button)))

    def get_init_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.init_button)))

    # Actions

    def input_phone(self, number):
        self.get_phone_input().send_keys(number)
        print("Input phone number")

    def pick_delivery_method(self):
        self.get_delivery_method_button().click()
        print("Clicked on delivery method")

    def pick_delivery_point(self):
        self.get_delivery_point_button().click()
        self.get_confirm_point_button().click()
        time.sleep(3)
        print("Picked delivery point")

    def pick_payment_method(self):
        self.get_payment_method_button().click()
        print("Picked payment method")

    def pick_contact_method(self):
        self.get_confirmation_method_button().click()
        assert self.get_call_time_selector().is_displayed()
        print("Picked contact method successfully!")

    def close_cookie_sheet(self):
        self.get_cookie_button().click()

    # Methods
    def input_information(self):
        self.get_current_url()
        self.close_cookie_sheet()
        self.input_phone("9999999999")
        self.pick_delivery_method()
        self.pick_delivery_point()
        self.pick_payment_method()
        self.pick_contact_method()
        assert self.get_init_button().is_displayed()
        print("Information input successful!")
