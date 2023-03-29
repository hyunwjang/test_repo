import os
import chromedriver_autoinstaller as AutoChrome

chrome_ver = AutoChrome.get_chrome_version().split('.')[0] # 현재 버전의 앞 두숫자
current_list = os.listdir(os.getcwd()) 			#현재 디렉토리 내 파일/폴더의 리스트
print(chrome_ver)
print(current_list)
    
if not chrome_ver in current_list:				# 버전명으로 된 폴더가 있는지 확인.
    print("크롬드라이버 다운로드 실행")
    AutoChrome.install(True)
    print("크롬드라이버 다운로드 완료")
else: print("크롬드라이버 버전이 최신입니다.")