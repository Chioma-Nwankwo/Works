from app import db


class Customer(db.Model):
    __tablename__='customer'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'),nullable=False)
    name = db.Column(db.String(50),nullable=False, unique=True)
    code = db.Column(db.String(10), nullable=False, unique=True)
    price = db.Column(db.Numeric(precision=10, scale=2), nullable=False, unique=False)

    order=db.relationship('Order', backref='customer')


    def __repr__(self):
        return f'<Customer>{self.name}'