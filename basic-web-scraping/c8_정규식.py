# 정규식 참고 사이트 w3school, python re

import re
# . (ca.e) : 하나의 문자 > care, cafe, case (O) | caffe (X)
# ^ (^de) : 문자열의 시작 > desk, destination (O) | fase (X)
# $ (se&) : 문자열의 끝 > case, base (O) | face (X)
p = re.compile("ca.e") # 정규식 생성
m = p.match("case") # 정규식 체크

def print_match(m):
    if m:
        print(f"m.group(): {m.group()}") # 매칭되면 case 출력, 매치되지 않으면 에러 발생, 일치하는 문자열 반환
        # print(f"m.string: {m.string()}") # 입력받은 문자열 반환
        print(f"m.start(): {m.start()}") # 일치하는 문자열의 시작 index 반환
        print(f"m.end(): {m.end()}") # 일치하는 문자열의 끝 index 반환
        print(f"m.span(): {m.span()}") # 일치하는 문자열의 시작/끝 index 반환

    else:
        print("매칭되지 않음")


# (1) match : 주어진 문자열의 처음부터 일치하는지 확인
m = p.match("careless") 
print_match(m) # care 출력

m = p.match("lesscare") 
print_match(m) # 매칭되지 않음

m = p.match("lesscareless")
print_match(m) # 매칭되지 않음


# (2) search : 주어진 문자열 중에 일치하는 게 있는지 확인
m = p.search("careless") 
print_match(m) # care 출력

m = p.search("lesscare")
print_match(m) # care 출력


# (3) findall : 일치하는 모든 문자열을 리스트 형태로 반환
lst = p.findall("care good careless carepure")
print(f"findall: {lst}") # ['care', 'care', 'care'] 출력