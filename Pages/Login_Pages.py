import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get ("https://training.pfms.gov.in/SitePages/Users/LoginDetails/Login.aspx")


#Test case = 1 Create Proposal
def Login():
    driver.find_element(By.XPATH,"//input[@id='UserName']").send_keys("DLSFDU02")
    driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("root@123")
# here need to enter captcha manually
    time.sleep(5)
    driver.find_element(By.XPATH,"//input[@id='ctl00_cphBody_btnLoginButton']").click()
time.sleep(2)

test data for automate.xlsx