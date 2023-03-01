import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By

firefox_driver_path = "/usr/bin/geckodriver"
firefox_binary_path = "/usr/bin/firefox"
firefox_options = webdriver.FirefoxOptions()
firefox_options.binary_location = firefox_binary_path
driver_service = webdriver.firefox.service.Service(firefox_driver_path)
driver = webdriver.Firefox(service=driver_service, options=firefox_options)

driver.get("https://app3.factohr.com/infolitz")
driver.maximize_window()  # For maximizing window
driver.find_element(By.ID, "txtUsername").clear()
driver.find_element(By.ID, "txtUsername").send_keys("125")
time.sleep(2)
driver.find_element(By.ID, "txtPassword").clear()
driver.find_element(By.ID, "txtPassword").send_keys("Meeting@11")
time.sleep(3)
driver.find_element(By.ID, "btnLogin").click()
time.sleep(5)
t1 = "Infolitz Software Pvt Ltd"
label = driver.find_element(By.XPATH, '//*[@id="divCompanyName"]').text
if label != t1:
    print("Login Failed")
else:
    print("Login Successfull")
# driver.find_element(By.ID, "searchText").send_keys("online attendance")
# time.sleep(5)
# pyautogui.press('Enter')
time.sleep(2)
da = driver.find_element(By.XPATH, '//*[@id="dashbordMenu"]')
time.sleep(4)
da.click()
time.sleep(3)
gl = driver.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/nav/ul[1]/li[1]/ul/li/a')
gl.click()
time.sleep(8)
punch = driver.find_element(By.XPATH, '//input[@id="btnIn" and @class="btn btn-primary"]')
time.sleep(1)
# time.sleep(3)
# print(punch)
# pu.click()
# time.sleep(2)
# driver.refresh()
# exit()
# Hr_title = driver.title
# exp_title =
# driver.find_element(By.ID,"IMG_26").click()
# driver.find_element(By.ID,"UL_29").click()
# driver.find_element(By.ID, "searchText").send_keys("online attendance")
driver.close()
