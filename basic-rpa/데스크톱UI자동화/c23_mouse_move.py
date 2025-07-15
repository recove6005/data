import pyautogui

# 스크린의 절대 좌표로 마우스 이동
# (가로x, 세로y) 위치로 (duration=3)3초 동안 마우스 이동
pyautogui.moveTo(100,100, duration=3)
pyautogui.moveTo(300,300, duration=3)
pyautogui.moveTo(200,100, duration=3)

# 현재 커서가 있는 위치를 기준으로 상대 좌표로 마우스 이동
print(pyautogui.position()) # 현재 마우스 위치 출력
pyautogui.move(100, 100, duration=3)
print(pyautogui.position())
pyautogui.move(200, 150, duration=3)
print(pyautogui.position())

# 마우스 위치 출력하기
p = pyautogui.position()
print(p[0], p[1]) # x, y
print(p.x, p.y) # x, y

