# 예외처리

# Chapter 57. 예외처리
try:
    print("나누기 전용 계산기입니다")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요: ")))
    nums.append(int(input("두 번째 숫자를 입력하세요: ")))
    nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], int(nums[2])))
except ValueError:
    print("Error, Wrong value.")
except ZeroDivisionError as err:
    print(err)
except:
    print("Unknown Error.")


# Chapter 58. 에러 발생시키기(raise)
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))

    if num1 >= 10 or num2 >= 10:
        raise ValueError # 에러 생성 키워드 raise
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 10 이하의 숫자만 입력하세요.")


# Chapter 59. 사용자 정의 예외처리
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))

    if num1 >= 10 or num2 >= 10:
        raise BigNumberError
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 10 이하의 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다.")
    print(err)
finally:
    print("Thank you for using our calculator.")


