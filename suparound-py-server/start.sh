#!/usr/bin/env bash
set -ex  # 에러 시 중단, 실행 명령 표시

# Chrome 설치
apt-get update
apt-get install -y wget gnupg unzip curl
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt install -y ./google-chrome-stable_current_amd64.deb

# Chrome 경로 출력
which google-chrome || echo "google-chrome not found"
google-chrome --version || echo "chrome version check failed"

# Flask 앱 실행
exec gunicorn wba-schedule:app --bind 0.0.0.0:$PORT

which google-chrome
google-chrome --version