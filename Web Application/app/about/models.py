from app import db


class About(db.Model):
    __tablename__='about'
    id = db.Column(db.Integer, primary_key=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'),nullable=False)
    name = db.Column(db.String(50),nullable=False, unique=True)
    code = db.Column(db.String(10), nullable=False, unique=True)


    def __repr__(self):
        return f'<About>{self.name}'