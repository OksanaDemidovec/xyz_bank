from pythongirlpower.pages.add_customer_page import AddCustomerPage
import pytest


def test_add_customer(browser, config, login_manager):
    manager_page = login_manager
    manager_page.click_add_customer_button(config["url"]["addcustomer"])
    add_customer_page = AddCustomerPage(browser, browser.current_url)
    add_customer_page.create_fake_user()
    add_customer_page.add_customer_submit()
    add_customer_page.parse_alert("Customer added successfully with customer id")


def test_add_customer_dublicate(browser, config, login_manager):
    manager_page = login_manager
    manager_page.click_add_customer_button(config["url"]["addcustomer"])
    add_customer_page = AddCustomerPage(browser, browser.current_url)
    add_customer_page.add_customer(
        config["info_about_customers"]["Albus Dumbledore"]["FirstName"],
        config["info_about_customers"]["Albus Dumbledore"]["LastName"],
        config["info_about_customers"]["Albus Dumbledore"]["PostCode"],
    )
    add_customer_page.add_customer_submit()
    add_customer_page.parse_alert(
        "Please check the details. Customer may be duplicate."
    )


@pytest.mark.parametrize("empty", ["first_name", "last_name", "post_code"])
def test_add_customer_empty_field(browser, config, empty, login_manager):
    manager_page = login_manager
    manager_page.click_add_customer_button(config["url"]["addcustomer"])
    add_customer_page = AddCustomerPage(browser, browser.current_url)
    add_customer_page.create_fake_user(empty)
    add_customer_page.add_customer_submit()
    add_customer_page.parse_alert(None)
