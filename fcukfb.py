from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys,time

driver=webdriver.Firefox()

driver.get("https://www.facebook.com")

fb_id=sys.argv[1]               #fb_id has your login id
fb_pwd=sys.argv[2]              #fb_pwd has your password

login=driver.find_element_by_xpath('//*[@id="email"]')
login.send_keys(fb_id)

password=driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys(fb_pwd)
password.send_keys(Keys.ENTER)

time.sleep(10)
events=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div[3]/div[3]/ul/li[1]/a/div')
events.click()

time.sleep(5)
birthday=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[1]/div/div/div[2]/div[3]/a/span')
birthday.click()

html=driver.page_source
soup=BeautifulSoup(html,'html.parser')

print(soup.title)
