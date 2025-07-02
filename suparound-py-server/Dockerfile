FROM python:3.13-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    unzip \
    curl \
    gnupg \
    ca-certificates \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    xdg-utils \
    libvulkan1 && rm -rf /var/lib/apt/lists/*


# 구글 크롬 설치
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb || apt-get -f install -y && \
    rm google-chrome-stable_current_amd64.deb

# python 패키지 설치
RUN pip install --no-cache-dir selenium chromedriver-autoinstaller flask gunicorn beautifulsoup4

WORKDIR /app
COPY . /app

CMD ["gunicorn", "wba-schedule:app", "--bind", "0.0.0.0:5000"]
