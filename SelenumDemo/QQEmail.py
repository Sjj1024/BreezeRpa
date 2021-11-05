from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://mail.qq.com/')
wait = WebDriverWait(browser, 10)
wait.until(EC.element_to_be_clickable((By.ID, 'switcher_qlogin'))).click()
