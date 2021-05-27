from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from env_secrets import env_secrets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = env_secrets.sqlalchemy_database_uri
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Bill(db.Model):
    __tablename__ = 'bill'

    id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.Float)
    currency = db.Column(db.Enum)
    payment_date = db.Column(db.Date)
    frequency = db.Column(db.Enum)
    category = db.Column(db.Enum)

    def __init__(self, cost, currency, payment_date, frequency, category):
        self.cost = cost
        self.currency = currency
        self.payment_date = payment_date
        self.frequency = frequency
        self.category = category
