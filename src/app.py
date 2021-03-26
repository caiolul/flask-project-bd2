import os
from src.views.views import init_app as views_init
from src.ext.db.db_connection import configure as configure_db
from flask_migrate import Migrate
from flask import Flask

curren_path = os.path.dirname(os.path.abspath(__file__))


def create_app():
    app = Flask(__name__)
    if app.debug == True:
        path = 'sqlite:////%s/testing/test.db' % (curren_path)
        app.config['SQLALCHEMY_DATABASE_URI'] = path
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    views_init(app)
    configure_db(app)

    Migrate(app, app.db)
    return app