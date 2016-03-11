# -*- coding: utf-8 -*-
import sys,os

DEBUG = True # flask Debugging mode

# Enable protection agains *Cross-site Request Forgery (CSRF)*
WTF_CSRF_ENABLED = True
CSRF_ENABLED = True
CSRF_SESSION_KEY = "9f5bae1bec912adc81e6b7f95e7253fb"

# for korean character
reload(sys)
sys.setdefaultencoding('utf-8')

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

# flask-security 메시지 override
SECURITY_MSG_EMAIL_NOT_PROVIDED =('이메일을 입력해주세요.', 'error')
SECURITY_MSG_UNAUTHORIZED = ('당신은 이 페이지에 접근할 권한이 없습니다.', 'error')
SECURITY_MSG_CONFIRM_REGISTRATION = ('감사합니다. 인증 절차에 관한 안내가 %(email)로 보내졌습니다.', 'success')
SECURITY_MSG_EMAIL_CONFIRMED = ('감사합니다 당신의 이메일이 인증되었습니다.', 'success')
SECURITY_MSG_ALREADY_CONFIRMED= ('당신의 이메일은 이미 인증되었습니다.', 'info')
SECURITY_MSG_INVALID_CONFIRMATION_TOKEN = ('잘못된 인증 토큰입니다.', 'error')
SECURITY_MSG_EMAIL_ALREADY_ASSOCIATED = ('%(email)이 이미 당신에 계정에 연관되어 있습니다.', 'error')
SECURITY_MSG_PASSWORD_MISMATCH = ('비밀번호가 서로 일치하지 않습니다', 'error')
SECURITY_MSG_RETYPE_PASSWORD_MISMATCH = ('비밀번호가 서로 일치하지 않습니다.', 'error')
SECURITY_MSG_INVALID_REDIRECT = ('도메인 바깥으로의 이동은 금지되었습니다.', 'error')
SECURITY_MSG_PASSWORD_RESET_REQUEST = ('비밀번호 초기화에 대한 안내가 %(email)로 보내졌습니다', 'info')
SECURITY_MSG_PASSWORD_RESET_EXPIRED = ('%(within) 내에 비밀번호를 교체하지 않으셔서, '
                                       '새로운 안내가 %(email)로 보내졌습니다..', 'error')
SECURITY_MSG_INVALID_RESET_PASSWORD_TOKEN = ('잘못된 비밀번호 초기화 토큰입니다..', 'error')
SECURITY_MSG_CONFIRMATION_REQUIRED = ('이메일 인증이 필요합니다.', 'error')
SECURITY_MSG_CONFIRMATION_REQUEST = ('감사합니다. 인증 절차에 관한 안내가 %(email)로 보내졌습니다.', 'info')
SECURITY_MSG_CONFIRMATION_EXPIRED = ('%(within) 시간 내에 이메일은 인증하지 않으셨습니다. 당신의 이메일을 인증하기 위한 '
                                     '새로운 안내가 %(email)로 보내졌습니다', 'error')
SECURITY_MSG_LOGIN_EXPIRED = ('%(within) 동안 로그인하지 않으셨습니다. 로그인을 위한 새로운 안내사항이 '
                              '%(email)로 보내졌습니다.', 'error')
SECURITY_MSG_LOGIN_EMAIL_SENT = ('로그인을 위한 안내가 %(email)로 보내졌습니다.', 'success')
SECURITY_MSG_INVALID_LOGIN_TOKEN = ('잘못된 로그인 토큰입니다.', 'error')
SECURITY_MSG_DISABLED_ACCOUNT = ('사용할 수 없는 계정입니다.', 'error')
SECURITY_MSG_INVALID_EMAIL_ADDRESS = ('잘못된 이메일 주소입니다', 'error')
SECURITY_MSG_PASSWORD_NOT_PROVIDED = ('비밀번호가 입력되지 않았습니다', 'error')
SECURITY_MSG_PASSWORD_NOT_SET = ('사용자에게 아무 비밀번호도 설정되지 않았습니다', 'error')
SECURITY_MSG_PASSWORD_INVALID_LENGTH = ('비밀번호는 6자리 이상으로 설정하셔야 합니다.', 'error')
SECURITY_MSG_USER_DOES_NOT_EXIST = ('사용자가 존재하지 않습니다.', 'error')
SECURITY_MSG_INVALID_PASSWORD = ('잘못된 비밀번호입니다.', 'error')
SECURITY_MSG_PASSWORDLESS_LOGIN_SUCCESSFUL = ('성공적으로 로그인하셨습니다', 'success')
SECURITY_MSG_PASSWORD_RESET = ('감사합니다. 비밀번호 초기화가 완료되었고, 자동으로 로그인 됩니다.', 'success')
SECURITY_MSG_PASSWORD_IS_THE_SAME = ('당신의 새 비밀번호는 옛날 비밀번호와 달라야 합니다.', 'error')
SECURITY_MSG_PASSWORD_CHANGE = ('비밀번호를 성공적으로 바꾸셨습니다.', 'success')
SECURITY_MSG_LOGIN = ('이 페이지에 접근하시려면 로그인 해주세요.', 'info')
SECURITY_MSG_REFRESH = ('페이지에 접근하기 위해서 재인증해주세요.', 'info')