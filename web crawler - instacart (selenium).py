from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import csv
import time

firefox_path = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe' # 改成你自己firefox.exe的位置
webdriver_path = 'D:\homework\geckodriver.exe' # 改成你檔案的位置
binary = FirefoxBinary(firefox_path)
driver = webdriver.Firefox(executable_path=webdriver_path,firefox_binary=binary)
driver.get("https://www.instacart.com/")

login_button = driver.find_element_by_link_text("Log in")
login_button.click()

email = driver.find_element_by_id("nextgen-authenticate.all.log_in_email")
email.send_keys('b90607029@gmail.com')
pwd = driver.find_element_by_id("nextgen-authenticate.all.log_in_password")
pwd.send_keys('medical0411')

# 第二次log in按鈕無法正確取得元素，改用Xpath搜尋
login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()

input = ''
# 讀取時間太久，容易報錯誤訊息，用迴圈直到成功為止
while True:
    try:
        input = driver.find_element_by_xpath("//input[@type='search']")
        break
    except:
        continue
count = 0

# UnicodeDecodeError錯誤，問題不是出在資料檔，而是 Python 腳本的預設編碼，
# 所以我們只要告訴 Python 我們要讀取的檔案是以 UTF-8 編碼即可解決
with open('products.csv', newline='', encoding="utf-8") as csvfile:
    products = csv.reader(csvfile)
    for row in products:
        product_id = row[0]
        product_name = row[1].strip('"')
        product_page = f"https://www.instacart.com/store/sprouts/search_v3/{product_name}"
        driver.get(product_page)

