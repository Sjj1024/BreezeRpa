import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面
# 打开网页
url = "https://zentao.metrodata.cn/user-login.html"
browser = webdriver.Chrome(options=chrome_options)
browser.get(url)
# 等待时间（隐式）全局元素等待
# browser.implicitly_wait(5)
# browser.maximize_window()  #最大化窗口

# 自动登录
# elem_name = browser.find_element_by_id("account").send_keys("chenliping")
# elem_passwd = browser.find_element_by_name("password").send_keys("Mdt12345")
# elem_log = browser.find_element_by_id("submit").click()


# 显示等待(自动登录）
wait = WebDriverWait(browser, 10)
input_name = wait.until(EC.presence_of_element_located((By.ID, "account"))).send_keys("chenliping")
input_passwd = wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("Mdt12345")
button = wait.until(EC.element_to_be_clickable((By.ID, "submit"))).click()

# time.sleep(1)
# btns = browser.find_elements(By.CLASS_NAME, "show-in-app")

# 页面跳转后切换到新页面
time.sleep(1)
print(f"页面是:{browser.window_handles}")
browser.switch_to.window(browser.window_handles[0])

# 点击项目集
button2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menuMainNav"]/li[2]/a'))).click()
# 获取信息
# Name = browser.find_element_by_xpath('//*[@id="block1973"]/div[2]/div/div[1]/h4')
# print(Name)
# time.sleep(1)
# browser.switch_to.frame('appIframe-my')
# h4 = wait.until(EC.presence_of_element_located((By.XPATH, '//h4'))).get_attribute("textContent")
# print(h4)

# browser.switch_to.frame('appIframe-my')
# h4 = wait.until(EC.presence_of_element_located((By.XPATH, '//h4'))).get_attribute("textContent")
# print(h4)

# 切换到项目集
browser.switch_to.frame('appIframe-program')
# innerHTML = wait.until(EC.presence_of_element_located((By.XPATH, '//*'))).get_attribute("innerHTML")
# print(innerHTML)

# 查找到table
arr = []
table_rows = wait.until(EC.presence_of_element_located((By.ID, "programList")))
print(table_rows)
# innerHTML = wait.until(EC.presence_of_element_located((By.XPATH, '//*'))).get_attribute('innerHTML')
# # h4 = wait.until(EC.presence_of_element_located((By.XPATH, '//')))
# print(innerHTML)
