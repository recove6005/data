# pip install lxml

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
webtoons = soup.find_all("a", attrs={"class": "ContentTitle__title_link--xXNfs"})

# soup.title
print(soup.title) # html <title> 태그 출력
print(soup.title.get_text()) # <title> 태그 내부 text 출력

# soup.a
print(soup.a) # 가장 처음 발견되는 <a> 태그 출력
print(soup.a.attrs) # <a>태그가 가진 속성(href, onclick...) 등의 정보를 딕셔너리 형태로 모두 출력
print(soup.a["href"]) # <a>태의 href 속성값 정보 출력

# soup.find
print(soup.find("a", attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload"인 a element를 찾음
print(soup.find(attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload"인 어떤 element를 찾음


# 형제 태그 찾기 
# next_sibling
rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.get_text())
print(rank1.next_sibling) # 태그 사이에 개행 정보(줄바꿈)가 있어서 다음 형제 태그가 출력이 안 될 수 있음
print(rank1.next_sibling.next_sibling) # rank1의 다음 위치의 형제 태그 출력
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())

# previous_sibling
rank2 = rank3.previous_sibling.previous_sibling # 이전 형제 태그를 찾음
print(rank2.a.get_text())

# parent
print(rank1.parent) # rank1의 부모 태그인 ol태그 전체 출력

# find_next_sibling()
rank2 = rank1.find_next_sibling("li") # 다음 li 형제 태그를 찾음
print(rank2.a.get_text())
rank3 = rank2.find_next_sibling("li")
print(rank3.a.get_text())

# find_previous_sibling()
rank2 = rank3.find_previous_sibling("li")
print(rank2.a.get_text())

# fins_next_siblings() 
print(rank1.find_next_siblings("li")) # 모든 li 형제 태그 출력

#
webtoon = soup.find("a", text="독립일기-11화 밥공기 딜레마") # innerText가 "독립일기-11화 밥공기 딜레마"인 a 태그를 찾음
print(webtoon)

# fins_all
cartoos = soup.find_all("a", attrs={"class":"title"})
