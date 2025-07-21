from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

sigungu_numbers = ['720', '200', '290', '710', '140', '230', '170', '260', '110']
sigungu_info = {
    '720': '군위군',
    '200': '남구',
    '290': '달서구',
    '710': '달성군',
    '140': '동구',
    '230': '북구',
    '170': '서구',
    '260': '수성구',
    '110': '중구'
}

hospital_data = []

try:
    url = 'https://www.nhis.or.kr/nhis/healthin/retrieveExmdAdminSearch.do'
    driver.get(url)
    wait = WebDriverWait(driver, 20)
    time.sleep(10)

    # 시도 설정
    select_sido_element = driver.find_element(By.ID, "search_sido")
    select_sido_object = Select(select_sido_element)
    select_sido_object.select_by_value("27")
    time.sleep(7)

    select_sigungu_element = driver.find_element(By.ID, "search_sigungu")
    select_sigungu_object = Select(select_sigungu_element)

    for sigungu_number in sigungu_numbers:
        select_sigungu_object.select_by_value(sigungu_number)
        time.sleep(5)

        # 검진 유형 설정
        if sigungu_number == '720':
            labels = driver.find_elements(By.CSS_SELECTOR, "label.checkbox.col-gap-8")
            labels[6].click()
            labels[7].click()
            labels[9].click()
        time.sleep(1)

        searchBtn = driver.find_element(By.ID, 'btnSearch')
        searchBtn.click()
        time.sleep(5)

        # pagination 돌면서 병원명, 주소 추출
        while True:
            # 페이지 소스 열기
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            # 현재 페이지 위치
            pagination = soup.select_one('div.pagination div.page')
            if not pagination:
                break
            
            current_page = pagination.select_one('strong')
            next_page = None

            if current_page:
                current_page_num = int(current_page.text.strip())
                page_links = pagination.select('a[onclick^="goPage"]')

                hospital_list = soup.select('ul#hospitalList > li')

                for li in hospital_list:
                    # 병원명 추출
                    title_div = li.select_one('button > div.list')
                    title_text = None
                    if title_div:
                        texts = list(title_div.stripped_strings)
                        title_text = texts[1]
                        print('병원명: ', title_text)

                    # 주소 추출
                    address_i = li.select_one('li.section.flex-col.col-gap-8.items-center')
                    address_text = None
                    if address_i:
                        address_text = address_i.get_text(strip=True).strip('"')
                        print('주소: ', address_text)

                    # 전화번호 추출
                    tel_span = li.select_one('a.section > span')
                    tel_text = None
                    if tel_span:
                        tel_text_temp = tel_span.get_text(strip=True).strip('"')
                        tel_text = tel_text_temp[5:]
                        print('연락처: ', tel_text)

                    # 데이터 저장
                    hospital_data.append({'구':sigungu_info[sigungu_number],'병원명': title_text, '병원장': '', '연락처': tel_text, '주소':address_text})

                    # 다음 페이지 찾기
                    for a in page_links:
                        page_num = int(a['title'].strip())
                        if page_num > current_page_num:
                            next_page = a
                            break
                            
                if next_page:
                    next_page_number = next_page['onclick'].split('goPage(')[1].split(')')[0]
                    driver.execute_script(f"goPage({next_page_number});")
                    time.sleep(5)
                else:
                    break

        closeBtn = driver.find_element(By.CLASS_NAME, "ico.x24.ico-close")
        closeBtn.click()    

finally:
    # driver.quit()
    if hospital_data:
        df = pd.DataFrame(hospital_data)
        filename = "안동_구역별_위암대장암유방암_검진병원목록.xlsx"
        df.to_excel(filename, index=False)
        print(f"{filename} 저장 완료, ({len(df)}개 병원)")