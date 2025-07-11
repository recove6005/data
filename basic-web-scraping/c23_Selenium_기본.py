# id 속성값으로 찾기
# find_element(By.ID, "searchBox")
# find_elements(By.ID, "searchBox")

# class 속성값으로 찾기
# find_element(By.CLASS_NAME, "btn")
# find_elements(By.CLASS_NAME, "btn")

# name 속성값으로 찾기
# find_element(By.NAME, "q")
# find_elements(By.NAME, "q")

# 태그명으로 찾기
# find_element(By.TAG_NAME, "button")
# find_elements(By.TAG_NAME, "button")

# <a> 링크 텍스트로 찾기
# find_element(By.LINK_TEXT, "로그인")
# find_elements(By.LINK_TEXT, "로그인")

# <a> 링크 텍스트의 일부분으로 찾기
# find_element(By.PARTIAL_LINK_TEXT, "로그")
# find_elements(By.PARTIAL_LINK_TEXT, "로그")

# CSS 선택자로 찾기
# find_element(By.CSS_SELECTOR, "div.container > button.btn")
# find_elements(By.CSS_SELECTOR, "div.container > button.btn")

# XPath 표현식으로 찾기
# find_element(By.XPATH, "//div[@class='box']//a[1]")
# find_elements(By.XPATH, "//div[@class='box']//a[1]")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36")

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 1. 네이버 이동
browser.get("https://www.naver.com/")
time.sleep(1)

# 2. 로그인 버튼 클릭
login_btn = browser.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW")
login_btn.click()

# 3. id, pw 입력
browser.find_element(By.ID, "id").send_keys("naver_id")
browser.find_element(By.ID, "pw").send_keys("naver_pw")

# 4. 로그인 버튼 클릭
browser.find_element(By.ID, "log.login").click()

# 5. html 정보 출력
print(browser.page_source)

# 6. 브라우저 종료
browser.close() # 현재 탭만 종료
browser.quit() # 전체 브라우저 종료

