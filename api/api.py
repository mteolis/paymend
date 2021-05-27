import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/paymend'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/time')
def get_current_time():
    return {'time': time.time(), 'neep': 'neep'}

