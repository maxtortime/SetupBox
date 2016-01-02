# index view
from app import app, db, user_datastore
from flask import render_template
from flask_classy import FlaskView
from flask_security import login_required

@app.before_first_request
def create_user():
    db.create_all()
    user_datastore.create_user(email='maxtortime@gmail.com', password='123456')
    db.session.commit()


class IndexView(FlaskView):
    decorators = [login_required]
    route_base = '/'

    def index(self):
        return render_template('index.html')