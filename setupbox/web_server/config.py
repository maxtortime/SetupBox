# -*- coding: utf-8 -*-
import sys,os

DEBUG = True # flask Debugging mode
# UPLOAD_FOLDER = FILES_ROOT = os.path.dirname(os.path.abspath(os.path.expanduser('~/.setupbox/')))

# Enable protection agains *Cross-site Request Forgery (CSRF)*
WTF_CSRF_ENABLED = True
CSRF_ENABLED = True

# for korean character

reload(sys)
sys.setdefaultencoding('utf-8')

# Database
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://setupbox:tptdjqqkrtm@fast2.ajou.ac.kr/setupbox'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'super-secret'

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2
CSRF_SESSION_KEY = "8f89068d65661cc47c7d4750e45b9891"

SECURITY_REGISTERABLE = False
SECURITY_CONFIRMABLE = False
SECURITY_POST_LOGIN_VIEW = '/explorer'