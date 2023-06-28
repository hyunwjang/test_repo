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

df = pd.DataFrame(columns = ['매장명','매장코드','위도','경도','주소','시도','시군구','gps','상세인사말',
                             '오늘날짜','오늘영업일','내일날짜','내일영업일','3일후날짜','3일후영업일',
                             '4일후날짜','4일후영업일','5일후날짜','5일후영업일','6일후날짜','6일후영업일','7일후날짜','7일후영업일'])
regions = finds_present("ul.sido_arae_box li") # 지역별 

ind = 0

for region in regions: 
    time.sleep(1)
    region.find_element(By.CSS_SELECTOR,'a.set_sido_cd_btn').click() #지역선택
    time.sleep(1)
    try:
        find_visible("ul.gugun_arae_box a.set_gugun_cd_btn").click() #전체 선택
    except:
        print('종료되었습니다.')
        break
    time.sleep(2)
    datas = finds_present("ul.quickSearchResultBoxSidoGugun li")#지점별
    
    for data in datas: #지점별
        ind = ind + 1 # 총 인덱스 수
        dnleh = data.get_attribute('data-lat')#위도 
        rudeh = data.get_attribute('data-long')#경도
        zhem = data.get_attribute('data-storecd')#매장코드
        name = data.get_attribute('data-name')#매장명
        gps = data.find_element(By.CSS_SELECTOR,'i').get_attribute('class')#gps 아이콘 
        addr = data.find_element(By.CSS_SELECTOR,'p').get_attribute('innerText')#주소
        trial = addr.split(" ")[0] # 시도
        city_county = addr.split(" ")[1] #시군구
        
    
        try:
            data.click() #매장명 클릭
        except:
            browser.find_element(By.CSS_SELECTOR, '#mCSB_3').send_keys(Keys.PAGE_DOWN) #스크롤 다운
            time.sleep(1) #스크롤 내려가는 시간
            data.click() #매장명 클릭
        
        
        
        find_present("a.btn_marker_detail").click()#상세보기 클릭
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
    
        # print(fir,fir2,sen,sen2,sud,sud2,fod,fod2,fir3,fir4,sen3,sen4,sun3,sun4)
        
        find_present('a.isStoreViewClosePop').click()#상세보기 x
    
        find_present('img[alt="close"]').click()#매장정보 끄기
        
        
        df.loc[ind]=[name, zhem, dnleh, rudeh, addr, trial, city_county, gps, detail,
                     fir,fir2,sen,sen2,sud,sud2,fod,fod2,fir3,fir4,sen3,sen4,sun3,sun4]
    
    find_present("h3.on a").click() #지역선택    

    
df.to_csv(r'C:\Users\hyunwoo\Desktop\태블로\df.csv',encoding='utf-8-sig')

print(df)   

