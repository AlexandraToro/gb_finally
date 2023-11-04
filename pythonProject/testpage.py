from BaseApp import BasePage
from BaseApp import parse_locators
import logging


ids = parse_locators("./locators.yaml")


class OperationHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Send {word} to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exception while operation with {locator}')
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f'Clicked {element_name} button')
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get test from {element_name}')
            return None
        logging.debug(f'We find text {text} in field {element_name}')
        return text

    def enter_login(self, word):
        self.enter_text_into_field(ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(ids["LOCATOR_PASS_FILED"], word, description="Password form")

    def click_login_button(self):
        self.click_button(ids["LOCATOR_LOGIN_BTN"], description="login")

    def get_error_text(self):
        return self.get_text_from_element(ids["LOCATOR_ERROR_FILED"])

    def auth(self):
        return self.get_text_from_element(ids["LOCATOR_AUTH"])

    def click_about_btn(self):
        self.click_button(ids["LOCATOR_ABOUT_BTN"])

    def check_title_about(self):
        return self.get_text_from_element(ids["LOCATOR_TITLE_ABOUT"])

    def font_size_title(self):
        return self.find_element(ids["LOCATOR_FONT_TITLE"]).value_of_css_property("font-size")
