from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selenium.common import NoSuchElementException

from .page import Page


class LoginPage(Page):

    def click_auth_button(self):
        print("SELF", self.__dict__)
        auth_element = self.find_element(AppiumBy.ID, "com.ajaxsystems:id/authHelloLogin")
        return self.click_element(auth_element)

    def enter_username(self, username):
        username_selector = (MobileBy.ID, "com.ajaxsystems:id/authLoginEmail")

        username_element = self.find_element(username_selector)
        username_element.clear()
        username_element.send_keys(username)

    def enter_password(self, password):
        password_selector = (MobileBy.ID, "com.ajaxsystems:id/authLoginPassword")

        password_element = self.find_element(password_selector)
        password_element.clear()
        password_element.send_keys(password)

    def click_login_button(self):
        login_button_selector = (MobileBy.ID, "com.ajaxsystems:id/authLogin")
        self.find_element(login_button_selector).click()

    def is_element_present(self, element_id):
        try:
            self.driver.find_element(MobileBy.ID, element_id)
            return True
        except NoSuchElementException:
            return False
