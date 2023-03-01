from selenium import webdriver
driver =webdriver.Firefox('/usr/local/bin/geckodriver')
driver.get("https://app3.factohr.com/infolitz")
driver.find_element(By.ID,"txtUsername").send_keys("125")
driver.find_element(By.ID,"txtPassword").send_keys("Meeting@11")
driver.find_element(By.ID,"btnLogin").click()
