import time
from selenium import webdriver
import pytest
from os import path
import json
import logging
from pythongirlpower.locators.locators import AccountPageLocators
from pythongirlpower.pages.login_page import LoginPage
from pythongirlpower.pages.manager_page import ManagerPage
from pythongirlpower.pages.customer_login_page import CustomerLoginPage
from pythongirlpower.pages.transactions_page import TransactionsPage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')

    browser = webdriver.Chrome(options=chrome_options)
    logger.info("Browser is opened")
    yield browser
    browser.quit()
    logger.info("Browser closed")


@pytest.fixture(name="config")
def read_config_file():
    file_path = path.join("test_data", "test_data.json")
    with open(file_path, "r") as f:
        data = json.load(f)
    return data


@pytest.fixture
def balance_amount(self):
    balance = self.wait_for_visibility(AccountPageLocators.BALANCE)
    amount = balance.text
    print(amount)
    return amount


@pytest.fixture
def login_manager(browser, config):
    login_page = LoginPage(browser, config["url"]["login"])
    login_page.open()
    login_page.click_manager_login_button(config["url"]["manager"])
    manager_page = ManagerPage(browser, browser.current_url)
    yield manager_page


@pytest.fixture
def login_customer(browser, config):
    def login(username):
        login_page = LoginPage(browser, config["url"]["login"])
        login_page.open()
        login_page.click_user_login_button(config["url"]["customer"])
        customer_login_page = CustomerLoginPage(browser, browser.current_url)
        customer_login_page.select_user_from_dropdown(config["usernames"][username])
        logged = customer_login_page.click_submit_button(config["url"]["account"])
        return logged

    yield login


@pytest.fixture
def transactions_instance(browser, config, login_customer):
    login_customer("username1")
    transactions = TransactionsPage(browser, config["url"]["account"])
    transactions.deposit()
    transactions.withdrawl()
    transactions.deposit()
    transactions.withdrawl()
    transactions.deposit()
    transactions.withdrawl()
    transactions.deposit()
    transactions.withdrawl()
    time.sleep(2)
    transactions.open_transactions_page(config["url"]["transactions"])
    return transactions
