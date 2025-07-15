import pyautogui

# 스크린샷
img = pyautogui.screenshot()
img.save("screenshot.png") # 스크린샷 이미지를 파일로 저장
pixel = pyautogui.pixel(28, 18)
print(pixel)
print(pyautogui.pixelMatchesColor(28, 18, (34, 167, 242)))


# 이미지 처리
file_menu = pyautogui.locateOnScreen("file_menu.png")
print(file_menu)
pyautogui.click(file_menu) # 이미지에 해당하는 곳으로 마우스 이동 후 클릭

trash_icon = pyautogui.locateOnScreen("trash_icon.png")
print(trash_icon)
pyautogui.click(trash_icon)

screen = pyautogui.locateOnScreen("screenshot.png")
print(screen)

# 3개 이상의 체크박스 클릭하기
for i in pyautogui.locateAllOnScreen("checkbox.png"):
    print(i)
    pyautogui.click(i, duration=0.25)
