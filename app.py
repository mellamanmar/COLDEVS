from flask import Flask
from routes.booking import booking

app = Flask (__name__)


@app.route('/')
def home():
    return 'Agencia de viajes'

app.register_blueprint(booking)