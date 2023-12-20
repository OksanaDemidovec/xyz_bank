import pytest
from pythongirlpower.pages.transactions_page import TransactionsPage
from pythongirlpower.pages.calendar_transactions_page import CalendarTransactionsPage


def test_calendar_transactions(browser, config, login_customer):
    login_customer("username3")
    transactions = TransactionsPage(browser, config["url"]["account"])
    transactions.open_transactions_page(config["url"]["transactions"])
    calendar = CalendarTransactionsPage(browser, config["url"]["transactions"])
    calendar.calendar_transactions_page()


@pytest.mark.xfail
def test_input_start_date(browser, config, login_customer):
    login_customer("username3")
    transactions = TransactionsPage(browser, config["url"]["account"])
    transactions.open_transactions_page(config["url"]["transactions"])
    input_start_date = CalendarTransactionsPage(browser, config["url"]["transactions"])
    input_start_date.input_start_date_calendar()


@pytest.mark.xfail
def test_input_end_date(browser, config, login_customer):
    login_customer("username3")
    transactions = TransactionsPage(browser, config["url"]["account"])
    transactions.open_transactions_page(config["url"]["transactions"])
    input_end_date = CalendarTransactionsPage(browser, config["url"]["transactions"])
    input_end_date.input_end_date_calendar()
