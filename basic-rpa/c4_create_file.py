# Section2. 엑셀 자동화
# Chapter 4. 파일 만들기

from openpyxl import Worbook

wb = Worbook() # 새 워크북 생성
ws = wb.active # 현재 활성화된 sheet를 가져옴
ws.title = "SampleSheet" # sheet의 이름 변경
wb.save("sample.xlsx") # 파일 저장
wb.close() # 워크북 종료