import requests

url = "https://chatgpt.com/c"

# user agent string 검색 >> WhatIsMyBrowser.com >> 현재 내 user-agent 정보를 확인할 수 있는 사이트
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers)
# res.raise_for_status()

with open("gpt.html", "w", encoding="utf8") as f:
    f.write(res.text)


# requests로 정보를 가져올 때 브라우저는 일부 정보를 지워서 응답함
# 헤더에 User-Agent 정보를 실어서 요청하면 올바른 정보를 모두 응답해 줌