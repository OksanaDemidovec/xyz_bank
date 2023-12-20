import pytest
from pythongirlpower.pages.open_account_page import OpenAccountPage


@pytest.mark.parametrize("currency", ["currency1", "currency2", "currency3"])
def test_open_account(browser, config, login_manager, currency):
    manager_page = login_manager
    manager_page.click_open_account_button(config["url"]["open_account"])
    open_account_page = OpenAccountPage(browser, config["url"]["open_account"])
    open_account_page.select_customer_from_dropdown(config["usernames"]["username2"])
    open_account_page.select_currency_from_dropdown(config["currency"][currency])
    func_result = open_account_page.click_process_button()
    assert "Account created successfully with account Number" in func_result, "Account creation failed"
