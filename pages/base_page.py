from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import random


class BasePage:
    def __init__(self, driver, url=None):
        self.url = url
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def open(self):
        self.driver.get(self.url)

    def log_info(self, message):
        self.logger.info(message)

    def wait_for_url(self, expected_url, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(expected_url)
        )

    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_invisibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_for_alert(self, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.alert_is_present()
        )

    def random_more_than_100(self):
        return random.randrange(100, 1000)

    def random_less_than_100(self):
        return random.randrange(1, 100)

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def wait_for_visibility_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )
