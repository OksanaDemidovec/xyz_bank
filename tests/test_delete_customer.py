from pythongirlpower.pages.customers_tab_page import CustomersTabPage


def test_delete_customer(browser, config, login_manager):
    manager_page = login_manager
    manager_page.click_customers_button(config["url"]["customers_tab"])
    customers_page = CustomersTabPage(browser, config["url"]["login"])
    customers_page.delete_customer(config["usernames"]["username5"])
    customers_page.search_deleted_customer(config["usernames"]["username5"])
    current_url = browser.current_url
    assert current_url == config["url"]["customers_tab"]
