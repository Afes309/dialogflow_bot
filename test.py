from selenium import webdriver
import time
import pickle





driver = webdriver.Chrome()
driver.get("https://google.com/")
driver.delete_all_cookies()
cookie = {'name' : 'foo', 'value' : 'bar'}
driver.add_cookie(cookie)

print(driver.get_cookies())


Мой телеграмм LisichkaAlisa



