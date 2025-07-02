# 1. Python 3.10 slim 이미지 기반 (가볍고 빠름)
FROM python:3.10-slim

# 2. 시스템 패키지 설치
RUN apt-get update && apt-get install -y \
    wget curl gnupg unzip fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libatk1.0-0 libcups2 libdbus-1-3 libgdk-pixbuf2.0-0 libnspr4 libnss3 libx11-xcb1 \
    libxcomposite1 libxdamage1 libxrandr2 xdg-utils libu2f-udev \
    && rm -rf /var/lib/apt/lists/*

# 3. Chrome 설치
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

# 4. 작업 디렉토리 설정
WORKDIR /app

# 5. 프로젝트 파일 복사
COPY . /app

# 6. 의존성 설치
RUN pip install --upgrade pip && pip install -r requirements.txt

# 7. 포트 설정 (Render가 자동으로 PORT env를 줌)
ENV PORT=8000

# 8. Flask 앱 실행 (Render용)
CMD ["gunicorn", "wba-schedule:app", "--bind", "0.0.0.0:$PORT"]
