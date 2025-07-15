import pyautogui

fw = pyautogui.getActiveWindow() # 현재 활성화된 창
print(fw.title) # 창 제목 정보
print(fw.size) # 창 크기 정보 (width, height)
print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표 정보
pyautogui.click(fw.left + 25, fw.top + 20)

for w in pyautogui.getAllWindows():
    print(w) # 모든 윈도우 가져오기

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)

# 현재 활성화가 되어있지 않다면
if w.isActive == False:
    w.activate() # 활성화 (맨 앞으로 가져옴)

# 현재 최대화가 되어있지 않다면
if w.isMaximized == False: 
    w.maximize() # 최대화

if w.isMinimized == False:
    w.minimize() # 최소화

pyautogui.sleep(1)
w.restore() # 화면 원복
w.close() # 윈도우 닫기
