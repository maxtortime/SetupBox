# -*- coding: utf-8 -*-
from config import FILES_ROOT, ALLOWED_EXTENSIONS
from filesystem import *
from flask import Flask, render_template, request, redirect, flash, url_for
from flask.ext.security import UserMixin, RoleMixin, SQLAlchemyUserDatastore, Security
from flask_security import http_auth_required, login_required
from flask_sqlalchemy import SQLAlchemy
from os import error
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config.from_object('config') # config import from config.py

# Define the DB
db = SQLAlchemy(app)

# Define models
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


'''
브라우저로 접속하면 로그인을 해야 한다는 alert 창이 뜸
terminal 에서는 http -a <email:password> <URL> 입력할 것 (README 참고)
ex) http -a maxtortime@gmail.com:123456 127.0.0.1:5000/authTest
'''

@app.route('/authTest')
@http_auth_required
def authTest():
    return "LOGIN GOOD"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/info')
def info():
    return render_template('info.html')


@app.route('/explorer')
@app.route('/files/<path:path>')
@login_required
def explorer(path=''):
    path_join = os.path.join(FILES_ROOT, path)
    if os.path.isdir(path_join):
        folder = Folder(FILES_ROOT, path)
        folder.read()
        return render_template('folder.html', folder=folder)
    else:
        my_file = File(FILES_ROOT, path)
        context = my_file.apply_action(View)
        folder = Folder(FILES_ROOT, my_file.get_path())

        if context == None:
            return render_template('file_unreadable.html', folder=folder)

        return render_template('file_view.html', text=context['text'], file=my_file, folder=folder)


@app.route('/search', methods=['POST'])
def search():
    q = request.form['q']
    return render_template('search.html', request = q)


@app.route('/new_directory', methods=["POST"])
@app.route('/<path:path>/new_directory', methods=["POST"])
def create_directory(path = ''):
    dirname = request.form["new_directory_name"]
    directory_root = request.form["directory_root"]

    try:
        os.mkdir(os.path.join(FILES_ROOT,directory_root,dirname))
    except error:
        print error.args
    return redirect('/files/' + directory_root)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == "POST":
        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            directory_root = request.form['directory_root']
            path = os.path.join(FILES_ROOT,directory_root,filename)

            file.save(path)

            return redirect(url_for('explorer', path=os.path.join(directory_root,filename)))
        else:
            return flash('file_upload_failed')

if __name__ == '__main__':
    app.run()
