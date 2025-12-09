import time

import pytest
from selenium import webdriver

from pages.cart_page import CartPage
from pages.client_info_page import ClientInfoPage
from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from pages.product_page import ProductPage


def test_buy_product():
    driver = webdriver.Firefox()

    mp = MainPage(driver)
    mp.open_catalog()

    cp = CatalogPage(driver)
    cp.apply_filters()
    cp.open_product_page()

    pp = ProductPage(driver)
    pp.add_product_to_cart()
    pp.open_cart_page()

    crtp = CartPage(driver)
    crtp.increase_product_count()
    crtp.product_confirmation()

    cip = ClientInfoPage(driver)
    cip.input_information()

    time.sleep(5)
    driver.close()
