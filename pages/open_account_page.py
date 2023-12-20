from .base_page import BasePage
from pythongirlpower.locators.locators import OpenAccountLocators


class OpenAccountPage(BasePage):
    def select_customer_from_dropdown(self, username):
        user_option_locator = OpenAccountLocators.USER_OPTION_ACCOUNT
        user_option_username = (user_option_locator[0], user_option_locator[1].format(username))
        user_option = self.wait_for_visibility(user_option_username)
        user_option.click()
        self.logger.info(f"The user {username} is chosen")

    def select_currency_from_dropdown(self, currency):
        currency_option_locator = OpenAccountLocators.CURRENCY_OPTION
        currency_option = (currency_option_locator[0], currency_option_locator[1].format(currency))
        currency_option = self.wait_for_visibility(currency_option)
        currency_option.click()
        self.logger.info(f"The currency {currency} is chosen")

    def click_process_button(self):
        process_button = self.wait_for_clickable(OpenAccountLocators.PROCESS_BUTTON)
        process_button.click()
        alert = self.wait_for_alert()
        alert_text = alert.text
        self.logger.info("Alert is received")
        self.logger.info(alert_text)
        alert.accept()
        self.logger.info("Alert is accepted")
        return alert_text
