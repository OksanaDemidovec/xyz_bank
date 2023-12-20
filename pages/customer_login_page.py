from .base_page import BasePage
from pythongirlpower.locators.locators import LoginCustomerLocators


class CustomerLoginPage(BasePage):
    def select_user_from_dropdown(self, username):
        user_option_locator = LoginCustomerLocators.USER_OPTION
        user_option_username = (
            user_option_locator[0],
            user_option_locator[1].format(username),
        )
        user_option = self.wait_for_visibility(user_option_username)
        user_option.click()
        self.logger.info("User is chosen")

    def click_submit_button(self, expected_url):
        submit_button = self.wait_for_clickable(
            LoginCustomerLocators.CUSTOMER_LOGIN_SUBMIT
        )
        submit_button.click()
        self.wait_for_url(expected_url)
        self.logger.info("User is logged in")
