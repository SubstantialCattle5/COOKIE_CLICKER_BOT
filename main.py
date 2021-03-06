from selenium import webdriver
from check import Check
import time
import math

CHROME_WEBDRIVER = 'E:\PROJECTS\chromedriver'
# Web Driver
driver = webdriver.Chrome(executable_path=CHROME_WEBDRIVER)
driver.get('https://orteil.dashnet.org/experiments/cookie/')
cookie = driver.find_element_by_id('cookie')

# Upgrades
upgrades_investment = Check()

def money_converter(org_money) :
    return org_money.replace(',' ,'')

count = 0
while True:
    count = count + 1
    cookie.click()
    money = driver.find_element_by_id('money')
    money = money_converter(money.text)

    if count % 5 == 0:
        upgrades_investment.value_check(saved=int(money))
        buy = driver.find_element_by_id(upgrades_investment.id)
        buy.click()

