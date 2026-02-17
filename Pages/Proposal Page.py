import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def Proposalpage():
    driver.find_element(By.XPATH, "//a[@title='S.A.S.C.I.']").click()
    time.sleep(2)
#action.move_to_element(driver.find_element(By.XPATH, "//a[@title = 'Schemes Master']")).perform()

#time.sleep(4)
    driver.find_element(By.XPATH, "//a[normalize-space()='Create Project Proposal']").click() #use normalize space for remove extra space

time.sleep(4)
