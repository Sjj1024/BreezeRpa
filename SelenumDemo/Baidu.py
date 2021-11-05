import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
# 设置隐式等待，超时10秒
wait = WebDriverWait(browser, 10)
browser.get("https://www.baidu.com/")
# 点击搜索按钮
input = wait.until(EC.presence_of_element_located((By.ID, 'kw')))
input.send_keys("python")
# time.sleep(2)
# # 关闭浏览器
# browser.close()
