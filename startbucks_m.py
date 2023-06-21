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

# expected_conditions.presence_of_element_located((By. ,""))	로딩된 페이지에 조건 요소가 있는지 확인
# expected_conditions.visibility_of_element_located((By. ,""))	로딩된 페이지에 조건 요소가 보이는지 확인
# expected_conditions.presence_of_all_elements_located((By. ,""))	로딩된 페이지가 조건 요소 중 하나라도 있는지 확인
# expected_conditions.element_to_be_clickable((By. ,""))	조건 요소가 클릭 가능한지 확인


browser = webdriver.Chrome()
wait =WebDriverWait(browser, 10)

def find_present(css):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))

def finds_present(css):
    find_present(css)
    return browser.find_elements(By.CSS_SELECTOR,css)

def find_visible(css):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))

def finds_visible(css):
    find_visible(css)
    return chrome.find_elements(By.CSS_SELECTOR,css)
# browser.get("https://www.naver.com/") # 사이트 접속
browser.get("https://www.starbucks.co.kr/store/store_map.do?disp=locale")

# find_present("a.set_sido_cd_btn").click() #서울 선택

df = pd.DataFrame(columns = ['매장명','매장코드','위도','경도','주소'])
regions = finds_present("ul.sido_arae_box li")
ind = 0

for region in regions: 
    time.sleep(2)
    region.find_element(By.CSS_SELECTOR,'a.set_sido_cd_btn').click() #지역선택
    time.sleep(2)
    try:
        find_visible("ul.gugun_arae_box a.set_gugun_cd_btn").click() #전체 선택
    except:
        print('종료되었습니다.')
        break
    time.sleep(2)
    datas = finds_present("ul.quickSearchResultBoxSidoGugun li")
    
    for data in datas:
        ind = ind + 1
        dnleh = data.get_attribute('data-lat')#위도 
        rudeh = data.get_attribute('data-long')#경도
        zhem = data.get_attribute('data-storecd')#매장코드
        name = data.get_attribute('data-name')#매장명
        addr = data.find_element(By.CSS_SELECTOR,'p').get_attribute('innerText')#주소   
        
        
        df.loc[ind]=[name,zhem,dnleh,rudeh,addr]
    
    find_present("h3.on a").click() #지역선택    

    
df.to_csv(r'C:\Users\hyunwoo\Desktop\태블로\df.csv',encoding='utf-8-sig')

print(df)   



#     print(data.get_attribute('data-lat'))#위도 
#     print(data.get_attribute('data-long'))#경도
#     print(data.get_attribute('data-storecd'))#매장코드
#     print(data.get_attribute('data-name'))#매장명

    
    # print(data.find_elements(By.CSS_SELECTOR,'p')[0].text)#주소   
    
    # data.click() #매장명 클릭
    # find_present("a.btn_marker_detail").click()#상세보기 클릭
    # find_present('a.isStoreViewClosePop').click()
    # find_present('img[alt="close"]').click()
    
    #storeMap > div:nth-child(4) > div > div:nth-child(6) > div:nth-child(604) > img
    #storeMap > div:nth-child(4) > div > div:nth-child(6) > div:nth-child(604) > img
    #storeMap > div:nth-child(4) > div > div:nth-child(6) > div:nth-child(18) > img
    # print(browser.find_element(By.CSS_SELECTOR,"ul.quickSearchResultBoxSidoGugun li").get_attribute('data-lat'))#위도   
    # print(browser.find_element(By.CSS_SELECTOR,"ul.quickSearchResultBoxSidoGugun li").get_attribute('data-long'))#경도
    # print(browser.find_element(By.CSS_SELECTOR,"ul.quickSearchResultBoxSidoGugun li").get_attribute('data-storecd'))#매장코드

    # 맨 아래로 스크롤 내린다.
    
    # 스크롤 사이 페이지 로딩 시간
    


# data.click() #매장명 클릭
# find_present("a.btn_marker_detail").click()#상세보기 클릭
# time.sleep(2)

# titles =  browser.find_elements(By.CSS_SELECTOR,'ul.quickSearchResultBoxSidoGugun li strong')

# # print(titles[0].text)
# # addrs =  browser.find_elements(By.CSS_SELECTOR,'ul.quickSearchResultBoxSidoGugun li p')
# # print(addrs[0].text)
# titles[0].click()

# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.btn_marker_detail'))) #딜레이
# browser.find_element(By.CSS_SELECTOR,"a.btn_marker_detail").click()
# time.sleep(2)


#storeMap > div:nth-child(4) > div > div:nth-child(6) > div:nth-child(604) > div:nth-child(2) > div > article > div > div.cont_wrap > a
    
# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.set_gugun_cd_btn'))) #딜레이
# browser.find_element(By.CSS_SELECTOR,"a.set_gugun_cd_btn").click()