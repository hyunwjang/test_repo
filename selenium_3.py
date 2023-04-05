from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# options = webdriver.ChromeOptions()
# options.add_argument("window-size=1000,1000")
# options.add_argument("no-sandbox")

chrome = webdriver.Chrome(r"./111/chromedriver.exe")
wait = WebDriverWait(chrome, 10)

#다나와 검색
def find_present(css):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))

def finds_present(css):
    find_present(css)
    return chrome.find_elements(By.CSS_SELECTOR,css)


def find_visible(css):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))

def finds_visible(css):
    find_visible(css)
    return chrome.find_elements(By.CSS_SELECTOR,css)


chrome.get("https://shop.danawa.com/virtualestimate/?controller=estimateMain&methods=index&marketPlaceSeq=16&logger_kw=dnw_gnb_esti")

time.sleep(1)
total = finds_visible("div.search_option_list div.search_option_item")

division = [x.text for x in total]
# print(division[0].split("\n"))

def c_cpu(count):
    company = division[count].split("\n")[1:]
    for i in range(len(company)):
        print(str(i+1)+"."+ company[i])
    cpu_brand = input(">>>>")
    find_visible(f"div.search_option_list div:nth-child({count+1}) ul li:nth-child({cpu_brand}) span").click()
    time.sleep(1)

# print([x.text for x in finds_visible("div.search_cate_title")])
category = [x.text for x in finds_visible("div.search_cate_title")]
category = [v for v in category if v]
#널값 제거

def categort_totle():
    for i in range(len(category)):
        print(str(i+1) + ": " + category[i])

while 1:
    categort_totle()
    print('--------------------------------')
    cpu_count = input()
    print('--------------------------------')
    if int(cpu_count) < int(100):
        c_cpu(int(cpu_count)-1)
    else:
        break


# for cat in range(len(category)):

#     c_cpu(cat)

find_visible("#searchDetailButton").click()
time.sleep(1)
find_visible("#submitSearchDetail").click()
time.sleep(5)
chrome.quit()

#chrome.switch_to.parent_frame()
#부모 인자로 돌아감