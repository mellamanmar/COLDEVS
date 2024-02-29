# Contiene la app

from flask import Flask
from routes.booking import booking
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy ()

# def create_app(test_config=None):
app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/coldevs'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

    # return app

@app.route('/')
def home():
    return 'Agencia de viajes'

app.register_blueprint(booking)