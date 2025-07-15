import pyautogui
pyautogui.sleep(3) # 3초 대기

pyautogui.click(1705, 1059, duration=1) # 1초 동안 (x, y) 좌표로 이동 후 클릭 실행

pyautogui.mouseDown() # 마우스 버튼을 누름
pyautogui.mouseUp() # 마우스 버튼에서 손을 뗌

pyautogui.doubleClick() # 더블 클릭
pyautogui.click(clicks=2) # 2번 클릭
pyautogui.click(clicks=500) # 500번 클릭

# 드래그
pyautogui.moveTo(100, 100)
pyautogui.mouseDown()
pyautogui.moveTo(200, 300)
pyautogui.mouseUp()
pyautogui.drag(100, 0, duration=0.25)
pyautogui.dragTo(1514, 349, duration=0.25)

pyautogui.sleep(3)
pyautogui.rightClick()
pyautogui.middleClick()

pyautogui.scroll(300) # 양수: 위로 스크롤, 음수: 아래로 스크롤

