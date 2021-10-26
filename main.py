from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

PATH = "/home/ahmad/Templates/chrome-driver/chromedriver"
serv = Service(PATH)
driver = webdriver.Chrome(service=serv)
driver.get("https://10fastfingers.com/")
try:
    
    startButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "typing-test"))
    )
    startButton.click()
    wordsContainer = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "row1"))
    )
    driver.implicitly_wait(10)
    spans = wordsContainer.find_elements(By.TAG_NAME, "span")
    
    print(f"number of words: {len(spans)}")
    for span in spans:
        print(span.text)
except Exception:
    print("An error occured!")

driver.quit()