import os
from . import create_app

app = create_app(os.getenv("CONFIG_MODE"))

@app.route('/home')
def home():
    return 'Agencia de viajes'

if __name__ == '__main__':
    app.run()