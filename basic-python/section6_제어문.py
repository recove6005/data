# 제어문

# Chapter 26. if
weather = input("오늘 날씨 어때요?")
if weather == "비" or weather == "눈":
    print("우산을 챙겨요 !")
elif weather == "미세먼지":
    print("마스크를 챙겨요 !")
else:
    print("준비물 필요 없어요 !")

temp = int(input("기온은 어때요?"))
if temp >= 30:
    print("너무 더워요 !")
elif temp >= 10 and temp < 30:
    print("덥지만 그럭저럭 참을만 해요.")
elif temp < 10 and temp > 5:
    print("서늘하고 시원해요 !")
else: 
    print("너무 추워요, 외투를 챙겨요 !")


# Chapter 27. for
# randrange()
for waiting_no in range(1, 6): # 1 ~ 5
    print("대기 번호: {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))


# Chapter 28. while
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분 되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다.".format(customer, index))
#     index += 1

customer = "토르"
person = "Unknow"
while person != customer:
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되나요?")
    if person == customer:
        print("커피 전달")
    else:
        print("주문 취소")


# Chapter 29. continue, break
absent = [2 ,5] # 결석
no_book = [7] # 책을 깜빡함
for student in range(1, 11): 
    if student in absent:
        continue # 다음 코드들을 실행하지 않고 다음 index로
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와.".format(student))
        break # for문 종료
    print("{0}, 책을 읽어 봐".format(student))


# Chapter 30. 한줄 for문
# 출석 번호가 1 2 3 4, 앞에 100을 붙임
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
print(students)
students = [i.upper() for i in students]
print(students)
