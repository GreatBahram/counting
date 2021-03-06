# Standard library imports
from datetime import datetime

# local imports
from pyaccounting import db


class PaymentModel(db.Model):
    """ Create a Payment table """
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    buyer = db.Column(db.Integer, db.ForeignKey('persons.id'))
    debtor = db.Column(db.Integer, db.ForeignKey('persons.id'))
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200))
    is_payoff = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
            onupdate=db.func.current_timestamp())

    def to_dict(self):
        return {
                'id': self.id,
                'date': self.date,
                'buyer': self.buyer,
                'debtor': self.debtor,
                'price': self.price,
                'description': self.description,
                'is_sale': self.is_sale,
                }

    def __repr__(self):
        if self.is_payoff:
            return f"<Payment: {self.debtor} +=> {self.buyer} ${self.price}"
        return f"<Payment: {self.debtor} -=> {self.buyer} ${self.price} "

    @classmethod
    def list_all_purchases(cls, id):
        items = cls.query.filter_by(is_payoff=False).filter_by(buyer=id).all()
        return items

    @classmethod
    def list_all_payoffs(cls, id):
        items = cls.query.filter_by(is_payoff=True).filter_by(debtor=id).all()
        return items

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
