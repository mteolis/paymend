from api import db


class MoneyOwed(db.Model):
    __tablename__ = 'money_owed'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    currency = db.Column(db.String)
    payment_date = db.Column(db.Date)
    frequency = db.Column(db.String)
    category = db.Column(db.String)
    sender = db.Column(db.String)
    recipient = db.Column(db.String)
