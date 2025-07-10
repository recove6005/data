from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# driver.get("https://series.naver.com/comic/detail.series?productNo=8826958")
# time.sleep(3)
# html = driver.page_source

# soup = BeautifulSoup(html, "html.parser")
# cartoons = soup.find_all("td", attrs={"class":"subj"})
# title = cartoons[0].div.span.get_text() # 첫번째 화 title 출력

# for cartoon in cartoons:
#     print(cartoon.div.span.get_text())


driver.get("https://comic.naver.com/webtoon/list?titleId=812354&tab=sun")
time.sleep(3)
html = driver.page_source

soup = BeautifulSoup(html, "html.parser")
cartoons = soup.find_all("a", attrs={"class":"EpisodeListList__link--DdClU"})
for cartoon in cartoons:
    title = cartoon.div.next_sibling.p.span.get_text()
    link = "https://comic.naver.com" + cartoon["href"]
    print(title, link)
