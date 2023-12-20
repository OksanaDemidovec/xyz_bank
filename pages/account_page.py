from .base_page import BasePage
from pythongirlpower.locators.locators import AccountPageLocators


class AccountPage(BasePage):
    def get_welcome_message(self, username):
        welcome_msg_locator = AccountPageLocators.WELCOME_MESSAGE
        formatted_locator = (
            welcome_msg_locator[0],
            welcome_msg_locator[1].format(username),
        )
        welcome_message = self.wait_for_visibility(formatted_locator).text
        self.logger.info(welcome_message)
        return welcome_message

    def click_logout_button(self, expected_url):
        logout_button = self.wait_for_clickable(
            AccountPageLocators.LOGOUT_BUTTON
        )
        logout_button.click()
        self.wait_for_url(expected_url)
        self.logger.info("User is logged out")

    def check_ui(self):
        assert self.wait_for_visibility(AccountPageLocators.TRANSACTIONS_BUTTON)
        assert self.wait_for_visibility(AccountPageLocators.DEPOSIT_BUTTON)
        assert self.wait_for_visibility(AccountPageLocators.WITHDRAWL_BUTTON)
        assert self.wait_for_visibility(AccountPageLocators.ACCOUNT_SELECTOR)
        assert self.wait_for_visibility(AccountPageLocators.ACCOUNT_NUMBER)
        assert self.wait_for_visibility(AccountPageLocators.BALANCE)
        assert self.wait_for_visibility(AccountPageLocators.CURRENCY)
        self.logger.info("UI is correct")

    def click_deposit_button(self, expected_url):
        deposit_button = self.wait_for_clickable(
            AccountPageLocators.DEPOSIT_BUTTON
        )
        deposit_button.click()
        self.wait_for_url(expected_url)
        self.logger.info("Deposit button is active")

    def click_withdrawl_button(self, expected_url):
        withdrawl_button = self.wait_for_clickable(
            AccountPageLocators.WITHDRAWL_BUTTON
        )
        withdrawl_button.click()
        self.wait_for_url(expected_url)
        self.logger.info("Withdrawl button is active")

    def click_transactions_button(self, expected_url):
        transactions_button = self.wait_for_clickable(
            AccountPageLocators.TRANSACTIONS_BUTTON
        )
        transactions_button.click()
        self.wait_for_url(expected_url)
        self.logger.info("Transactions button is active")

    def click_account_selector2(self, expected_url):
        account_selector = self.wait_for_clickable(
            AccountPageLocators.ACCOUNT_SELECTOR
        )
        account_selector.click()
        selector2 = self.wait_for_clickable(
            AccountPageLocators.SELECTOR_2)
        selector2.click()
        self.wait_for_url(expected_url)
        self.logger.info("Account selector is opened")

    def click_account_selector1(self, expected_url):
        account_selector = self.wait_for_clickable(
            AccountPageLocators.ACCOUNT_SELECTOR
        )
        account_selector.click()
        selector1 = self.wait_for_clickable(
            AccountPageLocators.SELECTOR_1)
        selector1.click()
        self.wait_for_url(expected_url)
        self.logger.info("Account selector is opened")

    def start_balance(self):
        balance = self.wait_for_visibility(AccountPageLocators.BALANCE)
        amount = balance.text
        return amount

    def check_balance(self, balance_amount):
        updated_balance = self.wait_for_visibility(AccountPageLocators.BALANCE)
        updated_amount = updated_balance.text
        assert balance_amount == updated_amount
        self.logger.info("Balance is correct")

    def check_balance_in_different_account(self, balance_amount):
        updated_balance = self.wait_for_visibility(AccountPageLocators.BALANCE)
        updated_amount = updated_balance.text
        assert balance_amount != updated_amount
        self.logger.info("Balance isn't equal")
