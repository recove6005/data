from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors') 
options.add_argument('--allow-running-insecure-content') 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('https://shopping.naver.com/home/p/index.nhn')

# '무선마우스' 입력
search = driver.find_element(By.XPATH, '//*[@id="autocompleteWrapper"]/input[1]')
search.send_keys('무선마우스')

# 검색 버튼 클릭
driver.find_element(By.XPATH, '//*[@id="autocompleteWrapper"]/a[2]').click() # 검색 버튼 클릭
search.send_keys(Keys.ENTER) # 키보드 Enter 처리

# 스크롤
# 지정한 위치(모니터 해상도 가장 아래)로 스크롤 내리기
driver.execute_script('window.scrollTo(0, 1080)') # 1920 * 1080 (모니터 해상도에서)
driver.execute_script('window.scrollTo(0. 2080)')

# 화면 가장 아래로 스크롤 내리기
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

# 동적 페이지에서 마지막까지 스크롤 내리기
interval = 2
prev_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)') # 스크롤을 화면 가장 아래로 내림
    time.sleep(interval) # 페이지 로딩 대기(2s)
    curr_height = driver.execute_script('return document.body.scrollHeight')
    
    if curr_height == prev_height: 
        break # 직전 높이와 같거나 높이 변화가 없으면 반복문 탈출

    prev_height = curr_height

# 맨 위로 올리기
driver.execute_script('window.scrollTo(0, 0)')

# 특정 영역 스크롤
from selenium.webdriver.common.action_chains import ActionChains
elem = driver.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[61]')

# 방법 1: ActionChain
actions = ActionChains(driver)
actions.move_to_element(elem).perform()

# 방법 2: 좌표 정보 이용
xy = elem.location_once_scrolled_into_view
print("type: ", type(xy)) # dict
print("value: ", xy)

elem.click()

time.sleep(3)
driver.quit()

