from locators.main_page_locators import MainPageLocators as Mpg
from pages.base_page import BasePage
import allure
from selenium.webdriver import ActionChains
from pytest_check import check
import re

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Вводим адрес в поле Откуда')
    def enter_address_in_input_from(self, address):
        self.send_keys_to_input(Mpg.INPUT_FROM, address)

    @allure.step('Вводим адрес в поле Куда')
    def enter_address_in_input_to(self, address):
        self.send_keys_to_input(Mpg.INPUT_TO, address)

    @allure.step('Проверяем отображение точки Откуда и ее адреса')
    def check_route_from_point(self, address):
        point_with_address = (Mpg.FROM_POINT[0], f"{Mpg.FROM_POINT[1]}/parent::*[.//*[contains(., '{address}')]]")
        with check: assert self.wait_visibility_of_element(point_with_address)

    @allure.step('Проверяем отображение точки Куда и ее адреса')
    def check_route_to_point(self, address):
        point_with_address = (Mpg.TO_POINT[0], f"{Mpg.TO_POINT[1]}/parent::*[.//*[contains(., '{address}')]]")
        with check: assert self.wait_visibility_of_element(point_with_address)

    @allure.step('Проверяем отображение блока выбора маршрута')
    def check_route_options_block_is_visibility(self):
        with check: assert self.wait_visibility_of_element(Mpg.VISIBILITY_ROUTE_OPTIONS_BLOCK)

    @allure.step('Проверяем что в блоке выбора маршрута указано "Авто Бесплатно В пути 0 мин."')
    def check_route_options_block_for_same_addresses(self):
        with check: assert self.wait_visibility_of_element(Mpg.FREE_CAR) and self.wait_visibility_of_element(Mpg.ZERO_MINUTES_ROUTE)

    @allure.step('Сохраняем время маршрута')
    def save_route_time(self):
        route_time = self.get_element_text(Mpg.ROUTE_TIME)
        return route_time

    @allure.step('Сохраняем стоимость маршрута')
    def save_route_cost(self):
        route_cost = self.get_element_text(Mpg.ROUTE_COST)
        return route_cost

    @allure.step('Выбираем - Оптимальный')
    def click_on_optimal_mode(self):
        self.click_on_element(Mpg.MODE_OPTIMAL)

    @allure.step('Выбираем - Свой')
    def click_on_mine_mode(self):
        self.click_on_element(Mpg.MODE_MINE)

    @allure.step('Выбираем тип - Драйв')
    def click_on_drive_type(self):
        self.click_on_element(Mpg.TYPE_DRIVE)

    @allure.step('Выбираем - Быстрый')
    def click_on_fast_mode(self):
        self.click_on_element(Mpg.MODE_FAST)

    @allure.step('Проверяем активность таба')
    def check_active_tab(self, locator):
        tab = self.find_element(locator)
        return "active" in tab.get_attribute("class")

    @allure.step('Проверяем доступность типа передвижения')
    def check_type_is_not_disabled(self, locator):
        mode = self.find_element(locator)
        return "disabled" not in mode.get_attribute("class")

    @allure.step('Проверяем отображение кнопки Вызвать такси')
    def check_visibility_call_taxi_button(self):
        with check: assert self.wait_visibility_of_element(Mpg.CALL_TAXI_BUTTON)

    @allure.step('Проверяем отображение кнопки Забронировать')
    def check_visibility_rent_button(self):
        with check: assert self.wait_visibility_of_element(Mpg.RENT_BUTTON)

    @allure.step('Нажимаем кнопку Вызвать такси')
    def click_on_call_taxi_button(self):
        self.click_on_element(Mpg.CALL_TAXI_BUTTON)

    @allure.step('Проверяем отображение всех 6 тарифов')
    def check_visibility_six_taxi_tariffs(self):
        tariffs = [Mpg.TARIFF_WORKER, Mpg.TARIFF_SLEEPY, Mpg.TARIFF_VACATION, Mpg.TARIFF_TALKATIVE, Mpg.TARIFF_COMFORTING, Mpg.TARIFF_GLOSSY]
        for tariff in tariffs:
            with check:
                assert  self.wait_visibility_of_element(tariff)

    @allure.step('Проверяем что один из тарифов активен')
    def check_one_tariff_card_is_active(self):
        active_card = self.find_elements(Mpg.ACTIVE_TARIFF_CARD)
        with check: assert len(active_card) == 1

    @allure.step('Наводим курсор на тултип')
    def move_cursor_on_tariff_card_tooltip(self):
        element = self.find_element(Mpg.TARIFF_CARD_TOOLTIP)
        ActionChains(self.driver).move_to_element(element).perform()

    @allure.step('Проверяем что в форме заказа такси отображаются поля Телефон, Способ оплаты, Комментарий водителю, Требования к заказу')
    def check_order_taxi_form_fields(self):
        with check: assert self.wait_visibility_of_element(Mpg.FIELD_PHONE)
        with check: assert self.wait_visibility_of_element(Mpg.PAY_TYPE_BUTTON)
        with check: assert self.wait_visibility_of_element(Mpg.INPUT_COMMENT_FOR_DRIVER)
        with check: assert self.wait_visibility_of_element(Mpg.HEADER_ORDER_REQUIREMENTS)

    @allure.step('Выбираем тариф Рабочий')
    def click_on_tariff_worker(self):
        self.click_on_element(Mpg.TARIFF_WORKER)

    @allure.step('Нажимаем на Требования к заказу')
    def click_on_order_requirements(self):
        self.click_on_element(Mpg.HEADER_ORDER_REQUIREMENTS)

    @allure.step('Нажимаем на ползунок Столик для ноутбука')
    def click_on_switcher_laptop_table(self):
        self.click_on_element(Mpg.SWITCHER_LAPTOP_TABLE)

    @allure.step('Нажимаем кнопку Ввести номер и заказать')
    def click_on_order_taxi_button(self):
        self.click_on_element(Mpg.BUTTON_ORDER_TAXI)

    @allure.step('Проверяем что в окне ожидания машины отображаются Заголовок: Поиск машины, Таймер, кнопки Отменить и Детали')
    def check_waiting_car_window(self):
        with check: assert self.wait_visibility_of_element(Mpg.HEADER_SEARCH_CAR)
        with check: assert self.wait_visibility_of_element(Mpg.TIMER_SEARCH_CAR)
        with check: assert self.wait_visibility_of_element(Mpg.BUTTON_CANCEL)
        with check: assert self.wait_visibility_of_element(Mpg.BUTTON_DETAILS)

    @allure.step('Ожидаем завершения ожидания машины')
    def wait_invisibility_of_timer_search_car(self):
        self.wait_invisibility_of_element(Mpg.TIMER_SEARCH_CAR, 150)

    @allure.step('Проверка что в окне оформленного заказа отображаются: заголовок, номер и картинка автомобиля, Имя, рейтинг и фото водителя, кнопки Отменить и Детали')
    def check_completed_order_window(self):
        with check: assert self.wait_visibility_of_element(Mpg.HEADER_COMPLETED_ORDER)
        with check: assert self.wait_visibility_of_element(Mpg.CAR_IMAGE)
        with check: assert self.wait_visibility_of_element(Mpg.CAR_NUMBER)
        with check: assert self.wait_visibility_of_element(Mpg.DRIVER_PHOTO)
        with check: assert self.wait_visibility_of_element(Mpg.DRIVER_NAME)
        with check: assert self.wait_visibility_of_element(Mpg.DRIVER_RATING)
        with check: assert self.wait_visibility_of_element(Mpg.BUTTON_CANCEL)
        with check: assert self.wait_visibility_of_element(Mpg.BUTTON_DETAILS)

    @allure.step('Получаем цену из карточки активного тарифа')
    def get_active_tariff_price(self):
        price_in_text = self.get_element_text(Mpg.ACTIVE_TARIFF_PRICE)
        price = re.search(r'\d+', price_in_text).group()
        return price

    @allure.step('Получаем цену в блоке Детали')
    def get_tariff_details_price(self):
        price_in_text = self.get_element_text(Mpg.PRICE_IN_DETAILS_WINDOW)
        price = re.search(r'\d+', price_in_text).group()
        return price

    @allure.step('Нажимаем кнопку Детали')
    def click_on_order_details_button(self):
        self.click_on_element(Mpg.BUTTON_DETAILS)

    @allure.step('Нажимаем кнопку Отменить')
    def click_on_order_cancel_button(self):
        self.click_on_element(Mpg.BUTTON_CANCEL)

    @allure.step('Проверяем закрытие окна оформленного заказа')
    def check_invisibility_of_order_window(self):
        with check: assert self.wait_invisibility_of_element(Mpg.HEADER_COMPLETED_ORDER, 6)