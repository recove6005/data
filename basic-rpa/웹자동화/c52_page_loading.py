from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors') 
options.add_argument('--allow-running-insecure-content') 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('https://flight.naver.com/flights/')

# 날짜 선택
driver.find_element(By.LINK_TEXT, '가는날 선택').click()
driver.find_element(By.LINK_TEXT, '30')[0].click() # 가는 날 클릭
driver.find_element(By.LINK_TEXT, '5')[1].click() # 오는 날 클릭

# 제주도 클릭
driver.find_element(By.XPATH, '//*@id="recommendationList"/ul/li[1]').click()

# 항공권 검색 클릭
driver.find_element(By.LINK_TEXT, '항공권 검색').click()


# 첫 번째 결과 출력
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

try: 
    result_elem = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(By.XPATH, '//*[@id="content"]/div[2]/div/div[4]/ul/li[1]'))
    print(result_elem.text) 
except:
    print('Error')

time.sleep(3)
driver.quit()