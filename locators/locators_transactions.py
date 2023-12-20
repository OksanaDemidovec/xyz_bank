from selenium.webdriver.common.by import By


class TransactionsPage:
    TRANSACTIONS_BUTTON = (By.XPATH, "//button[@ng-click='transactions()']")
    CALENDAR_START = (By.XPATH, "//*[@id='start']")
    CALENDAR_END = (By.XPATH, "//*[@id='end']")
    BACK_BUTTON = (By.XPATH, "//*[@ng-click='back()']")
    RESET_BUTTON = (By.XPATH, "//*[@ng-click='reset()']")
    FIRST_CELL_TRANSACTIONS = (By.XPATH, "// *[ @ id = 'anchor0'] / td[1]")
    PAGINATION_BUTTON_R = (By.XPATH, "//*[@ng-click='scrollRight()']")
    PAGINATION_BUTTON_L = (By.XPATH, "//*[@ng-click='scrollLeft()']")
    TOP_BUTTON = (By.XPATH, "//*[@ng-click='scrollTop()']")


class WithdrawlDepositPage:
    DEPOSIT_BUTTON_1 = (By.XPATH, "//div[@class='borderM box padT20 ng-scope']//div[3]//button[2]")
    WITHDRAWL_BUTTON_1 = (By.XPATH, "//div[@class='borderM box padT20 ng-scope']//div[3]//button[3]")
    DEPOSIT_BUTTON_2 = (By.XPATH, "//button[@class='btn btn-default']")
    WITHDRAWL_BUTTON_2 = (By.XPATH, "//button[@class='btn btn-default']")
    AMOUNT_INPUT = (By.XPATH, "//div[@class='form-group']//input[1]")
    MESSAGE = (By.XPATH, "//div[@class='borderM box padT20 ng-scope']/div[4]/div/span")
    SUCCESSFUL_MESSAGE_W = (By.XPATH, "//span[text()='Transaction successful']")
    SUCCESSFUL_MESSAGE_D = (By.XPATH, "//span[text()='Deposit Successful']")


class SortingPage:
    SORTING_DATE = (By.XPATH, "//*[contains(text(), 'Date-Time')]")
    UPDATE_LIST_TRANSACTIONS = (By.CSS_SELECTOR, "table tbody tr")
    DATE_TRANSACTIONS = (By.XPATH, "//tr/td[1]")
    SORTING_AMOUNT = (By.XPATH, "//*[contains(text(), 'Amount')]")
    SORTING_TYPE = (By.XPATH, "//*[contains(text(), 'Transaction Type')]")
    FIRST_CELL_TYPE = (By.XPATH, "//*[@id='anchor0']/td[3]")
    SECOND_CELL_TYPE = (By.XPATH, "//*[@id='anchor1']/td[3]")
