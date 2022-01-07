from selenium import webdriver
from check import Check

CHROME_WEBDRIVER = 'E:\PROJECTS\chromedriver'
# Web Driver
driver = webdriver.Chrome(executable_path=CHROME_WEBDRIVER)
driver.get('https://orteil.dashnet.org/experiments/cookie/')
cookie = driver.find_element_by_id('cookie')

# Upgrades
upgrades_investment = Check()


while True:
    cookie.click()
    money = driver.find_element_by_id('money')
    print(money.text)