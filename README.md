# SetupBox
Open source cloud storage service.

# How to run server
1. git clone .../SetupBox.git
2. pip install virtualenv
3. virtualenv venv
4. source venv/bin/activate
4. pip install -r requirements.txt
5. python SetupBox.py

# 한글 주석
-*- coding: utf-8 -*-
한글 주석을 달고 싶으면 이 코드를 주석으로 맨 위에 삽입하세요!

## 터미널에서 인증 테스트
1. pip install httpie (위에서 requirements 를 설치했으면 이미 되 있음)
2. http -a <email:password> <URL> 입력할 것 
3. 예를 들어 http -a maxtortime@gmail.com:123456 127.0.0.1:5000/authTest 라고 입력하면
4. LOGIN GOOD 이라 뜨면 정상
