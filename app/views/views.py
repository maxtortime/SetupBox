# -*- coding: utf-8 -*-

# index view
from app import app
from flask import render_template, request
from flask_classy import FlaskView
from flask_security import http_auth_required

'''
브라우저로 접속하면 로그인을 해야 한다는 alert 창이 뜸
terminal 에서는 http -a <email:password> <URL> 입력할 것 (README 참고)
ex) http -a maxtortime@gmail.com:123456 127.0.0.1:5000/foo
'''


@app.route('/foo')
@http_auth_required
def foo():
    return "LOGIN GOOD"


class IndexView(FlaskView):
    route_base = '/'

    def index(self):
        return render_template('index.html')
