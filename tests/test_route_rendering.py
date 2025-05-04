import allure
import pytest
from data import TestData
from pages.main_page import MainPage

class TestRouteRendering:
    addresses = [(TestData.addresses[0], TestData.addresses[1]),
                 (TestData.addresses[1], TestData.addresses[0])
                  ]

    @allure.title('После ввода адресов в Поля откуда и Куда на карте отображается маршрут')
    @allure.description('Проверяем отображение двух точек маршрута и их адрес')
    @pytest.mark.parametrize("address_from, address_to", addresses)
    def test_rendering_route_on_map(self, driver, open_main_page, address_from, address_to):
        page=MainPage(driver)
        page.enter_address_in_input_from(address_from)
        page.enter_address_in_input_to(address_to)
        page.check_route_from_point(address_from)
        page.check_route_to_point(address_to)