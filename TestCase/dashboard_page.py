from selenium.webdriver.common.by import By
from utils.Wait_utils import WaitUtils

class DashboardPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver)

        self.sasci_menu = (By.XPATH, "//a[@title='S.A.S.C.I.']")
        self.create_proposal = (By.XPATH, "//a[normalize-space()='Create Project Proposal']")

    def navigate_to_create_proposal(self):
        self.wait.wait_for_element_clickable(self.sasci_menu).click()
        self.wait.wait_for_element_clickable(self.create_proposal).click()