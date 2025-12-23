from app import db


class Contact(db.Model):
    __tablename__='contact'
    id = db.Column(db.Integer, primary_key=True)
    home_id = db.Column(db.Integer, db.ForeignKey('home.id'),nullable=False)
    name = db.Column(db.String(50),nullable=False, unique=True)
    code = db.Column(db.String(10), nullable=False, unique=True)


    def __repr__(self):
        return f'<Contact>{self.name}'