import pytest
from pythongirlpower.pages.customers_tab_page import CustomersTabPage


@pytest.mark.parametrize("field", ["First Name", "Last Name", "Post Code"])
def test_sorting_by_field(browser, config, login_manager, field):
    manager_page = login_manager
    manager_page.click_customers_button(config["url"]["customers_tab"])
    customer_tab_page = CustomersTabPage(browser, config)
    values = customer_tab_page.sorting_by_field(field)
    assert [value.text for value in values] == sorted([value.text for value in values])
    values1 = customer_tab_page.sorting_by_field(field)
    assert [value1.text for value1 in values1] == sorted([value1.text for value1 in values1], reverse=True)
