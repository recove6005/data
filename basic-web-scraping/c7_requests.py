# pip install requests
import requests

res = requests.get("https://chatgpt.com/c") 
print("응답코드: ", res.status_code) # 403 권한없음 

res = requests.get("https://naver.com") # url 접속 후 정보를 응답받음
print("응답코드: ", res.status_code) # 200 정상, 

if res.status_code == requests.codes.ok:
    print("응답 정상")
else:
    print("Error: ", res.status_code)

# >> 응답페이지에 대한 권한이 있는지 없는지, 서버에 문제는 없는지 등을 확인할 때

res = requests.get("http://google.com")
res.raise_for_status()
print(len(res.text))
print(res.text) # 실제 html 텍스트

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)