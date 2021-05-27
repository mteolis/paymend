import os
import time
from flask import Flask
from flask_migrate import Migrate


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/paymend'

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from models.Bill import db
    db.init_app(app)
    migrate = Migrate(app, db)

    @app.route('/time')
    def get_current_time():
        return {'time': time.time(), 'noot': 'n00t'}

    return app
