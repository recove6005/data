# 연산자

# Chapter 9. 연산자
print(1 != 3) # True
print(not(1 != 3)) # False

print((3 > 0) and (3 < 5)) # True
print((3 > 0) % (3 < 5)) # True

print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True

print(5 > 4 > 3) # (5 > 4) and (4 > 3) → True and True → True
print(5 > 4 > 7) # (5 > 4) and (4 > 7) → True and False → False


# Chapter 11. 숫자 처리 함수
print(abs(-5)) # -5 절댓값 처리 → 5
print(pow(4, 2)) # 4^2 → 16
print(max(5, 12, 2)) # 최댓값 12
print(min(5, 12, 2)) # 최솟값 2
print(round(3.14)) # 반올림 3
print(round(4.99)) # 반올림 5

from math import *
print(floor(4.99)) # 내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4


# Cahpter 12. 랜덤함수
from random import *
print(random()) # 0.0 ~ 0.9 사이의 임의의 값 생성
print(random() * 10) # 0.0 ~ 9.0 사이의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 9 사이의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 사이의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 사이의 임의의 값 생성

print(randrange(1, 46)) # 1 ~ 45 사이의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 사이의 임의의 값 생성