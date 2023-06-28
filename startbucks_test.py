from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
import requests
from bs4 import BeautifulSoup

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

df = pd.DataFrame(columns = ['매장명','매장코드','위도','경도','주소','시도','시군구','gps','상세인사말',
                             '오늘날짜','오늘영업일','내일날짜','내일영업일','3일후날짜','3일후영업일',
                             '4일후날짜','4일후영업일','5일후날짜','5일후영업일','6일후날짜','6일후영업일',
                             '7일후날짜','7일후영업일','주차정보','오시는길'])
df_columns = [x for x in df.columns]
regions = finds_present("ul.sido_arae_box li")
ind = 0

for region in regions: 
    time.sleep(1)
    region.find_element(By.CSS_SELECTOR,'a.set_sido_cd_btn').click() #지역선택
    time.sleep(1)
    try:
        find_visible("ul.gugun_arae_box a.set_gugun_cd_btn").click() #전체 선택
        # find_visible("#mCSB_2_container > ul > li:nth-child(4) > a").click() #강북구
        # find_present('#mCSB_2_container > ul > li:nth-child(15) > a').click()#서대문구
        time.sleep(2)
        datas = finds_present("ul.quickSearchResultBoxSidoGugun li")
    except:
        time.sleep(1)
        datas = finds_present("ul.quickSearchResultBoxSidoGugun li")

    for data in datas:
        
        ind = ind + 1
        dnleh = data.get_attribute('data-lat')#위도 
        rudeh = data.get_attribute('data-long')#경도
        zhem = data.get_attribute('data-storecd')#매장코드
        name = data.get_attribute('data-name')#매장명
        addr = data.find_element(By.CSS_SELECTOR,'p').get_attribute('innerText')#주소   
        gps = data.find_element(By.CSS_SELECTOR,'i').get_attribute('class')#gps 아이콘 
        addr = data.find_element(By.CSS_SELECTOR,'p').get_attribute('innerText')#주소
        trial = addr.split(" ")[0] # 시도
        city_county = addr.split(" ")[1] #시군구
        
        
        #mCSB_2_container > ul > li:nth-child(15) > a
        try:
            
            
            data.click() #매장명 클릭
        except:
            browser.find_element(By.CSS_SELECTOR, '#mCSB_3').send_keys(Keys.PAGE_DOWN) #스크롤 다운
            time.sleep(1) #스크롤 내려가는 시간
            data.click() #매장명 클릭

        find_present("a.btn_marker_detail").click()#상세보기 클릭
