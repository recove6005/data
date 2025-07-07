# 자료구조

# Chapter 20. 리스트
# 치하철 칸 별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway.index("조세호")) # 1

subway.append("하하") # 마지막 배열에 하하 삽입
print(subway) # ['유재석', '조세호', '박명수', '하하']

subway.insert(1, "정형돈") # 1 인덱스 위치에 정형돈 삽입
print(subway) # ['유재석', '정형돈', '조세호', '박명수', '하하']

print(subway.pop()) # 맨 뒤에 있는 사람을 한 명 꺼냄 > 하하
print(subway)  # ['유재석', '정형돈', '조세호', '박명수']

print(subway.pop()) # 맨 뒤에 있는 사람을 한 명 꺼냄 > 박명수
print(subway) # ['유재석', '정형돈', '조세호']

print(subway.pop()) # 맨 뒤에 있는 사람을 한 명 꺼냄 > 조세호
print(subway) # ['유재석', '정형돈']

# 같은 이름의 사람이 몇 명 있는지 
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬
num_list = [5, 2, 4, 3, 1]
num_list.sort() # 오름차순 정렬
print(num_list) 

# 거꾸로 정렬
num_list.reverse()  
print(num_list) # [5, 4, 3, 2, 1]

# 배열 비우기
num_list.clear()
print(num_list) # []

# 다양한 자료형 함께 삽입
mix_list = ["조세호", 20, True]
print(mix_list) # ['조세호', 20, True]

# 리스트 확장
num_list.extend(mix_list)
print(num_list)


# Chapter 21. 사전
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3]) # 유재석
print(cabinet[100]) # 김태호
print(cabinet.get(3)) # 유재석
print(cabinet[5]) # Error 발생
print(cabinet.get(5)) # None > 다음 코드 진행
print(cabinet.get(5, "사용 가능")) # 5 키값이 cabinet에 없을 경우 "사용 가능" 문자열 반환
print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet) # {'A-3': '유재석', 'B-100': '김태호'}
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet) # {'A-3': '유재석', 'B-100': '김태호', 'C-20': 조세호}

# 간 손님
del cabinet["A-3"] # 'A-3' 키, 값 삭제
print(cabinet) # {'B-100': '김태호', 'C-20': 조세호}

# key 들만 출력
print(cabinet.keys()) # dict_keys(['B-100', 'C-20'])

# value 들만 출력
print(cabinet.values()) # dict_values(['김태호', '조세호'])

# key, value 쌍으로 출력
print(cabinet.items()) # dict_items([('B-100', '김태호'), ('C-20', '조세호')])

# 목욕탕 폐점
cabinet.clear()
print(cabinet) # {}


# Chapter 22. 튜플(tuple)
menu = ("돈까스", "치즈까스")
print(menu[0]) # 돈까스
print(menu[1]) # 치즈까스

menu.add("생선까스") # Error: 'tuple' object has no attribute 'add'

(name, age , hobby) = ("김종국", 20, "치즈까스")
print(name, age, hobby) # 김종국 20 치즈까스


# Chapter 23. 세트(set)
# 중복X, 순서X
my_set = {1,2,3,3,3}
print(my_set) # {1, 2, 3}

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python) # {'유재석'}
print(java.intersection(python)) # {'유재석'}

# 합집합 (java도 할 수 있거나 python도 할 수 있는 개발자)
print(java | python) # {'유재석', '김태호', '양세형', '박명수'}
print(java.union(python))

# 차집합 (java를 할 수 있지만 python은 할 수 없는 개발자)
print(java - python) # {'김태호', '양세형'}
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python) # {'유재석', '박명수', '김태호'}

# java를 잊음
java.remove("김태호")
print(java) # {'유재석', '양세형'}


# Chapter 24. 자료구조의 변경
menu = {"coffee", "milk", "juice"}
print(menu, type(menu)) # {'juice', 'milk', 'coffee'} <class, 'set'>

menu = list(menu)
print(menu, type(menu)) # ['juice', 'milk', 'coffee'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu)) # ('juice', 'milk', 'coffee') <class 'tuple'>