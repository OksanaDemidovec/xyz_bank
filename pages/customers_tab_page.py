from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from pythongirlpower.locators.locators import CustomersTabLocators


class CustomersTabPage(BasePage):
    def delete_customer(self, customer):
        first_name, last_name = customer.split()
        delete_button_locator = CustomersTabLocators.DELETE_CUSTOMER_BUTTON
        delete_button_locator = (delete_button_locator[0], delete_button_locator[1].format(first_name, last_name))
        delete_button_option = self.wait_for_clickable(delete_button_locator)
        delete_button_option.click()
        self.logger.info(f"The customer {customer} is deleted")

    def search_customer(self, locator):
        search_field_locator = CustomersTabLocators.SEARCH_CUSTOMER
        search_field = self.wait_for_visibility(search_field_locator)
        search_field.send_keys(locator)
        search_field.send_keys(Keys.ENTER)
        self.logger.info(f"The search by {locator} is completed")

    def find_customer_after_searching(self, customer, another_customer):
        first_name, last_name = customer.split()
        first_name1, last_name1 = another_customer.split()
        customer_locator = CustomersTabLocators.CHECK_CUSTOMER_IN_TABLE
        customer_locator = (customer_locator[0], customer_locator[1].format(last_name))
        if self.is_element_present(customer_locator):
            customer_on_page = self.wait_for_visibility(customer_locator)
            customer_text = customer_on_page.text
            customer_name = " ".join(customer_text.split()[:2])
            self.logger.info("The customer %s is present on the page", customer_name)
            customer_locator = CustomersTabLocators.CHECK_CUSTOMER_IN_TABLE
            customer_locator = (customer_locator[0], customer_locator[1].format(last_name1))
            self.wait_for_invisibility(customer_locator)
            self.logger.info("Another customer %s isn`t present on the page", another_customer)
            return customer_name
        else:
            self.logger.info("The wrong customer %s is not present on the page", customer)
            return "Customer not found"

    def search_deleted_customer(self, customer):
        first_name, last_name = customer.split()
        customer_locator = CustomersTabLocators.CHECK_CUSTOMER_IN_TABLE
        customer_locator = (customer_locator[0], customer_locator[1].format(last_name))
        self.wait_for_invisibility(customer_locator)
        self.logger.info("The customer %s not found on the page", customer)

    def clear_searching_field(self):
        search_field_locator = CustomersTabLocators.SEARCH_CUSTOMER
        search_field = self.wait_for_visibility(search_field_locator)
        search_field.clear()

    def sorting_by_field(self, field):
        sort_field_locator = CustomersTabLocators.FIELD_FOR_SORTING
        sort_field_locator = (sort_field_locator[0], sort_field_locator[1].format(field))
        sort_field = self.wait_for_clickable(sort_field_locator)
        sort_field.click()
        self.logger.info("Data is sorted by field %s", field)
        rows = self.wait_for_visibility_elements(CustomersTabLocators.ROW)
        values = []
        for element in rows:
            value = self.wait_for_visibility(CustomersTabLocators.VALUES)
            values.append(value)
        return values
