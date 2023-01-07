#here we are writing a program to scratch wikipedia site
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
#1 this below code for click on article count
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

#2 this below code for click on all portals
# all_portals = driver.find_element(By.LINK_TEXT, "Community portal")
# all_portals.click()

#3 this below code for searching python.
search = driver.find_element(By.NAME, "search")
search.send_keys("Python") #it will search Python
search.send_keys(Keys.ENTER) #it will click the enter button on search