import allure
import pytest
from data import TestData
from pages.main_page import MainPage

class TestRouteOptionsBlock:
    different_addresses = [(TestData.addresses[0], TestData.addresses[1]),
                 (TestData.addresses[1], TestData.addresses[0])
                 ]

    @allure.title('После ввода разных адресов в Поля откуда и Куда отображается блок с выбором маршрута')
    @pytest.mark.parametrize("address_from, address_to", different_addresses)
    def test_route_block_for_different_addresses(self, driver, open_main_page, address_from, address_to):
        page = MainPage(driver)
        page.enter_address_in_input_from(address_from)
        page.enter_address_in_input_to(address_to)
        page.check_route_options_block_is_visibility()



    same_addresses = [(TestData.addresses[0], TestData.addresses[0]),
                           (TestData.addresses[1], TestData.addresses[1])
                           ]

    @allure.title('После ввода одинаковых адресов в Поля откуда и Куда отображается блок с выбором маршрута в котором указано "Авто Бесплатно В пути 0 мин."')
    @pytest.mark.parametrize("address_from, address_to", same_addresses)
    def test_route_block_for_same_addresses(self, driver, open_main_page, address_from, address_to):
        page = MainPage(driver)
        page.enter_address_in_input_from(address_from)
        page.enter_address_in_input_to(address_to)
        page.check_route_options_block_for_same_addresses()