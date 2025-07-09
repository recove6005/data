# 모듈과 패키지
# Chapter 62. 모듈 
import theater_module
import travel.vietnam
theater_module.price(3) # 3명 영화 관람
theater_module.price_morning(4)
theater_module.price_soldier(2)

import theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(2)

from theater_module import *
# from random import *
price(3)
price_morning(4)
price_soldier(2)

# 모듈의 특정 함수만 import하기
from theater_module import price, price_morning
price(5)
price_morning(3)
# price_soldier(7) > Error

from theater_module import price_soldier as sp
sp(5)


# Chapter 63. 패키지
import travel.thailand
# import travel.thailand.ThailandPackage # 오류
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()


# Chapter 64. __all__
from travel import * # Err, 정의되지 않음 -> __init__.py의 __all__ 변수에 패키지 각 파일의 공개 설정 필요
trip_to_second = travel.vietnam.VietnamPackage()
trip_to_second.detail()


# Chapter 65. 모듈 직접 실행
from travel import *

