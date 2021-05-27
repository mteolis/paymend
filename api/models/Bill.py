from api import db


class Bill(db.Model):
    __tablename__ = 'bill'

    id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.Float)
    currency = db.Column(db.String)
    payment_date = db.Column(db.Date)
    frequency = db.Column(db.String)
    category = db.Column(db.String)
