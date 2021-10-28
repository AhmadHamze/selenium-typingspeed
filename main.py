from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from requests_html import HTML

import time

PATH = "/home/ahmad/Templates/chrome-driver/chromedriver"
serv = Service(PATH)
driver = webdriver.Chrome(service=serv)
driver.get("https://10fastfingers.com/typing-test/english")
try:
    
    wordsContainer = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "row1"))
    )
    driver.implicitly_wait(10)
    # The line below is essential, it allows the display of the spans containing the
    # words to type. Without it "driver.page_source" won't be able to capture the spans
    wordsContainer.find_elements(By.TAG_NAME, "span")
    
    html = HTML(html=driver.page_source)
    match = html.find("#row1", first=True)
    words = match.text.split(" ")
    inputField = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inputfield"))
    )
    for word in words:
        inputField.send_keys(word)
        inputField.send_keys(Keys.SPACE)
    timer = driver.find_element(By.ID, "timer")
    timer = timer.text[2:]
    timer = int(timer)
    print(f"{(len(words) * 60) / (60 - timer)} WPM")
    time.sleep(60)
except Exception:
    print("An error occured!")

driver.quit()