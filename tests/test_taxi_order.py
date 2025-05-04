import allure
import pytest
from data import TestData
from locators.main_page_locators import MainPageLocators as Mpg
from pages.main_page import MainPage

class TestTaxiOrder:

    @allure.title('При нажатие Вызвать открывается форма заказа со всеми 6 тарифами по ТЗ, один из них активный')
    def test_order_taxi_form_with_six_tariffs(self, driver, enter_addresses):
        page=MainPage(driver)
        page.click_on_fast_mode()
        page.click_on_call_taxi_button()
        page.check_visibility_six_taxi_tariffs()
        page.check_one_tariff_card_is_active()


    tariffs = [(Mpg.TARIFF_WORKER, TestData.TARIFF_WORKER_DESCRIPTION),
               (Mpg.TARIFF_SLEEPY, TestData.TARIFF_SLEEPY_DESCRIPTION),
               (Mpg.TARIFF_VACATION, TestData.TARIFF_VACATION_DESCRIPTION),
               (Mpg.TARIFF_TALKATIVE, TestData.TARIFF_TALKATIVE_DESCRIPTION),
               (Mpg.TARIFF_COMFORTING, TestData.TARIFF_COMFORTING_DESCRIPTION),
               (Mpg.TARIFF_GLOSSY, TestData.TARIFF_GLOSSY_DESCRIPTION)]

    @allure.title('Проверка описания тарифов в тултипах')
    @pytest.mark.parametrize("tariff_locator, tariff_description", tariffs)
    def test_taxi_tariffs_description_in_tooltips(self, driver, enter_addresses,tariff_locator, tariff_description):
        page = MainPage(driver)
        page.click_on_fast_mode()
        page.click_on_call_taxi_button()
        page.click_on_element(tariff_locator)
        page.move_cursor_on_tariff_card_tooltip()
        assert page.find_element_on_page_by_text(tariff_description)

    @allure.title('Проверка полей в форме заказа такси')
    @allure.description('Проверяем наличие полей: Телефон, Способ оплаты, Комментарий водителю, Требования к заказу')
    def test_order_taxi_form_fields(self, driver, enter_addresses):
        page=MainPage(driver)
        page.click_on_fast_mode()
        page.click_on_call_taxi_button()
        page.check_order_taxi_form_fields()

    @allure.title('Проверка окна ожидания машины')
    @allure.description('Проверяем что в окне ожидания машины отображаются Заголовок: Поиск машины, Таймер, кнопки Отменить и Детали')
    def test_car_waiting_window(self, driver, enter_addresses):
        page = MainPage(driver)
        page.click_on_fast_mode()
        page.click_on_call_taxi_button()
        page.click_on_tariff_worker()
        page.click_on_order_requirements()
        page.click_on_switcher_laptop_table()
        page.click_on_order_taxi_button()
        page.check_waiting_car_window()

    @allure.title('Проверка окна оформленного заказа')
    @allure.description('Проверяем что в окне оформленного заказа отображаются: заголовок, номер и картинка автомобиля, Имя, рейтинг и фото водителя, кнопки Отменить и Детали')
    def test_completed_order_window(self, driver, enter_addresses):
        page = MainPage(driver)
        page.click_on_fast_mode()
        page.click_on_call_taxi_button()
        page.click_on_tariff_worker()
        page.click_on_order_requirements()
        page.click_on_switcher_laptop_table()
        page.click_on_order_taxi_button()
        page.wait_invisibility_of_timer_search_car()
        page.check_completed_order_window()

    @allure.title('Проверка что стоимость в деталях заказа соответствует стоимости при выборе тарифа')
    def test_tariff_price_in_order_details_window_respond_tariff_price_before_placing_order(self, driver, enter_addresses):
        page = MainPage(driver)
        page.click_on_fast_mode()
        page.click_on_call_taxi_button()
        page.click_on_tariff_worker()
        first_price = page.get_active_tariff_price()
        page.click_on_order_requirements()
        page.click_on_switcher_laptop_table()
        page.click_on_order_taxi_button()
        page.wait_invisibility_of_timer_search_car()
        page.click_on_order_details_button()
        second_price = page.get_tariff_details_price()
        assert first_price == second_price

    @allure.title('Проверка закрытия окна по оформленного заказа при нажатие кнопки Отменить')
    @pytest.mark.xfail(reason="Баг")
    def test_cancel_taxi_order(self, driver, enter_addresses):
        page = MainPage(driver)
        page.click_on_fast_mode()
        page.click_on_call_taxi_button()
        page.click_on_tariff_worker()
        page.click_on_order_requirements()
        page.click_on_switcher_laptop_table()
        page.click_on_order_taxi_button()
        page.wait_invisibility_of_timer_search_car()
        page.click_on_order_cancel_button()
        page.check_invisibility_of_order_window()