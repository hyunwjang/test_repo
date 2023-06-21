from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox")

browser = webdriver.Chrome()
wait =WebDriverWait(browser, 10)

def find_present(css): #코드생성
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))

def finds_present(css): #코드생성
    find_present(css)
    return browser.find_elements(By.CSS_SELECTOR,css)

def find_visible(css): #창에 보이는것
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))

def finds_visible(css): #창에 보이는것
    find_visible(css)
    return browser.find_elements(By.CSS_SELECTOR,css)

browser.get("https://www.starbucks.co.kr/menu/drink_list.do?CATE_CD=product_cold_brew")

df = pd.DataFrame(columns = ['카테고리','메뉴명','칼로리','나트륨','포화지방','당류','단백질','카페인'])

datas = finds_present('div.product_list li.menuDataSet')
ind = 0
for data in range(len(datas)):
    time.sleep(2)
    find_visible('#mCSB_1_container li label').click()
    

    finds_present('div.product_list li.menuDataSet dl dt a img')[data].click()
    
    try:
        category = find_visible('div.sub_tit_inner h2 img').get_attribute('alt')
    except:
        print('카테고리가 없습니다.')
    name = find_visible('div.myAssignZone h4').get_attribute('innerText').split('\n')[0]
    kcal = find_visible('li.kcal dl dd').text
    sodiumg = find_visible('li.sodium dl dd').text
    sat_FAT = find_visible('li.sat_FAT dl dd').text
    sugars = find_visible('li.sugars dl dd').text
    protein = find_visible('li.protein dl dd').text
    caffeine = find_visible('li.caffeine dl dd').text

    print(category, name, kcal,sodiumg,sat_FAT,sugars,protein,caffeine)
    df.loc[ind]=[category,name,kcal,sodiumg,sat_FAT,sugars,protein,caffeine]
    ind = ind + 1
    
    browser.back()
    
    
    
df.to_csv(r'C:\Users\hyunwoo\Desktop\태블로\df_menu.csv',encoding='utf-8-sig')

time.sleep(3)