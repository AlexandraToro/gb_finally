import logging
import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def parse_locators(filename: str):
    ids = dict()
    with open(filename) as f:
        locators = yaml.safe_load(f)
    if "xpath" in locators.keys():
        for locator in locators["xpath"].keys():
            ids[locator] = (By.XPATH, locators["xpath"][locator])
    if "css" in locators.keys():
        for locator in locators["css"].keys():
            ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])
    return ids


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://test-stand.gb.ru"

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")
        except:
            logging.exception("Fiend element exception")
            element = None
        return element

    def get_element_property(self, mode, locator, property):
        element = self.find_element(mode, locator)
        if element:
            return element.value_of_css_property(property)
        else:
            logging.error(f'Property {property} not found element with locator {locator}')
            return None

    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception("Exception while open site")
            start_browsing = None
        return start_browsing

