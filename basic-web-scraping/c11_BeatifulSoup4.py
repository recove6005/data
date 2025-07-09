# pip install lxml

import requests
from bs4 import BeautifulSoup

url ="https://www.naver.com/"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

print(soup.title) # html <title> 태그 출력
print(soup.title.get_text()) # <title> 태그 내부 text 출력

print(soup.a) # 가장 처음 발견되는 <a> 태그 출력
print(soup.a.attrs) # <a>태그가 가진 속성(href, onclick...) 등의 정보를 딕셔너리 형태로 모두 출력
print(soup.a["href"]) # <a>태의 href 속성값 정보 출력

a1 = soup.find("a", attrs={"class":"link_pay"}) # class 속성값으로 <a>태그 객체를 찾음
print(a1)
