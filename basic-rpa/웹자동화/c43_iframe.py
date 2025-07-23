from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors') 
options.add_argument('--allow-running-insecure-content') 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

# iframe 내에 있는 태그는 직접 가져올 수 없음
# frame 전환 후 실행해야 함
driver.switch_to.frame('iframeResult') # 프레임 전환
elem = driver.find_element(By.XPATH, '//*[@id="html"]') 
elem.click()

# 상위 html로 빠져나옴
driver.switch_to.default_content()


time.sleep(5)
driver.quit()

