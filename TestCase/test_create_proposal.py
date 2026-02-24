from Pages.login_page import LoginPage
from Pages.dashboard_page import DashboardPage

def test_navigation(driver):

    login = LoginPage(driver)
    dashboard = DashboardPage(driver)

    login.load()
    login.login("DLSFDU02", "root@123")

    dashboard.navigate_to_create_proposal()