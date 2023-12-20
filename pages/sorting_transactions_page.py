from datetime import datetime
from selenium.webdriver.common.by import By
from .base_page import BasePage
from pythongirlpower.locators.locators_transactions import SortingPage as SPLocators


class SortingTransactionsPage(BasePage):
    def sorting_transactions_by_date(self, expected_url):
        transactions_button = self.wait_for_clickable(SPLocators.SORTING_DATE)
        transactions_button.click()
        self.wait_for_url(expected_url)

        self.wait_for_visibility(SPLocators.UPDATE_LIST_TRANSACTIONS)

        transaction_dates = self.driver.find_elements(By.XPATH, "//tr/td[1]")

        prev_date = None
        for date_element in transaction_dates:
            current_date = date_element.text
            if prev_date is not None:
                if datetime.strptime(current_date, "%B %d, %Y") <= datetime.strptime(prev_date, "%B %d, %Y"):
                    return True
                else:
                    return "Transactions are not sorted by date ascending"
        self.logger.info("Transactions sorted by date ascending")

    def sorting_transactions_by_amount(self):
        transactions_button = self.wait_for_clickable(SPLocators.SORTING_AMOUNT)
        transactions_button.click()

        self.wait_for_visibility(SPLocators.UPDATE_LIST_TRANSACTIONS)

        transaction_amount = self.driver.find_elements(By.XPATH, "//tr/td[2]")

        prev_amount = None
        for amount_element in transaction_amount:
            current_amount = amount_element.text
            if prev_amount is not None:
                assert current_amount >= prev_amount, "Transactions are not sorted by amount ascending"
            prev_amount = current_amount

        self.logger.info("Transactions sorted by amount ascending")

    def sorting_transactions_by_type(self):
        transactions_button = self.wait_for_clickable(SPLocators.SORTING_TYPE)
        transactions_button.click()

        self.wait_for_visibility(SPLocators.UPDATE_LIST_TRANSACTIONS)

        first_cell_type = self.wait_for_visibility(SPLocators.FIRST_CELL_TYPE)
        second_cell_type = self.wait_for_visibility(SPLocators.SECOND_CELL_TYPE)

        if first_cell_type.text == second_cell_type.text:
            self.logger.info("Transactions sorted by type ascending")
            return True
        else:
            raise ValueError("Transactions are not sorted by type ascending")
