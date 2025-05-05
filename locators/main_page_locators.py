from selenium.webdriver.common.by import By

class MainPageLocators:

    # Инпут Откуда
    INPUT_FROM= By.CSS_SELECTOR, "input#from"

    # Инпут Куда
    INPUT_TO = By.CSS_SELECTOR, "input#to"

    # Точка маршрута Откуда
    FROM_POINT = (By.XPATH, "//*[contains(@class, 'route-pin__label-0')]")

    # Точка маршрута Куда
    TO_POINT = (By.XPATH, "//*[contains(@class, 'route-pin__label-1')]")

    # Блок с выбором маршрута(отображается)
    VISIBILITY_ROUTE_OPTIONS_BLOCK = By.CSS_SELECTOR, ".type-picker.shown"

    # Текст Авто Бесплатно
    FREE_CAR = By.XPATH, ".//div[text()='Авто Бесплатно']"

    # Текст В пути 0 мин
    ZERO_MINUTES_ROUTE = By.XPATH, ".//div[text()='В пути 0 мин.']"

    # Время в пути
    ROUTE_TIME = By.XPATH, "//div[@class = 'results-text']/div[@class='duration']"

    # Стоимость маршрута
    ROUTE_COST = By.XPATH, "//div[@class = 'results-text']/div[@class='text']"

    # Вид - Оптимальный
    MODE_OPTIMAL = By.XPATH, ".//div[text()='Оптимальный']"

    # Вид - Свой
    MODE_MINE = By.XPATH, ".//div[text()='Свой']"

    # Вид - Быстрый
    MODE_FAST = By.XPATH, ".//div[text()='Быстрый']"

    # Тип - Авто
    TYPE_CAR = By.XPATH, "//img[contains(@src, 'car')]/parent::div"

    # Тип - Пешком
    TYPE_WALK = By.XPATH, "//img[contains(@src, 'walk')]/parent::div"

    # Тип - Такси
    TYPE_TAXI = By.XPATH, "//img[contains(@src, 'taxi')]/parent::div"

    # Тип - Велосипед
    TYPE_BIKE = By.XPATH, "//img[contains(@src, 'bike')]/parent::div"

    # Тип - Самокат
    TYPE_SCOOTER = By.XPATH, "//img[contains(@src, 'scooter')]/parent::div"

    # Тип - Драйв
    TYPE_DRIVE = By.XPATH, "//img[contains(@src, 'drive')]/parent::div"

    # Кнопка Вызвать такси
    CALL_TAXI_BUTTON = By.XPATH, ".//button[text()='Вызвать такси']"

    # Кнопка Забронировать
    RENT_BUTTON = By.XPATH, ".//button[text()='Забронировать']"

    # Тариф Рабочий
    TARIFF_WORKER = By.XPATH, ".//div[text()='Рабочий']/parent::div"

    # Тариф Сонный
    TARIFF_SLEEPY = By.XPATH, ".//div[text()='Сонный']/parent::div"

    # Тариф Отпускной
    TARIFF_VACATION = By.XPATH, ".//div[text()='Отпускной']/parent::div"

    # Тариф Разговорчивый
    TARIFF_TALKATIVE = By.XPATH, ".//div[text()='Разговорчивый']/parent::div"

    # Тариф Утешительный
    TARIFF_COMFORTING = By.XPATH, ".//div[text()='Утешительный']/parent::div"

    # Тариф Глянцевый
    TARIFF_GLOSSY = By.XPATH, ".//div[text()='Глянцевый']/parent::div"

    # Активная карточка тарифа
    ACTIVE_TARIFF_CARD = By.CSS_SELECTOR, ".tcard.active"

    # Тултип в активной карточке тарифа
    TARIFF_CARD_TOOLTIP = By.CSS_SELECTOR, ".tcard.active > button[customclass='tcard-i']"

    # Поле Телефон
    FIELD_PHONE = By.XPATH, ".//div[text()='Телефон']"

    # Кнопка Способ оплаты
    PAY_TYPE_BUTTON = By.XPATH, ".//div[@class='pp-text' and text()='Способ оплаты']"

    # Инпут Комментарий водителю
    INPUT_COMMENT_FOR_DRIVER = By.XPATH, ".//label[text()='Комментарий водителю...']"

    # Заголовок Требования к заказу
    HEADER_ORDER_REQUIREMENTS = By.XPATH, ".//div[text()='Требования к заказу']"

    # Ползунок Столик для ноутбука
    SWITCHER_LAPTOP_TABLE = By.XPATH, "//div[contains(@class, 'r-sw-label') and text()='Столик для ноутбука']/following-sibling::div//span"

    # Кнопка Ввести номер и заказать
    BUTTON_ORDER_TAXI = By.XPATH, ".//span[text()='Ввести номер и заказать']"

    # Заголовок Поиск машины
    HEADER_SEARCH_CAR = By.XPATH, ".//div[text()='Поиск машины']"

    # Таймер ожидания машины
    TIMER_SEARCH_CAR = By.CLASS_NAME, "order-header-time"

    # Кнопка Отменить
    BUTTON_CANCEL = By.XPATH, "//img[@alt='close']/parent::button"

    # Кнопка Детали
    BUTTON_DETAILS = By.XPATH, "//img[@alt='burger']/parent::button"

    # Заголовок N мин. и приедет
    HEADER_COMPLETED_ORDER = By.XPATH, "//div[contains(@class, 'order-header-title')][contains(normalize-space(), 'мин. и приедет')]"

    # Изображение Машины
    CAR_IMAGE = By.XPATH, "//img[@alt='Car']"

    # Номер машины(не пустой)
    CAR_NUMBER = By.XPATH, "//div[@class='number' and text() and normalize-space(text()) != '']"

    # Фото водителя
    DRIVER_PHOTO = By.XPATH, "//img[@alt='close']/parent::div"

    # Имя водителя
    DRIVER_NAME = By.XPATH, "//div[contains(@class, 'order-btn-rating')]/parent::div/following-sibling::div[text() and normalize-space(text()) != '']"

    # Рейтинг водителя
    DRIVER_RATING = By.XPATH, "//div[@class='order-btn-rating' and text() and normalize-space(text()) != '']"

    # Стоимость активного тарифа
    ACTIVE_TARIFF_PRICE = By.XPATH, "//div[contains(@class, 'tcard active')]//div[contains(@class, 'tcard-price')]"

    # Стоимость в блоке Детали
    PRICE_IN_DETAILS_WINDOW = By.XPATH, "//div[contains(text(), 'Стоимость')]"