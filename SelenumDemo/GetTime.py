# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
# capabilities = DesiredCapabilities.CHROME
# capabilities['loggingPrefs'] = {'browser': 'ALL'}
#
# driver = webdriver.Chrome(desired_capabilities=capabilities)
#
# driver.get('https://www.baidu.com')
#
# # print console log messages
# for entry in driver.get_log('browser'):
#     print(entry)
"""
entry格式：
{'level': 'SEVERE', 'message': 'https://open.ccod.com/WARTC/cphoneRTC/verto-min.js 2086:28 "INVALID METHOD OR NON-EXISTANT CALL REFERENCE IGNORED" "verto.clientReady"', 'source': 'console-api', 'timestamp': 1626147049481}
其中source：

console-api 控制台日志
network 网络日志
"""

#
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# import json
#
#
# class Mychrome:
#
#     def __init__(self):
#         self.options = webdriver.ChromeOptions()
#         self.flash_urls = []
#         self.set_browser()
#
#     def set_browser(self):
#
#         prefs = {
#             "profile.managed_default_content_settings.images": 1,
#
#         }
#         if self.flash_urls is not None and len(self.flash_urls) != 0:
#             prefs['profile.managed_plugins_allowed_for_urls'] = self.flash_urls
#         self.options.add_experimental_option('prefs', prefs)
#         self.options.add_experimental_option('w3c', False)
#
#         # 方法1
#         # capabilities = DesiredCapabilities.CHROME
#         # capabilities['loggingPrefs'] = {"performance","all"}
#         # self.driver = webdriver.Chrome(
#         #     desired_capabilities=capabilities
#         # )
#
#         # 方法2
#         # self.options.add_experimental_option("excludeSwitches", ['enable-automation'])  # window.navigator.webdriver设置为undefined，逃过网站的防爬检查,headless无效
#         desired_capabilities = self.options.to_capabilities()  # 将功能添加到options中
#         desired_capabilities['loggingPrefs'] = {
#             "performance": "ALL"  # 添加日志
#         }
#         self.driver = webdriver.Chrome(
#             desired_capabilities=desired_capabilities
#         )
#
#     def gethtml(self):
#         url = 'http://www.baidu.com'
#         self.driver.get(url)
#         print(self.driver.get_log('performance'))
#         print('-' * 60)
#         print(self.driver.get_log('performance'))
#         for entry in self.driver.get_log('performance'):
#             params = json.loads(entry.get('message')).get('message')
#             print(params.get('request'))  # 请求连接 包含错误连接
#             print(params.get('response'))  # 响应连接 正确有返回值得连接
#
#
# if __name__ == '__main__':
#     browser = Mychrome().gethtml()


import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

caps = {
    'browserName': 'chrome',
    'loggingPrefs': {
        'browser': 'ALL',
        'driver': 'ALL',
        'performance': 'ALL',
    },
    'goog:chromeOptions': {
        'perfLoggingPrefs': {
            'enableNetwork': True,
        },
        'w3c': False,
    },
}
driver = webdriver.Chrome(desired_capabilities=caps)

driver.get('https://www.kancloud.cn/ccjin/yingq/1631612')  # 免费天气接口
# driver.get('https://www.tianqiapi.com/free/day?appid=23035354&appsecret=8YvlPNrz')  # 免费天气接口
# 必须等待一定的时间，不然会报错提示获取不到日志信息，因为絮叨等所有请求结束才能获取日志信息
time.sleep(3)

driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div/div[3]/span[2]/a').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div/div[3]/span[2]/a').click()

time.sleep(3)

request_log = driver.get_log('performance')
# request_log = driver.get_log('server')
# print(request_log)
print("len(request_log)", len(request_log))
print(request_log)

for i in range(len(request_log)):
    message = json.loads(request_log[i]['message'])
    message = message['message']['params']
    # .get() 方式获取是了避免字段不存在时报错
    request = message.get('request')
    if (request is None):
        continue

    url = request.get('url')
    print("url", url)
    # if (url == "https://www.tianqiapi.com/free/day?appid=23035354&appsecret=8YvlPNrz"):
    #     # 得到requestId
    #     print(message['requestId'])
    #     # 通过requestId获取接口内容
    #     content = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': message['requestId']})
    #     print(content)
    #     break


driver.close()