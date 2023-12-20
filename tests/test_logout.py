from pythongirlpower.pages.account_page import AccountPage


def test_user_logout(browser, config, login_customer):
    login_customer("username3")
    account_page = AccountPage(browser, browser.current_url)
    account_page.click_logout_button(config["url"]["customer"])
