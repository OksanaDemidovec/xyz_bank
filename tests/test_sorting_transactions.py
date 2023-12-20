import pytest
from pythongirlpower.pages.sorting_transactions_page import SortingTransactionsPage


def test_transactions_by_date(browser, config, transactions_instance):
    sorting_transactions = SortingTransactionsPage(browser, config["url"]["transactions"])
    sorting_transactions.sorting_transactions_by_date(config["url"]["sorting_transactions"])


@pytest.mark.xfail
def test_transactions_by_amount(browser, config, transactions_instance):
    sorting_transactions = SortingTransactionsPage(browser, config["url"]["transactions"])
    sorting_transactions.sorting_transactions_by_amount()


@pytest.mark.xfail
def test_transactions_by_type(browser, config, transactions_instance):
    sorting_transactions = SortingTransactionsPage(browser, config["url"]["transactions"])
    sorting_transactions.sorting_transactions_by_type()
