from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from runserver import app, db
from config import SQLALCHEMY_DATABASE_URI
import sqlite3

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def create_db():
    conn = sqlite3.connect('setupbox.db')
    if conn:
        print "setupbox.db created successfully"
    else:
        print "Creating setupbox.db failed"


if __name__ == '__main__':
    manager.run()
