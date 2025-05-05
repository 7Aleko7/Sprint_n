from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_elements(self, locator):
        element = self.driver.find_elements(*locator)
        return element

    def find_element(self, locator):
        element = self.driver.find_element(*locator)
        return element

    def click_on_element(self, locator):
        self.wait_visibility_of_element(locator)
        self.driver.find_element(*locator).click()

    def send_keys_to_input(self, locator, keys):
        self.wait_visibility_of_element(locator)
        self.driver.find_element(*locator).send_keys(keys)

    def get_element_text(self, locator):
        self.wait_visibility_of_element(locator)
        element_text = self.driver.find_element(*locator).text
        return element_text

    def wait_visibility_of_element(self, locator):
        try:
            return WebDriverWait(self.driver, 6).until(
                expected_conditions.visibility_of_element_located(locator)
            )
        except TimeoutException:
            return False

    def wait_invisibility_of_element(self, locator, time_out):
        try:
            return WebDriverWait(self.driver, time_out).until(expected_conditions.invisibility_of_element_located(locator))
        except TimeoutException:
            return False

    def find_element_on_page_by_text(self, find_text):
        element = self.driver.find_element(By.XPATH, f"//*[text()='{find_text}']")
        return element