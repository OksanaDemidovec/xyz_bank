from pythongirlpower.pages.transactions_page import TransactionsPage


def test_pagination_of_transaction_list(browser, config, transactions_instance):
    transactions = TransactionsPage(browser, config["url"]["transactions"])
    transactions.pagination_right_of_transaction_list(config["url"]["pagination_transactions"])
    transactions.pagination_left_of_transaction_list(config["url"]["top_transactions"])


def test_button_top_of_transaction_list(browser, config, transactions_instance):
    transactions = TransactionsPage(browser, config["url"]["transactions"])
    transactions.pagination_right_of_transaction_list(config["url"]["pagination_transactions"])
    transactions.button_top_of_transaction_list(config["url"]["top_transactions"])


def test_button_reset_transactions_page(browser, config, transactions_instance):
    transactions = TransactionsPage(browser, config["url"]["transactions"])
    transactions.button_reset()


def test_button_back_transactions_page(browser, config, transactions_instance):
    transactions = TransactionsPage(browser, config["url"]["transactions"])
    transactions.button_back(config["url"]["account"])
