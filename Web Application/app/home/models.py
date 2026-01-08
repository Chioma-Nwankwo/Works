from app import db


class Home(db.Model):
    __tablename__='home'
    id = db.Column(db.Integer, primary_key=True)
    about_id = db.Column(db.Integer, db.ForeignKey('about.id'),nullable=False)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'),nullable=False)
    name = db.Column(db.String(50),nullable=False, unique=True)
    code = db.Column(db.String(10), nullable=False, unique=True)


    def __repr__(self):
        return f'<Home>{self.name}'
