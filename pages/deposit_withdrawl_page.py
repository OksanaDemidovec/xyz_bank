from .base_page import BasePage
from pythongirlpower.locators.locators import DepositPageLocators, WithdrawlPageLocators
from selenium.common.exceptions import NoSuchElementException


class DepositPage(BasePage):
    def check_ui_deposit(self):
        assert self.wait_for_visibility(DepositPageLocators.AMOUNT_INPUT)
        assert self.wait_for_visibility(DepositPageLocators.DEPOSIT_BUTTON)
        self.logger.info("UI is correct")

    def click_deposit_button(self, expected_url):
        deposit_button = self.wait_for_clickable(
            DepositPageLocators.DEPOSIT_BUTTON
        )
        deposit_button.click()
        self.wait_for_url(expected_url)
        self.logger.info("Deposit button is active")
        assert self.wait_for_visibility(DepositPageLocators.MESSAGE)

    def enter_valid_deposit(self):
        amount_input = self.wait_for_clickable(
            DepositPageLocators.AMOUNT_INPUT
        )
        random_number = self.random_more_than_100()
        amount_input.send_keys(random_number)
        self.logger.info("Valid deposit is added")
        return random_number

    def enter_invalid_deposit(self, amount):
        amount_input = self.wait_for_clickable(
            DepositPageLocators.AMOUNT_INPUT
        )
        amount_input.click()
        amount_input.clear()
        amount_input.send_keys(amount)
        self.logger.info("Invalid deposit is added")
        return amount

    def check_successful_message(self):
        assert self.wait_for_visibility(DepositPageLocators.SUCCESSFUL_MESSAGE)
        self.logger.info("Successful message appears")

    def check_no_successful_message(self):
        try:
            self.wait_for_visibility(DepositPageLocators.SUCCESSFUL_MESSAGE)
            assert True
        except NoSuchElementException:
            assert False
        self.logger.info("Successful message doesn't appear")


class WithdrawlPage(BasePage):
    def check_ui_withdrawl(self):
        assert self.wait_for_visibility(WithdrawlPageLocators.AMOUNT_INPUT)
        assert self.wait_for_visibility(WithdrawlPageLocators.WITHDRAWL_BUTTON)
        self.logger.info("UI is correct")

    def click_withdrawl_button(self, expected_url):
        withdrawl_button = self.wait_for_clickable(
            WithdrawlPageLocators.WITHDRAWL_BUTTON
        )
        withdrawl_button.click()
        self.wait_for_url(expected_url)
        self.logger.info("Withdrawl button is active")

    def enter_valid_withdrawl(self):
        amount_input = self.wait_for_clickable(
            WithdrawlPageLocators.AMOUNT_INPUT
        )
        random_number = self.random_less_than_100()
        amount_input.send_keys(random_number)
        self.logger.info("Valid deposit is added")
        return random_number

    def enter_invalid_withdrawl(self, amount):
        amount_input = self.wait_for_clickable(
            WithdrawlPageLocators.AMOUNT_INPUT
        )
        amount_input.click()
        amount_input.clear()
        amount_input.send_keys(amount)
        self.logger.info("Invalid withdrawl is added")
        return amount

    def check_w_successful_message(self):
        assert self.wait_for_visibility(WithdrawlPageLocators.SUCCESSFUL_MESSAGE)
        self.logger.info("Successful message appears")

    def check_no_w_successful_message(self):
        try:
            self.wait_for_visibility(WithdrawlPageLocators.SUCCESSFUL_MESSAGE)
            assert True
        except NoSuchElementException:
            assert False
        self.logger.info("Successful message doesn't appear")

    def check_fail_message(self):
        assert self.wait_for_visibility(WithdrawlPageLocators.FAIL_MESSAGE)
        self.logger.info("Fail message appears")
