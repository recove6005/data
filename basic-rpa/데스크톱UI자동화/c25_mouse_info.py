import pyautogui

pyautogui.mouseInfo() # 마우스 정보창을 띄움

pyautogui.PAUSE = 1 # 모든 동작아 1초씩 sleep 적용
pyautogui.FAILSAFE = False

for i in range(10):
    pyautogui.move(100, 100)
    pyautogui.sleep(1)