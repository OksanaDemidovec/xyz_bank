from pythongirlpower.pages.login_page import LoginPage
from pythongirlpower.pages.customer_login_page import CustomerLoginPage
from pythongirlpower.pages.account_page import AccountPage
from pythongirlpower.pages.deposit_withdrawl_page import DepositPage, WithdrawlPage
import time


def test_valid_deposit(browser, config):
    login_page = LoginPage(browser, config["url"]["login"])
    login_page.open()
    login_page.click_user_login_button(config["url"]["customer"])
    customer_login_page = CustomerLoginPage(browser, browser.current_url)
    customer_login_page.select_user_from_dropdown(
        config["usernames"]["username1"]
        )
    customer_login_page.click_submit_button(config["url"]["account"])
    account_page = AccountPage(browser, browser.current_url)
    account_page.check_ui()
    start_balance = account_page.start_balance()
    account_page.click_deposit_button(config["url"]["account"])
    deposit_page = DepositPage(browser, browser.current_url)
    deposit_page.check_ui_deposit()
    random_number = deposit_page.enter_valid_deposit()
    deposit_page.click_deposit_button(config["url"]["account"])
    deposit_page.check_successful_message()
    new_balance = str(int(start_balance) + random_number)
    account_page.check_balance(new_balance)


def test_invalid_deposit(browser, config):
    account_page = AccountPage(browser, browser.current_url)
    start_balance = account_page.start_balance()
    account_page.click_deposit_button(config["url"]["account"])

    deposit_page = DepositPage(browser, browser.current_url)
    deposit_page.check_ui_deposit()
    deposit_page.click_deposit_button(config["url"]["account"])
    account_page.check_balance(start_balance)
    deposit_page.enter_invalid_deposit(config["deposit"]["null"])
    deposit_page.click_deposit_button(config["url"]["account"])
    deposit_page.check_no_successful_message()
    account_page.check_balance(start_balance)
    deposit_page.enter_invalid_deposit(config["deposit"]["zero"])
    deposit_page.click_deposit_button(config["url"]["account"])
    deposit_page.check_no_successful_message()
    account_page.check_balance(start_balance)


def test_valid_withgrawl(browser, config):
    account_page = AccountPage(browser, browser.current_url)
    account_page.check_ui()
    start_balance = account_page.start_balance()
    account_page.click_withdrawl_button(config["url"]["account"])
    withdrawl_page = WithdrawlPage(browser, browser.current_url)
    withdrawl_page.check_ui_withdrawl()
    time.sleep(1)
    random_number = withdrawl_page.enter_valid_withdrawl()
    withdrawl_page.click_withdrawl_button(config["url"]["account"])
    withdrawl_page.check_w_successful_message()
    new_balance = str(int(start_balance) - random_number)
    account_page.check_balance(new_balance)


def test_invalid_withgrawl(browser, config):
    account_page = AccountPage(browser, browser.current_url)
    account_page.click_withdrawl_button(config["url"]["account"])
    start_balance = account_page.start_balance()
    withdrawl_page = WithdrawlPage(browser, browser.current_url)
    withdrawl_page.check_ui_withdrawl()
    withdrawl_page.enter_invalid_withdrawl(config["withdrawl"]["less_than_0"])
    withdrawl_page.click_withdrawl_button(config["url"]["account"])
    account_page.check_balance(start_balance)
    time.sleep(1)
    withdrawl_page.check_no_w_successful_message()
    withdrawl_page.enter_invalid_withdrawl(config["withdrawl"]["null"])
    withdrawl_page.click_withdrawl_button(config["url"]["account"])
    account_page.check_balance(start_balance)
    withdrawl_page.enter_invalid_withdrawl(config["withdrawl"]["zero"])
    withdrawl_page.click_withdrawl_button(config["url"]["account"])
    account_page.check_balance(start_balance)


def test_withdrawl_more_than_balance(browser, config):
    account_page = AccountPage(browser, browser.current_url)
    start_balance = account_page.start_balance()
    account_page.click_withdrawl_button(config["url"]["account"])
    withdrawl_page = WithdrawlPage(browser, browser.current_url)
    withdrawl_page.check_ui_withdrawl()
    invalid_withdrawl = int(start_balance) + 1
    withdrawl_page.enter_invalid_withdrawl(invalid_withdrawl)
    withdrawl_page.click_withdrawl_button(config["url"]["account"])
    withdrawl_page.check_fail_message()
    account_page.check_balance(start_balance)


def test_account_selector(browser, config):
    account_page = AccountPage(browser, browser.current_url)
    start_balance = account_page.start_balance()
    account_page.click_account_selector2(config["url"]["account"])
    account_page.check_balance_in_different_account(start_balance)
    account_page.click_account_selector1(config["url"]["account"])


def test_balance_after_loguot(browser, config):
    account_page = AccountPage(browser, browser.current_url)
    start_balance = account_page.start_balance()
    account_page.click_logout_button(config["url"]["customer"])
    login_page = LoginPage(browser, config["url"]["login"])
    login_page.open()
    login_page.click_user_login_button(config["url"]["customer"])
    customer_login_page = CustomerLoginPage(browser, browser.current_url)
    customer_login_page.select_user_from_dropdown(
        config["usernames"]["username1"]
    )
    customer_login_page.click_submit_button(config["url"]["account"])
    account_page.check_balance(start_balance)
