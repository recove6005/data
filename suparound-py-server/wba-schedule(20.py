#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/wba-schedule', methods=['GET'])
def get_wba_schedule():
    # ✅ Chrome 옵션 설정
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument("window-size=1920x1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(options=options)

    url = 'https://www.wbaboxing.com/wba-fights-schedule#'
    driver.get(url)

    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    schedule_section = soup.select('section.post-content-text div.world')

    titles = []
    player1Images = []
    player2Images = []
    player1Names = []
    player2Names = []
    player1Countries = []
    player2Countries = []

    if schedule_section:
        for fight in schedule_section:
            # 제목, 날짜, 장소 추출
            title_section = fight.select_one('td.bg-white.custom-widget-header')
            if(title_section):
                title = title_section.select_one('h4').text.strip() if title_section.select_one('h4') else 'No Title'

                if "FLYWEIGHT" not in title in title : continue

                details = title_section.get_text(separator=' ').strip()
                print(f"Title: {title}")
                print(f"Details: {details}")
                titles.append(details)

            # 이미지 추출
            images = fight.select('td.col-md-4.text-center img')
            if images:
                first_image_url = images[0]['src'] if len(images) > 0 else 'No Image'
                second_image_url = images[2]['src'] if len(images) > 2 else 'No Image'
                print(f"First Image URL: {first_image_url}")
                print(f"Second Image URL: {second_image_url}")
                player1Images.append(first_image_url)
                player2Images.append(second_image_url)


            # 선수 이름 추출
            names = fight.select('tr:nth-child(3) td.text-center h4')
            if names:
                player_one_name = ' '.join(names[0].text.split()).strip() # if len(names) > 0 else 'No Mame'
                player_two_name = ' '.join(names[1].text.split()).strip() # if len(names) > 2 else 'No Name'
                player1Names.append(player_one_name)
                player2Names.append(player_two_name)
                print(player1Names)

            # 국적 추철
            countries = fight.select('tr:nth-child(4) td.text-center span')
            if countries:
                player_one_country = countries[0].text.strip() # if len(countries) > 0 else 'No Country'
                player_two_country = countries[2].text.strip() # if len(countries) > 2 else 'No Country'
                print(f"Player 1 Country: {player_one_country}")
                print(f"Player 2 Country: {player_two_country}")
                player1Countries.append(player_one_country)
                player2Countries.append(player_two_country)

            print("-" * 50)

    driver.quit()

    jsonData = []
    for index, item in enumerate(titles) :
        jsonData.append({
            'title': titles[index],
            'playerOneName': player1Names[index],
            'playerTwoName': player2Names[index],
            'playerOneCountry': player1Countries[index],
            'playerTwoCountry': player2Countries[index]
        })

    print(jsonData)

    return jsonData

if __name__ == "__main__": 
    app.run(debug=True)


