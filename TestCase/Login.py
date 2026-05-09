from Pages.Login_Pages import LoginPage

def test_login(driver):

    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("DLSFDU02", "root@123")
