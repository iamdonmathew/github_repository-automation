from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_path = r"C:\Users\iamdo\Downloads\chromedriver.exe" # specify your driver location
driver = webdriver.Chrome(chrome_path)
driver.get("https://github.com/login")
username = "your email" # specify your email
password = "your password" # specify your password
usernamefield = driver.find_element_by_name("login")
usernamefield.clear()
usernamefield.send_keys(username)
pfield = driver.find_element_by_name("password")
pfield.clear()
pfield.send_keys(password)
driver.find_element_by_name("commit").click()
driver.find_element_by_xpath("""/html/body/div[5]/div/aside[1]/div[2]/div[1]/div/h2/a""").click()
reponame = driver.find_element_by_name("repository[name]")
reponame.send_keys("Test") # specify your repository name
driver.find_element_by_xpath("""//*[@id="repository_visibility_public"]""").click()
driver.find_element_by_xpath("""//*[@id="repository_auto_init"]""").click()
driver.find_element_by_xpath("""//*[@id="repo-new-license-details"]/summary""").click()
driver.find_element_by_xpath("""//*[@id="license-label-mit"]""").click()
time.sleep(1)
driver.find_element_by_xpath("""//*[@id="new_repository"]/div[3]/button""").click()
time.sleep(4)
driver.close()

