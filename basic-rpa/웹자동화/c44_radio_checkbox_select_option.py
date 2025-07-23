from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors') 
options.add_argument('--allow-running-insecure-content') 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')
# driver.switch_to.frame('iframeResult') # 프레임 전환

# # radio
radio = driver.find_element(By.XPATH, '//*[@id="html"]') 
if radio.is_selected == False: # 라디오 버튼이 선택되어 있지 않으면
    print("선택되어 있지 않으므로 선택하기")
    radio.click()
else: # 라디오 버튼이 선택되어 있다면
    print("선택되어 있으므로 액션 X")

time.sleep(3)


# checkbox
# ...


# select & option
driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select')
driver.switch_to.frame('iframeResult')

# select 내부 원하는 option을 직접 선택 클릭
# option[1], option[2] ...
option_01 = driver.find_element(By.XPATH, '//*[@id="cars"]/option[3]')
option_01.click()

# 텍스트 값을 통해서 option 선택: text()="Audi"
option_02 = driver.find_element(By.XPATH, '//*[@id="cars"]/option[text()="Audi"]')
option_02.click()

# 텍스트 값이 부분 일치하는 option 선택: contains
option_03 = driver.find_element(By.XPATH, '//*[@id="cars"]/option[contains(text(), "Au")]')
option_03.click()
