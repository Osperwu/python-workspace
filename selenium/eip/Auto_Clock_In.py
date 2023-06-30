from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import time
import datetime
import requests
import random
import ddddocr
from PIL import Image


today = str(datetime.date.today())

# 使用Line Notify回報
def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code
# 權杖
token = 'GUfngH9605YHPxFFiCkOvwKMUhIs5UL7LD7ezDZjCWO'

# 啟動chrome_headless模式
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")
#要用途為取消網頁中的彈出視窗，避免妨礙網路爬蟲的執行。
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--stat-maximized")
chrome_options.add_argument("--no-sandbox")

executable_path="/WriteoffServer_VN/driver/chromedriver_win32_113.0.5672.63/chromedriver.exe"
# driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options)
driver = webdriver.Chrome(executable_path, options=chrome_options)
print(executable_path)
# time.sleep(60000)
login = "https://eipdev.1177tech.com.tw/EipConnect/web/#/login"
print(login)
driver.get(login)

# 擷取驗證碼
scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
driver.set_window_size(scroll_width, scroll_height)
driver.save_screenshot('./screenshot.png')
element = driver.find_element("xpath","//*[@id='app']/div/form/div/div/div[3]/img")
left = element.location['x']
right = element.location['x'] + element.size['width']
top = element.location['y']
bottom = element.location['y'] + element.size['height']
img = Image.open('./screenshot.png')
img = img.crop((left, top, right, bottom))
img = img.convert("RGB")
img.save('./screenshot.png')
# 解析驗證碼
ocr = ddddocr.DdddOcr()
with open('./screenshot.png','rb') as f:
    img = f.read()
res = ocr.classification(img)
#開始登入
driver.find_element("xpath","//*[@id='app']/div/form/div/div/div[1]/input").send_keys("osper.wu@1177tech.com.tw")
driver.find_element("xpath","//*[@id='app']/div/form/div/div/div[2]/input").send_keys("Aa123456")
driver.find_element("xpath","//*[@id='app']/div/form/div/div/div[3]/div[2]/input").send_keys(res)
submit = driver.find_element("xpath","//*[@id='app']/div/form/div/div/button[1]")
ActionChains(driver).click(submit).perform()
time.sleep(1)
print("login successful")
msg = 'login success'
lineNotifyMessage(token, msg)

check_button = driver.find_element("xpath","//*[@id='app']/div/div[1]/div[2]/div[1]/div[1]/div/div[1]")
ActionChains(driver).click(check_button).perform()
time.sleep(1)
clock_in = driver.find_element("xpath","//*[@id='app']/div/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/button").get_attribute("outerHTML").replace('"',"")
clock_out = driver.find_element("xpath","//*[@id='app']/div/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/button").get_attribute("outerHTML").replace('"',"")

print(clock_in)
print(clock_out)
# if "disabled=disabled" in clock_in:
#     msg = "\n★" + today + "★\n    今日已打卡~"
#     lineNotifyMessage(token, msg)
# else:
#     clock_in_go = driver.find_element("xpath","//*[@id='app']/div/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/button")
#     # stop = random.randrange(10, 290)
#     stop = 1
#     # time.sleep(stop)
#     ActionChains(driver).click(clock_in_go).perform()
#     msg = "\n★" + today + "★\n    打卡成功！" + "\n    延遲秒數:" + str(stop) + "秒"
#     lineNotifyMessage(token, msg)
