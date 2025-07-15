import sys
print(sys.executable)

import requests
from openpyxl import Workbook
from openpyxl.drawing.image import Image
wb = Workbook()
ws = wb.active

img_url = "http://www.bhc.co.kr/upload/bhc/menu/%EB%BF%8C%EB%A7%81%ED%81%B4_%ED%95%9C%EB%A7%88%EB%A6%AC_410x271.jpg"
response = requests.get(img_url)
with open("bhc_chicken.jpg", "wb") as f:
    f.write(response.content)

img = Image("bhc_chicken.jpg")
ws.add_image(img, "C3") # C3 위치에 img.png 파일의 이미지를 삽입

wb.save("sample_image.xlsx")