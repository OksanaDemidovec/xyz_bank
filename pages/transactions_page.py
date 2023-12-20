import time
from .base_page import BasePage
from pythongirlpower.locators.locators_transactions import TransactionsPage as TPLocators
from pythongirlpower.locators.locators_transactions import WithdrawlDepositPage as WDLocators


class TransactionsPage(BasePage):
    def open_transactions_page(self, expected_url):
        transactions_button = self.wait_for_clickable(TPLocators.TRANSACTIONS_BUTTON)
        transactions_button.click()
        self.wait_for_url(expected_url)
        self.logger.info("Redirecting to the Transactions page")

    def pagination_right_of_transaction_list(self, expected_url):
        pagination_button = self.wait_for_clickable(TPLocators.PAGINATION_BUTTON_R)
        pagination_button.click()
        self.wait_for_url(expected_url)
        self.logger.info("The transaction list pagination buttons work correctly")

    def pagination_left_of_transaction_list(self, expected_url):
        pagination_button = self.wait_for_clickable(TPLocators.PAGINATION_BUTTON_L)
        pagination_button.click()
        self.wait_for_url(expected_url)
        self.logger.info("The transaction list pagination buttons work correctly")

    def button_top_of_transaction_list(self, expected_url):
        top_button = self.wait_for_clickable(TPLocators.TOP_BUTTON)
        top_button.click()
        self.wait_for_url(expected_url)
        self.logger.info("The “Top” button in the transaction list works correctly")

    def button_back(self, expected_url):
        button_back = self.wait_for_clickable(TPLocators.BACK_BUTTON)
        button_back.click()
        self.wait_for_url(expected_url)
        self.logger.info("Redirecting to the Customer page")

    def button_reset(self):
        button_reset = self.wait_for_clickable(TPLocators.RESET_BUTTON)
        button_reset.click()
        first_cell = self.wait_for_invisibility(TPLocators.FIRST_CELL_TRANSACTIONS)
        if first_cell:
            self.logger.info("The transaction list has become clear")
        else:
            print("The transactions list did not become clear")

    def deposit(self):
        deposit_button_1 = self.wait_for_clickable(WDLocators.DEPOSIT_BUTTON_1)
        deposit_button_1.click()
        amount_input = self.wait_for_clickable(WDLocators.AMOUNT_INPUT)
        amount_input.send_keys(100)
        deposit_button_2 = self.wait_for_clickable(WDLocators.DEPOSIT_BUTTON_2)
        deposit_button_2.click()
        assert self.wait_for_visibility(WDLocators.SUCCESSFUL_MESSAGE_D)
        self.logger.info("Deposit is added")

    def withdrawl(self):
        withdrawl_button_1 = self.wait_for_clickable(WDLocators.WITHDRAWL_BUTTON_1)
        withdrawl_button_1.click()
        time.sleep(1)
        amount_input = self.wait_for_clickable(WDLocators.AMOUNT_INPUT)
        amount_input.send_keys(20)
        withdrawl_button_2 = self.wait_for_clickable(WDLocators.WITHDRAWL_BUTTON_2)
        withdrawl_button_2.click()
        assert self.wait_for_visibility(WDLocators.SUCCESSFUL_MESSAGE_W)
        self.logger.info("Withdrawl is added")
