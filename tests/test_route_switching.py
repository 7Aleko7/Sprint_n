import allure
from pages.main_page import MainPage
from pytest_check import check

class TestRouteSwitching:

    @allure.title('Переключение вида на Оптимальный')
    @allure.description('Проверяем что после переключения стал активным таб Оптимальный и изменилось время или стоимость маршрута')
    def test_switch_mode_to_optimal(self, driver, enter_addresses):
        page=MainPage(driver)
        first_cost = page.save_route_cost()
        first_time = page.save_route_time()
        page.click_on_optimal_mode()
        second_cost = page.save_route_cost()
        second_time = page.save_route_time()
        page.check_optimal_is_active()
        with check: assert first_cost != second_cost or first_time != second_time

    @allure.title('Переключение вида на Свой')
    @allure.description('Проверяем что после переключения стал активным таб Свой и и доступны все типы маршрута')
    def test_switch_mode_to_mine(self, driver, enter_addresses):
        page=MainPage(driver)
        page.click_on_mine_mode()
        page.check_mine_is_active()
        page.check_all_type_is_not_disabled()

    @allure.title('При выборе вида маршрута Быстрый активна кнопка Вызвать такси')
    def test_call_taxi_button_visible_on_fast_mode(self, driver, enter_addresses):
        page=MainPage(driver)
        page.click_on_fast_mode()
        page.check_visibility_call_taxi_button()

    @allure.title('При выборе вида маршрута Свой, типа передвижения Драйв активна кнопка Забронировать')
    def test_rent_button_visible_on_mine_mode_and_drive_type(self, driver, enter_addresses):
        page=MainPage(driver)
        page.click_on_mine_mode()
        page.click_on_drive_type()
        page.check_visibility_rent_button()