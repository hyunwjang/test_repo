from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox")


browser = webdriver.Chrome(r"./111/chromedriver.exe",options=options)
# browser.get("https://www.naver.com/") # 사이트 접속
browser.get("https://shopping.naver.com/home")

# browser.back() #뒤로가기
# browser.forward()# 앞으로가기

# time.sleep(3) #심플하고 심플함 변수에 적용이 어려움
# browser.implicitly_wait(10) #
wait =WebDriverWait(browser, 10)


# a = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name=query]'))) #네이버 검색어
# a = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[class^=_searchInput]')))  # 네이버 쇼핑 검색어
search_d = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[class^=_searchInput]'))) #네이버 검색어 심화ㅑ

search_d.send_keys("갤럭시")
search_d.send_keys("\n")
# time.sleep(2)
# browser.switch_to.frame('searchIframe')
# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li span[class^=place_bl]'))) #네이버 검색어time.sleep(1)

# browser.find_element(By.CSS_SELECTOR,"#_pcmap_list_scroll_container").click()

# 로딩된 데이터 개수 확인
# lis = browser.find_elements(By.CSS_SELECTOR,"li[class^=basicList_item__0T9JD]")
# before_len = len(lis)

# while True:
#     # 맨 아래로 스크롤 내린다.
#     browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.END)

#     # 스크롤 사이 페이지 로딩 시간
#     time.sleep(1)

#     # 스크롤 후 로딩된 데이터 개수 확인
#     lis = browser.find_elements(By.CSS_SELECTOR,"div[class^=basicList_item__0T9JD]")
#     after_len = len(lis)

#     # 로딩된 데이터 개수가 같다면 반복 멈춤
#     if before_len == after_len:
#         break
#     before_len = after_len
    

titles =  browser.find_elements(By.CSS_SELECTOR,'a[class=basicList_link__JLQJf]')
# classification =  browser.find_elements(By.CSS_SELECTOR,'li span[class^=KCMnt]')

titles[0].click()
    

browser.window_handles[0]
#기존 웹페이지 확인
browser.switch_to.window(browser.window_handles[1])
#지정 웹페이지로 이동 함수

print(browser.window_handles)
# a = [x.text for x in titles]

# b = [x.text for x in classification]

# import pandas as pd
# df = pd.DataFrame(zip(a,b))
# print(df)
# # for title in titles:
#     print(title.text)

# for cl in classification:
#     print(cl.text)
    

time.sleep(4)
browser.close()