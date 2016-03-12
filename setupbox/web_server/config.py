# -*- coding: utf-8 -*-
import sys
# for korean character

reload(sys)
sys.setdefaultencoding('utf-8')

DEBUG = True # flask Debugging mode

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
# Please change your own email address and password
MAIL_USERNAME = 'setupboxtest@gmail.com'
MAIL_PASSWORD = 'tptdjqqkrtm'

# Enable protection agains *Cross-site Request Forgery (CSRF)*
WTF_CSRF_ENABLED = True
CSRF_ENABLED = True
CSRF_SESSION_KEY = "9f5bae1bec912adc81e6b7f95e7253fb"

# Database
SQLALCHEMY_DATABASE_URI = "sqlite:///setupbox.db"
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'super-secret'

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.

THREADS_PER_PAGE = 2

SECURITY_REGISTERABLE = True
SECURITY_CONFIRMABLE = False
SECURITY_POST_LOGIN_VIEW = '/explorer'
SECURITY_SEND_REGISTER_EMAIL = False  # 회원가입 인증 메일 보내기 기능 켜기/끄기
SECURITY_PASSWORD_HASH = 'bcrypt'  # 비밀번호 암호화 Hash algorithm  설정
SECURITY_PASSWORD_SALT = '$2b$12$DQdhlb3XSdY5fHIWEzb/Mu'
SECURITY_RECOVERABLE = True  # 비밀번호 초기화 기능 켜기/끄기
SECURITY_CHANGEABLE = True # 비밀번호 바꾸기 기능 켜기/끄기
