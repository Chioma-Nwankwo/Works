from app import db


class Menu(db.Model):
    __tablename__='menu'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False, unique=True)
    code = db.Column(db.String(10), nullable=False, unique=True)


    def __repr__(self):
        return f'<Menu>{self.name}'
              

                   
    