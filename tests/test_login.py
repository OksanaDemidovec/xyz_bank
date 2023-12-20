from pythongirlpower.pages.account_page import AccountPage


def test_user_login(browser, config, login_customer):
    login_customer("username1")
    account_page = AccountPage(browser, browser.current_url)
    welcome_message = account_page.get_welcome_message(config["usernames"]["username1"])
    expected_welcome_message = f"{config['usernames']['username1']}"
    assert (
        welcome_message == expected_welcome_message
    ), f"Expected '{expected_welcome_message}', but got '{welcome_message}'"


def test_manager_login(browser, config, login_manager):
    current_url = browser.current_url
    assert current_url == config["url"]["manager"]
