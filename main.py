from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

PATH = "/home/ahmad/Templates/chrome-driver/chromedriver"
serv = Service(PATH)
driver = webdriver.Chrome(service=serv)
driver.get("https://10fastfingers.com/")

time.sleep(3)

driver.quit()