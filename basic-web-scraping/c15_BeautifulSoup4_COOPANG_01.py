from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import re

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&page=1")
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# 모든 상품 제목 출력
items = soup.find_all("li", attrs={"class":re.compile("^ProductUnit")})
# print(items[0].a.figure.next_sibling.div.next_sibling.get_text())
for item in items:
    print(item.a.figure.next_sibling.div.next_sibling.get_text())


