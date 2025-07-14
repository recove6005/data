# pip install selenium webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless') # 브라우저를 띄우지 않음
options.add_argument('--no-sandbox') # 샌드박스(크롬 악성코드 실행을 막는 보안 프로세스) 기능을 끔
options.add_argument('--disable-dev-shm-usage') # /dev/shm(리눅스 공유 메모리 영역, 제한적 용량이 크롤링에 문제될 수 있음) 대신 디스크 기반 임시 저장공간을 사용
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://comic.naver.com/webtoon/weekday.nhn")
time.sleep(3)
html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

# 전체 웹툰 제목 출력
cartoons = soup.find_all("a", attrs={"class":"ContentTitle__title_area--x24vt"}) # 리스트 형태로 반환
for cartoon in cartoons:
    print(cartoon.get_text())

