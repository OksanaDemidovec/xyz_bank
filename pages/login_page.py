from .base_page import BasePage
from pythongirlpower.locators.locators import LoginPageLocators


class LoginPage(BasePage):
    def click_user_login_button(self, expected_url):
        user_login_button = self.wait_for_clickable(
            LoginPageLocators.USER_LOGIN_BUTTON
        )
        user_login_button.click()
        self.wait_for_url(expected_url)
        self.logger.info("Redirecting to the Login Customer page")

    def click_manager_login_button(self, expected_url):
        manager_login_button = self.wait_for_clickable(
            LoginPageLocators.MANAGER_LOGIN_BUTTON
        )
        manager_login_button.click()
        self.wait_for_url(expected_url)
        self.logger.info("Manager is logged in")
