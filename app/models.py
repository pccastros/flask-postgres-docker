from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    phone = db.Column(db.String(20))
    age = db.Column(db.Integer)

    def __repr__(self):
        return '<User {}>'.format(self.name)