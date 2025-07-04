# 문자열 처리

# Chapter 14. 문자열
personal_number = "012345-7891234"

print(f"Gender: {personal_number[7]}")
print(f"Birth Year: {personal_number[0:2]}") # 0 ~ 1
print(f"Birth Month: {personal_number[2:4]}") # 2 ~ 3
print(f"Birth Day: {personal_number[4:6]}") # 4 ~ 5

print(f"Birth Date: {personal_number[:6]}") # 처음부터 ~ 5
print(f"Last 7 Number: {personal_number[7:]}") # 7 ~ 끝까지
print(f"Reverse 7 Number: {personal_number[-7:]}") # 0자리 제외 맨 뒤에서 7번째 문자부터 끝까지


# Chapter 15. 문자열 처리 함수
python = "Python is Amazing Python python"
print(python.lower()) # 문자열 전체 소문자 전환
print(python.upper()) # 문자열 전체 대문자 전환
print(python[0].isupper) # 문자가 대문자인지 > True
print(len(python)) # 문자열 길이 > 17
print(python.replace("Python", "Java")) # 모든 Python 문자열을 "Java" 문자열로 교체

index = python.index("n") 
print(index) # 문자 n이 첫번째로 등장하는 위치 인덱스
index = python.index("n", index+1)
print(index) # 문자 n이 두번째로 등장하는 위치 인덱스
index = python.index("n", index+2)
print(index) # 문자 n이 세번째로 등장하는 위치 인덱스

print(python.find("n")) # 문자 n이 가장 첫번째로 등장하는 위치 인덱스
print(python.find("Java")) # 없는 문자열이므로 -1 반환
print(python.index("Java")) # 없는 문자열이므로 Error 발생

print(python.count("n")) # 문자열에 포함된 문자 'n'의 개수


# Chapter 16. 문자열 포멧
print("I'm %d years old." % 20)
print("I like %s" % "python")
print("Apple is start within %c" % "A")
print("I like %s and %s colors." % ("blue", "red"))

print("I'm {} years old.".format(20))
print("I like {} and {} colors".format("blue", "red"))
print("I like {0} and {1} colors".format("blue", "red"))
print("I like {1} and {0} colors".format("blue", "red"))

print("I'm {age} years old, and I like {color} color.".format(age = 20, color = "red"))
print("I'm {age} years old, and I like {color} color.".format(color = "red", age = 20))

# v3.6 이상
age = 20
color = "red"
print(f"I'm {age} years old, and I like {color} color.")


# Chapter 17. 탈출 문자 \
# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# 큰따옴표 안에 큰따옴표
print("나는 \"릴리\" 입니다.")
print('나는 "릴리" 입니다.')
print('나는 \'릴리\' 입니다.')
print("나는 '릴리' 입니다.")

# \\ : 문장 내에서는 \
print("C:\Users\Nadocoding\Desktop\PythonWorkspace")  # \가 탈출 문자로 인식됨 > \U \N \D \P
print("C:\\Users\\Nadocoding\\Desktop\\PythonWorkspace")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # PineApple > 커서가 문자열 맨 처음으로 이동해 Red를 덮어씌우며 Pine을 작성

# \b : 백스페이스
print("Redd\bApple") # RedApple > 백스페이스 하면서 d를 지움

# \t : 탭
print("Red\tApple") # Red     Apple