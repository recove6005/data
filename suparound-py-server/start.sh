#!/usr/bin/env bash

# Chrome 설치
apt-get update
apt-get install -y wget gnupg unzip curl
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt install -y ./google-chrome-stable_current_amd64.deb

# Flask 앱 실행
exec gunicorn wba-schedule:app --bind 0.0.0.0:$PORT

which google-chrome
google-chrome --version