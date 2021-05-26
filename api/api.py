import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from env_secrets import env_secrets


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = env_secrets.sqlalchemy_database_uri
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/time')
def get_current_time():
    return {'time': time.time(), 'noot': 'n00t'}

