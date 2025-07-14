from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import re
import os

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&q=2019%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84")
time.sleep(3)

index = 0

for i in range(3):
    # 스크립트에 의해 html이 변경될 경우(다음 버튼 클릭)
    # 현재 웹페이지 html과 soup를 갱신해 줘야 함
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    next_btn = driver.find_element(By.CSS_SELECTOR, "div.compo-paging > button.btn_next")
    
    div = soup.find("div", attrs={"class":"flipsnap_item", "data-is-active":"true"})
    ul = div.find("ul", attrs={"class":"c-list-basic ty_flow35"})
    images = ul.find_all("div", attrs={"class":"wrap_thumb"})
    
    for image in images:
        index+=1
        print(f"\nimage url[{index}]: {image.a.img["src"]}\n")
        url = image.a.img["src"]

        img_res = requests.get(url, stream=True)
        img_res.raise_for_status()

        with open(f"movie{index}.jpg", "wb") as f:
            f.write(img_res.content)
        
    next_btn.click()

