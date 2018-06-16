from __future__ import print_function
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys,time
from  googlecalapi import addtocalapi

fb_id=input("Enter your email ID: ")               #fb_id has your login id
fb_pwd=input("Enter your facebook password: ")     #fb_pwd has your password

_browser_profile = webdriver.FirefoxProfile()
_browser_profile.set_preference("dom.webnotifications.enabled", False)
_browser_profile.set_preference("dom.push.enabled", False)
driver=webdriver.Firefox(firefox_profile=_browser_profile)

driver.get("https://www.facebook.com")

login=driver.find_element_by_xpath('//*[@id="email"]')
login.send_keys(fb_id)

password=driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys(fb_pwd)
password.send_keys(Keys.ENTER)


time.sleep(10)

driver.get("https://facebook.com/events/birthdays")

SCROLL_PAUSE_TIME = 3


last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

html=driver.page_source
soup=BeautifulSoup(html,'html.parser')

print(soup.title)

month_box=soup.findAll("div",{"class":"_43qm _tzu _43q9"})

name=[]
date=[]
for i in range(len(month_box)):
    image=month_box[i].findAll("img")
    a=month_box[i].findAll("a",{"class":"link"})
    for j in range(len(image)):
        name.append(image[j]['alt'])
        ddate=a[j]['data-tooltip-content']
        date.append(ddate.split('(')[-1].strip(')'))


birthdays=dict(zip(name,date))

remove=[]
for k,v in birthdays.items():
    if 'day' in v:
        remove.append(k)

for i in remove:
    del(birthdays[i])

addtocalapi(birthdays)
