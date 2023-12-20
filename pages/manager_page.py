from .base_page import BasePage
from pythongirlpower.locators.locators import ManagerPageLocators


class ManagerPage(BasePage):
    def click_add_customer_button(self, expected_url):
        add_customer_button = self.wait_for_clickable(
            ManagerPageLocators.ADD_CUSTOMER_TAB
        )
        add_customer_button.click()
        self.wait_for_url(expected_url)
        self.logger.info("Redirecting to the Add Customer page")

    def click_open_account_button(self, expected_url):
        open_account_button = self.wait_for_clickable(
            ManagerPageLocators.OPEN_ACCOUNT_TAB
        )
        open_account_button.click()
        self.wait_for_url(expected_url)
        self.logger.info("Redirecting to the Open Account page")

    def click_customers_button(self, expected_url):
        customers_button = self.wait_for_clickable(
            ManagerPageLocators.CUSTOMERS_TAB
        )
        customers_button.click()
        self.wait_for_url(expected_url)
        self.logger.info("Redirecting to the Customers page")
