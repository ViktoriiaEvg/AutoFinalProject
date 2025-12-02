import time

import pytest
from selenium import webdriver

from pages.cart_page import CartPage
from pages.client_info_page import ClientInfoPage
from pages.main_page import MainPage
from pages.catalog_page import CatalogPage

# @pytest.mark.order(3)
def test_buy_product():
    driver = webdriver.Firefox()

    mp = MainPage(driver)
    # mp.authorization()
    mp.open_catalog()

    cp = CatalogPage(driver)
    cp.pick_an_item()


    time.sleep(2)
    driver.close()