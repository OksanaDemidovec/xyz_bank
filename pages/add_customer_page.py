from .base_page import BasePage
from pythongirlpower.locators.locators import AddCustomerLocators
from selenium.common.exceptions import NoAlertPresentException
import random
import string


class AddCustomerPage(BasePage):
    def add_customer(self, first_name, last_name, postcode):
        first_name_input_element = self.wait_for_visibility(
            AddCustomerLocators.FIRST_NAME_FIELD
        )
        last_name_input_element = self.wait_for_visibility(
            AddCustomerLocators.LAST_NAME_FILED
        )
        postcode_input_element = self.wait_for_visibility(
            AddCustomerLocators.POST_CODE_FIELD
        )
        first_name_input_element.send_keys(first_name)
        last_name_input_element.send_keys(last_name)
        postcode_input_element.send_keys(postcode)
        self.logger.info("Customer data is entered")

    def add_customer_submit(self):
        add_customer_submit_button = self.wait_for_clickable(
            AddCustomerLocators.ADD_CUSTOMER_BUTTON
        )
        add_customer_submit_button.click()

    def parse_alert(self, expected_text):
        try:
            alert = self.driver.switch_to.alert
            assert (
                expected_text in alert.text
            ), f"Expected part '{expected_text}' not found: {alert.text}"
            alert.accept()
        except NoAlertPresentException:
            self.logger.info("No alert is presented. Customer isn't created")
            pass

    def generate_fake_data(self):
        letters = string.ascii_lowercase
        return {
            "first_name": "".join(random.choice(letters) for i in range(10)),
            "last_name": "".join(random.choice(letters) for i in range(10)),
            "post_code": "".join(random.choices(string.digits, k=5)),
        }

    def create_fake_user(self, empty_field=None):
        fake_data = self.generate_fake_data()
        if empty_field:
            fake_data[empty_field] = ""
            self.logger.info(f"Leaving field '{empty_field}' empty.")
        self.add_customer(
            fake_data["first_name"],
            fake_data["last_name"],
            fake_data["post_code"]
        )
