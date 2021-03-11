# 導入模組
import os
import sys
import time
from random import randint    
from selenium import webdriver

# 設定搜尋目標
targetAsset = '2330.TW'

# 指定下載路徑
options = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "D:\\Crawler\\DownloadData"}
options.add_experimental_option('prefs', prefs)

# 使用 Chrome 瀏覽器驅動
driver = webdriver.Chrome('D:\\Crawler\\chromedriver.exe', chrome_options = options)

# 進入yahoo finance網站
driver.get('https://finance.yahoo.com/')

# 搜尋輸入框 id
inputElement = driver.find_element_by_css_selector('#yfin-usr-qry')

# 傳入字串
inputElement.send_keys(targetAsset)

# 提交表單
inputElement.submit()

# 等待頁面刷新，讓程式休息5秒
time.sleep(5)

# 使用 CSS定位 Historical Data
items = driver.find_elements_by_css_selector('a span')
for item in items:
    if item.text == 'Historical Data':
        item.click()
        break

# 讓程式隨機休息 1 ~ 3秒 
time.sleep(randint(1, 3))

# 使用 CSS定位，開啟 Time Period設定框
arrows = driver.find_elements_by_css_selector("div[data-test=\"dropdown\"] span,svg[data-icon=\"CoreArrowDown\"]")[2].click()

# 讓程式隨機休息 1 ~ 3秒 
time.sleep(randint(1, 3))

# 使用 CSS定位，將時間調整到 5年
durations = driver.find_elements_by_css_selector("ul li button[data-value=\"5_Y\"] span")
for duration in durations:
    if duration.text == '5Y':
        duration.click()
        break

# 讓程式隨機休息 1 ~ 3秒 
time.sleep(randint(1, 3))

# 使用 CSS定位，點擊 APPly
buttons = driver.find_elements_by_css_selector('button span')
for button in buttons:
    if button.text == 'Apply':
        button.click()
        break
        
# 讓程式隨機休息 1 ~ 3秒 
time.sleep(randint(1, 3))
        
# 使用 CSS定位，點擊 Download
links =  driver.find_elements_by_css_selector('a span')
for link in links:
    if link.text == 'Download':
        link.click()
        break
# 讓程式休息 10秒         
time.sleep(10)

# 關閉瀏覽器
driver.quit()
