# 함수
# Chapter 32. 함수
def open_accout():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

balance = 0
balance = deposit(balance, 1000)
print(balance)


# Chapter 34. 함수 기본값
def profile(name, age=17, main_lang="python"):
    print("Name: {0}\t Age: {1}\t 주사용언어: {2}".format(name, age, main_lang))


# Chapter 36. 가변인자
def profile(name, age, *language):
    # 가변인자 *language: 고정된 두 매개변수 name, age 이외에 전달되는 모든 인자들은 튜플 형태로 language에 모여짐

    # print()는 끝나면 줄바꿈\n을 함, end는 줄바꿈 대신 쓸 표시 출력
    print("Name: {0}\tAge: {1}\t".format(name, age), end=", ") 
    for lang in language:
        print(lang, end=" ")
    print()

# name = 유재석, age = 20, *language = ("python", "java", "C", "C++", "C#")
profile("유재석", 20, "python", "java", "C", "C++", "C#")
# name = 김태호, age = 25, *language = ("kotlin", "swift", ".", ".", ".")
profile("김태호", 25, "kotlin", "swift", ".", ".", ".")


# Chapter 37. 지역변수 전역변수
gun = 10

def checkpoint(soldiers): # 경계근무
    gun = 20
    gun = gun - soldiers
    print("[inner] left guns: {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[inner] left guns: {0}".format(gun))
    return gun

print("Whole guns: {0}".format(gun))
checkpoint(2)
print("Left guns: {0}".format(gun))
gun=checkpoint_ret(gun, 3)
print("Left guns: {0}".format(gun))