from selenium.webdriver.common.by import By


class LoginPageLocators:
    USER_LOGIN_BUTTON = (By.XPATH, "//*[text()='Customer Login']")
    MANAGER_LOGIN_BUTTON = (By.XPATH, "//*[text()='Bank Manager Login']")


class AccountPageLocators:
    WELCOME_MESSAGE = (
        By.XPATH,
        "//strong[contains(., 'Welcome')]//span[text()='{}']",
    )
    LOGOUT_BUTTON = (By.XPATH, "//button[@class='btn logout']")
    TRANSACTIONS_BUTTON = (By.XPATH, "//div[@class='borderM box padT20 ng-scope']//div[3]//button[1]")
    DEPOSIT_BUTTON = (By.XPATH, "//div[@class='borderM box padT20 ng-scope']//div[3]//button[2]")
    WITHDRAWL_BUTTON = (By.XPATH, "//div[@class='borderM box padT20 ng-scope']//div[3]//button[3]")
    ACCOUNT_SELECTOR = (By.CSS_SELECTOR, "#accountSelect")
    SELECTOR_1 = (By.XPATH, '//*[@id="accountSelect"]/option[1]')
    SELECTOR_2 = (By.XPATH, '//*[@id="accountSelect"]/option[2]')
    ACCOUNT_NUMBER = (By.XPATH, "//div[@class='center']//strong[1]")
    BALANCE = (By.XPATH, "//div[@class='center']//strong[2]")
    CURRENCY = (By.XPATH, "//div[@class='center']//strong[3]")


class LoginCustomerLocators:
    CUSTOMER_LOGIN_SUBMIT = (By.XPATH, "//button[@type='submit']")
    USER_OPTION = (By.XPATH, "//option[text()='{}']")


class ManagerPageLocators:
    ADD_CUSTOMER_TAB = (
        By.XPATH,
        "//*[contains(@class,'btn-lg') and contains(text(),'Add Customer')]",
    )
    OPEN_ACCOUNT_TAB = (By.XPATH, "//*[contains(text(), 'Open Account')]")
    CUSTOMERS_TAB = (By.XPATH, "//*[contains(text(), 'Customers')]")


class AddCustomerLocators:
    ADD_CUSTOMER_BUTTON = (
        By.XPATH,
        "//button[@type='submit']",
    )
    FIRST_NAME_FIELD = (
        By.XPATH,
        "//*[@ng-model='fName']",
    )
    LAST_NAME_FILED = (
        By.XPATH,
        "//*[@ng-model='lName']",
    )
    POST_CODE_FIELD = (
        By.XPATH,
        "//*[@ng-model='postCd']",
    )


class OpenAccountLocators:
    USER_OPTION_ACCOUNT = (By.XPATH, "//option[text()='{}']")
    CURRENCY_OPTION = (By.XPATH, "//option[text()='{}']")
    PROCESS_BUTTON = (By.XPATH, "//button[@type='submit']")
    ALERT_MESSAGE = (By.XPATH, "//*[contains(@class,'btn-lg') and contains(text(),'Open Account')]")


class CustomersTabLocators:
    DELETE_CUSTOMER_BUTTON = (By.XPATH, "//tr[td[text()='{}'] and td[text()='{}']]/td/button[text()='Delete']")
    CHECK_CUSTOMER_IN_TABLE = (By.XPATH, "//tr[td[contains(text(), '{}')]]")
    SEARCH_CUSTOMER = (By.XPATH, "//input[@placeholder='Search Customer']")
    FIELD_FOR_SORTING = (By.XPATH, "//a[contains(text(), '{}')]")
    VALUES = (
        By.XPATH,
        "//tr[@ng-repeat='cust in Customers | orderBy:sortType:sortReverse | filter:searchCustomer']")
    TABLE = (By.XPATH, "//table[@class='table table-bordered table-striped']")
    ROW = (By.XPATH, "//tr/td[1]")


class DepositPageLocators:
    AMOUNT_INPUT = (By.XPATH, "//div[@class='form-group']//input[1]")
    DEPOSIT_BUTTON = (By.XPATH, "//button[@class='btn btn-default']")
    MESSAGE = (By.XPATH, "//div[@class='borderM box padT20 ng-scope']/div[4]/div/span")
    SUCCESSFUL_MESSAGE = (By.XPATH, "//span[text()='Deposit Successful']")


class WithdrawlPageLocators:
    AMOUNT_INPUT = (By.XPATH, "//div[@class='form-group']//input[1]")
    WITHDRAWL_BUTTON = (By.XPATH, "//button[@class='btn btn-default']")
    MESSAGE = (By.XPATH, "//div[@class='borderM box padT20 ng-scope']/div[4]/div/span")
    FAIL_MESSAGE = (By.XPATH, "//span[text()='Transaction Failed. You can not withdraw amount more than the balance.']")
    SUCCESSFUL_MESSAGE = (By.XPATH, "//span[text()='Transaction successful']")
