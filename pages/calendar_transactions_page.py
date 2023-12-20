from .base_page import BasePage
from pythongirlpower.locators.locators_transactions import TransactionsPage as TPLocators


class CalendarTransactionsPage(BasePage):
    def calendar_transactions_page(self):
        calendar_start = self.wait_for_clickable(TPLocators.CALENDAR_START)
        calendar_start.click()
        calendar_end = self.wait_for_clickable(TPLocators.CALENDAR_END)
        calendar_end.click()

        if calendar_start.is_displayed() and calendar_start.is_enabled():
            self.logger.info("The calendar start date is active and visible")
        else:
            print("The calendar start date is not active and visible")

        if calendar_end.is_displayed() and calendar_end.is_enabled():
            self.logger.info("The calendar end date is active and visible")
        else:
            print("The calendar end date is not active and visible")

    def input_start_date_calendar(self):
        calendar_start = self.wait_for_clickable(TPLocators.CALENDAR_START)
        calendar_start.click()
        calendar_start.clear()
        calendar_start.send_keys("05-12-2023-00-00")
        if calendar_start.get_attribute("value") == "2023-10-05T00:00":
            self.logger.info("Start date was set correctly")
        else:
            raise AssertionError("Start date was not set correctly")

    def input_end_date_calendar(self):
        calendar_end = self.wait_for_clickable(TPLocators.CALENDAR_END)
        calendar_end.click()
        calendar_end.clear()
        calendar_end.send_keys("12-10-2023-00-00")
        if calendar_end.get_attribute("value") == "2023-10-12T00:00":
            self.logger.info("End date was set correctly")
        else:
            raise AssertionError("End date was not set correctly")
