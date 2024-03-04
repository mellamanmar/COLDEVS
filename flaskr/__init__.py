# Contiene la app

from flask import Flask
import os
# from flaskr.routes.booking import booking
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import config

db = SQLAlchemy()
migrate = Migrate ()

def create_app(config_mode):
    
    app = Flask (__name__ , instance_relative_config=True)
    app.config.from_object(config[config[config_mode]])

    db.init_app (app, db)
    migrate.init_app(app, db)

    return app


# if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)

    # # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    # app.register_blueprint(booking)
    # app.add_url_rule('/', endpoint='index')
