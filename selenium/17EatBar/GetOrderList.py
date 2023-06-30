import time
from datetime import datetime
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# 使用Line Notify回報
def lineNotifyMessage(token, msg):
    url = 'https://notify-api.line.me/api/notify'
    headers = {
        "Authorization": "Bearer " + token,
        # "Content-Type": "multipart/form-data"
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {
        "message": msg,
    }
    # 要傳送的圖片檔案
    image_path = ""  # 將路徑替換為你的圖片路徑
    if image_path:
        files = {"imageFile": open(image_path, "rb")}
        response = requests.post(url, headers=headers, data=payload, files=files)
    else:
        response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        print("訊息已成功發送")
    else:
        print("發送訊息時發生錯誤 : ", response.status_code)


# 設定網頁選項
def settingOption():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-extensions")
    # 要用途為取消網頁中的彈出視窗，避免妨礙網路爬蟲的執行。
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--stat-maximized")
    chrome_options.add_argument("--no-sandbox")
    return chrome_options


# 取得訂餐資訊
def getData():
    data = []
    i = 1
    try:
        while (True):
            order = driver.find_element(By.XPATH,
                                        '//*[@id="app"]/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/div[1]/table/tbody/tr[' + str(
                                            i) + ']').text
            i = i + 1
            user = order.replace('修改', '').replace('作廢', '').replace('\n', '')
            if user.__contains__('D02'):
                data.append(user + '\n')

    except:
        print('今天B辦公室共===>', i, '人訂餐')
    finally:
        return data


# 計算最終金額
def getTotalPrrice(l):
    total = 0
    for item in l:
        # 提取最後的數字
        last_num = int(item.split()[-1])
        # 將最後的數字相加
        total += last_num

    return total


if __name__ == '__main__':
    driver_path = "/WriteoffServer_VN/driver/chromedriver_win32_113.0.5672.63/chromedriver.exe"
    url = "https://eip.1177tech.com.tw/17chihebar/index.html#/order"
    userID = 'osperwu'
    pwd = 'Aa030606'
    token = 'BOQQUxqftVug50d1AtHdfideu3vAAqPB1Ur862izwDE'  # RD1
    # token = 'GUfngH9605YHPxFFiCkOvwKMUhIs5UL7LD7ezDZjCWO'  # EIP

    driver = webdriver.Chrome(driver_path, options=settingOption())
    time.sleep(1)
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/form/div[1]/div[2]/div/span/input').send_keys(userID)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/form/div[2]/div[2]/div/span/span/input').send_keys(pwd)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/button[2]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/ul/li[4]').click()
    time.sleep(1)
    shopName = driver.find_element(By.XPATH,
                                   '//*[@id="app"]/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[1]/div[1]').text
    print(shopName)
    data = getData()
    total = len(data)
    # print('RD1共', total, '人訂餐')
    price = getTotalPrrice(data)
    # print('共$', price)
    time.sleep(1)

    currentDateAndTime = datetime.now()
    msg = str(currentDateAndTime).split(".")[0] + '\n🌽🤞🐱‍🚀🍆RD1共' + str(
        len(data)) + '人訂餐\n' + '🍑💦👌🏼😎' + shopName + '\n'
    for i in data:
        msg = msg + i

    msg = msg + '共$' + str(price)
    print(msg)
    lineNotifyMessage(token, msg)
    driver.quit()
