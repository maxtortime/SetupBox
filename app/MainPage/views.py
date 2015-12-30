# -*- coding: utf-8 -*-

# index view
from flask import render_template, Blueprint
from flask_security import http_auth_required

'''
브라우저로 접속하면 로그인을 해야 한다는 alert 창이 뜸
terminal 에서는 http -a <email:password> <URL> 입력할 것 (README 참고)
ex) http -a maxtortime@gmail.com:123456 127.0.0.1:5000/foo
'''

MainPage = Blueprint('MainPage', __name__, template_folder='templates')

@MainPage.route('/authTest')
@http_auth_required
def authTest():
    return "LOGIN GOOD"

@MainPage.route('/')
def index():
    return render_template('index.html')

@MainPage.route('/info')
def info():
    return render_template('info.html')


@MainPage.route('/explorer')
def explorer():
    return render_template('explorer.html')


