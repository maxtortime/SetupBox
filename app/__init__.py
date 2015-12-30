# -*- coding: utf-8 -*-
# Import flask and template operators
from MainPage.views import MainPage
from flask import Flask
from flask_security import SQLAlchemyUserDatastore, Security
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

app = Flask(__name__)
mail = Mail(app)
app.register_blueprint(MainPage)
app.config.from_object('config') # config import from config.py

# Define the DB
db = SQLAlchemy(app)
from models import User, Role

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
