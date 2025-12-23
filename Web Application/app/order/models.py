from app import db


class Order(db.Model):
    __tablename__='order'
    id = db.Column(db.Integer, primary_key=True)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'),nullable=False)
    name = db.Column(db.String(50),nullable=False, unique=True)
    code = db.Column(db.String(10), nullable=False, unique=True)

    menu = db.relationship('Menu', backref='menu')


    def __repr__(self):
        return f'<Order>{self.name}'