import sys

# -*- coding: utf-8 -*-
DEBUG = True # flask Debugging mode

# Enable protection agains *Cross-site Request Forgery (CSRF)*
WTF_CSRF_ENABLED = True
CSRF_ENABLED = True

# Define the application directory

# for korean character
reload(sys)
sys.setdefaultencoding('utf-8')

# Define the Database - MariaDB 10.1.7 on DigitalOcean cloud server
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://setupbox:tptdjqqkrtm@128.199.154.140/setupbox'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'super-secret'

# UPLOAD_FOLDER
UPLOAD_FOLDER = 'app/static/uploads/'

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2
CSRF_SESSION_KEY = "8f89068d65661cc47c7d4750e45b9891"

# flask-security blueprint name
SECURITY_BLUEPRINT_NAME = "setupbox"
