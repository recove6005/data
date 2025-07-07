# 입출력

# Chapter 39. 표준입출력
print("Python", "Java", sep=",")

import sys
print("python", "java", file=sys.stdout) # 표준 출력으로 문작이 찍히는 것
print("python", "java", file=sys.stderr) # 표준 에러로 처리

# set 출력 -> 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    # subject는 8개 공간 확보 후 왼쪽 배치, score는 4개 공간 확보 후 오른쪽 배치
    print(subject.ljust(8), str(score).rjust(4), sep=':') 

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    # 3만큼 공간 확보 후남은 공간만큼 0으로 채움
    print("대기번호: " + str(num).zfill(3))

answer = input("Input any value: ")
print("The value is '{0}'.".format(answer))
print("The Value Type: {0}".format(type(answer)))


# Chapter 40. 다양한 출력 포멧
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되(>), 총 10자리 공간을 확보(10)
print("{0:>10}".format(500))

# 양수일 땐 +로 표시, 음수일 땐 -로 표시, 오른쪽 정렬(>)
# 형식지정자(format specifier): + -> +,- 부호 항상 표시
# 형식지정자(format specifier): - -> 부호는 음수만, 양수는 공백으로 표시
print("{0:>+10}".format(500))
print("{0:>+10}".format(-500))

# 왼쪽 정렬하고(<), 빈칸을 _로 채움
print("{0:_<+10}".format(500))
print("{0:_<10}".format(500))

# 3자릿수 마다 콤마 찍기
print("{0:,}".format(10000000000))

# 3자릿수 마다 콤마찍고, +- 부호 붙이기
print("{0:+,}".format(-1000000000))

# 3자릿수 마다 콤마 찍기, 부호 표시, 자릴수 확보, 빈칸은 ^로 채우기
print("{0:^<+30}".format(1000000000000))
print("{0:^<+30,}".format(1000000000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점 특정 자리수까지만 표시 (소수점 3번째 자리에서 반올림)
print("{0:.2f}".format(5/3))


# Chapter 41. 파일입출력
# r: 읽기
# w: 새로 쓰기
# a: 이어 쓰기
# x: 파일이 없을 경우에만 생성, 파일이 이미 있으면 에러
# r+: 읽고, 이어 쓰기 가능
# w+: 새로 쓰고, 읽기 가능
# a+: 이어 쓰고, 읽기 가능
# 바이너리 값은 b 문자를 붙임

# w, print()
score_file = open("score.txt", "w", encoding="utf8")
print("수학: 0", file=score_file) # score.txt 파일에 print
print("영어: 50", file=score_file) # score.txt 파일에 print
score_file.close()

# a, write()
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학: 80")
score_file.write("\n코딩: 100")
score_file.close() # 버퍼에 있는 내용을 파일로 완전히 저장(flush)하고, 파일을 안전하게 닫음

# r, read()
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

# r, readline()
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline() 
    if not line: # 더 이상 읽을 줄이 없으면 readline()은 빈 문자열을 반환
        break
    print(line)
score_file.close()

# if not 조건문: falsy값 체크
# None(null)
# False
# 0, 0.0 (숫자형 0)
# "" (빈 문자열)
# [] (빈 리스트)
# {} (빈 딕셔너리)
# set() (빈 세트)
# () (빈 튜플)

# r, readlines() 
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # 한줄씩 읽고 list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()


# Chapter 42. pickle
import pickle

# pickle 쓰기, wb
profile_file = open("profile.pickle", "wb")
profile = {"이름":"박명수", "나이": 30, "취미":["축구", "골프", "코딩"]}
pickle.dump(profile, profile_file) # profile에 있는 값 정보를 file에 저장
profile_file.close()

# pickle 읽기, rb
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file의 값을 불러오기
print("pickle read value: {0}".format(profile))
profile_file.close()


# Chapter 43. with
import pickle

# pickle 파일의 변수를 한번에 읽고 쓰기
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("I'm studing python.")


