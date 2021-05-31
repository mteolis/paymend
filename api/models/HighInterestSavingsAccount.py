from api import db


class HighInterestSavingsAccount(db.Model):
    __tablename__ = 'high_interest_savings_account'

    id = db.Column(db.Integer, primary_key=True)
    principal = db.Column(db.Float)
    interest_rate = db.Column(db.Float)
    total = db.Column(db.Float)
    time_period = db.Column(db.Float)
    payout_date = db.Column(db.Date)
