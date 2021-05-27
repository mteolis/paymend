from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Bill(db.Model):
    __tablename__ = 'bill'

    id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.Float)
    currency = db.Column(db.String)
    payment_date = db.Column(db.Date)
    frequency = db.Column(db.String)
    category = db.Column(db.String)

    def __init__(self, cost, currency, payment_date, frequency, category):
        self.cost = cost
        self.currency = currency
        self.payment_date = payment_date
        self.frequency = frequency
        self.category = category
