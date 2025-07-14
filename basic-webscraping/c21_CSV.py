from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import csv

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
time.sleep(3)

csv_filename = "시가총액1-200.csv"
f = open(csv_filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

for page in range(1, 5):
    driver.get(f"https://finance.naver.com/sise/sise_market_sum.naver?&page={page}")
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")

        if len(columns) <= 1: continue
        
        data = [column.get_text().strip() for column in columns]
        print(data)
        writer.writerow(data)