###########################################################################################################################        
        time.sleep(1)
        detail= find_present('#container > div.shopArea_pop01.isStoreBizViewWrap > section > header > div > p').text #상세페이지 인삿말
        
        
        fir = find_present('dl.date_time_left > dt:nth-child(1)').text
        fir2= find_present('dl.date_time_left > dd:nth-child(2)').text
        sen = find_present('dl.date_time_left > dt:nth-child(3)').text
        sen2= find_present('dl.date_time_left > dd:nth-child(4)').text
        sud = find_present('dl.date_time_left > dt:nth-child(5)').text
        sud2= find_present('dl.date_time_left > dd:nth-child(6)').text
        fod = find_present('dl.date_time_left > dt:nth-child(7)').text
        fod2= find_present('dl.date_time_left > dd:nth-child(8)').text
        
        fir3 = find_present('dl.date_time_right > dt:nth-child(1)').text
        fir4= find_present('dl.date_time_right > dd:nth-child(2)').text
        sen3 = find_present('dl.date_time_right > dt:nth-child(3)').text
        sen4= find_present('dl.date_time_right > dd:nth-child(4)').text
        sun3 = find_present('dl.date_time_right > dt:nth-child(5)').text
        sun4= find_present('dl.date_time_right > dd:nth-child(6)').text
        
        #뷰티블스푸
        html = browser.page_source  
        soup = BeautifulSoup(html, 'html.parser')
        
        for i in range(1,8):
            try:
                if str(soup.select_one(f'div.shopArea_infoWrap > dl:nth-child({i}) > dt').get_text(strip=True)) == "주차정보":#주차정보
                    try:
                        dt_p = soup.select_one(f'div.shopArea_infoWrap > dl:nth-child({i}) > dd').get_text(strip=True)
                    except:
                        continue
                    try:
                        dt_o= soup.select_one(f'div.shopArea_infoWrap > dl:nth-child({i+1}) > dd').get_text(strip=True)  
                    except:
                        break
                    break
                elif i ==7:
                    break
            except:
                for j in range(1,8):
                    try:
                        if str(soup.select_one(f'div.shopArea_infoWrap > dl:nth-child({j}) > dt').get_text(strip=True)) == "오시는길":#오시는길
                            try:
                                dt_o = soup.select_one(f'div.shopArea_infoWrap > dl:nth-child({j}) > dd').get_text(strip=True)                    
                            except:
                                continue   
                    except:
                        break


        df_list = [x for x in df.columns]
        for x in range(1,5):
            if str(soup.select_one(f'div.shopArea_infoWrap > dl:nth-child({x}) > dt').get_text(strip=True)) == "위치 및 시설":
                dt_h = soup.select_one(f'div.shopArea_infoWrap > dl:nth-child({x}) > dd')#위치 및 시설
                break
            else:
                continue
            
        dt_lh = []
        for i in range(10):
            try:
                x = dt_h.select('img')[i]['src']
                dt_lh.append(x.split('/')[-1])
            except:
                break
            #위치시설 태그 추출
        
        for i in dt_lh:
            if i not in df_list:
                df[i] = 0
                df.loc[ind,i] = 2
            else:
                df.loc[ind,i] = 2
            #위치시설 태그 적제
            
        for y in range(1,5):
            if str(soup.select_one(f'div.shopArea_infoWrap > dl:nth-child({y}) > dt').get_text(strip =True))=="서비스":
                dt_s = soup.select_one(f'div.shopArea_infoWrap > dl:nth-child({y}) > dd')#서비스
            else:
                continue
        dt_ls = []
            
        for i in range(10):
            try:
                x = dt_s.select('img')[i]['src']
                dt_ls.append(x.split('/')[-1])
            except:
                break
            #서비스 태그 추출
        
        # print(df_list)
        for i in dt_ls:
            if i not in df_list:
                df[i] = 0
                df.loc[ind,i] = 1
            else:
                df.loc[ind,i] = 1
        # 서비스 부분 데이터 쌓기
                
        find_present('a.isStoreViewClosePop').click()#상세보기 x
    
        find_present('img[alt="close"]').click()#매장정보 끄기
        

        for df_l in df_columns:
            df.loc[ind,'매장명']=name
            df.loc[ind,'매장코드']=zhem
            df.loc[ind,'위도']=dnleh
            df.loc[ind,'경도']=rudeh
            df.loc[ind,'주소']=addr
            df.loc[ind,'시도']=trial
            df.loc[ind,'시군구']=city_county
            df.loc[ind,'gps']=gps
            df.loc[ind,'상세인사말']=detail
            df.loc[ind,'오늘날짜']=fir
            df.loc[ind,'오늘영업일']=fir2
            df.loc[ind,'내일날짜']=sen
            df.loc[ind,'내일영업일']=sen2
            df.loc[ind,'3일후날짜']=sud
            df.loc[ind,'3일후영업일']=sud2
            df.loc[ind,'4일후날짜']=fod
            df.loc[ind,'4일후영업일']=fod2
            df.loc[ind,'5일후날짜']=fir3
            df.loc[ind,'5일후영업일']=fir4
            df.loc[ind,'6일후날짜']=sen3
            df.loc[ind,'6일후영업일']=sen4
            df.loc[ind,'7일후날짜']=sun3
            df.loc[ind,'7일후영업일']=sun4
            try:
                df.loc[ind,'주차정보']=dt_p
            except:
                continue
            try:
                df.loc[ind,'오시는길']=dt_o
            except:
                break
            
    find_present("h3.on a").click() #지역선택    

df = df.fillna(0)    
df.to_csv(r'C:\Users\hyunwoo\Desktop\태블로\df.csv',encoding='utf-8-sig')

print(df)   
