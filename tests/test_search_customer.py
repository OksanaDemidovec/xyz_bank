import pytest
from pythongirlpower.pages.manager_page import ManagerPage
from pythongirlpower.pages.customers_tab_page import CustomersTabPage


@pytest.mark.parametrize("field", ["FirstName", "LastName", "PostCode", "AccountNumber"])
def test_search_customer_with_valid_data(browser, config, login_manager, field):
    manager_page = login_manager
    manager_page.click_customers_button(config["url"]["customers_tab"])
    customer_tab_page = CustomersTabPage(browser, config)
    customer_tab_page.clear_searching_field()
    customer = config["usernames"]["username2"]
    customer_tab_page.search_customer(config["info_about_customers"][customer][field])
    username = config["usernames"]["username2"]
    another_username = config["usernames"]["username1"]
    func_customer = customer_tab_page.find_customer_after_searching(username, another_username)
    config_customer = config["usernames"]["username2"]
    assert func_customer == config_customer


@pytest.mark.parametrize("field", ["FirstName", "LastName", "PostCode", "AccountNumber"])
@pytest.mark.xfail
def test_search_customer_with_invalid_data(browser, config, login_manager, field):
    manager_page = login_manager
    manager_page.click_customers_button(config["url"]["customers_tab"])
    manager_page = ManagerPage(browser, config)
    manager_page.click_customers_button(config["url"]["manager"])
    customer_tab_page = CustomersTabPage(browser, config)
    customer_tab_page.clear_searching_field()
    customer = config["usernames"]["username4"]
    customer_tab_page.search_customer(config["info_about_customers"][customer][field])
    username = config["usernames"]["username4"]
    another_username = config["usernames"]["username1"]
    func_customer = customer_tab_page.find_customer_after_searching(username, another_username)
    config_customer = config["usernames"]["username4"]
    assert func_customer == config_customer
