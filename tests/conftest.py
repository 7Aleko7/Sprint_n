import pytest
from selenium import webdriver
from urls import Urls
from data import TestData
from pages.main_page import MainPage

@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()

@pytest.fixture
def open_main_page(driver):
    driver.get(Urls.BASE_URL)

@pytest.fixture
def enter_addresses(driver, open_main_page):
    page=MainPage(driver)
    page.enter_address_in_input_from(TestData.addresses[1])
    page.enter_address_in_input_to(TestData.addresses[0])