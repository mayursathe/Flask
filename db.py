from app import db
from flask_bcrypt import generate_password_hash

class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String, unique=True, nullable=False)
   email = db.Column(db.String, unique=True, nullable=False)
   password = db.Column(db.String, unique=False, nullable=False)

if __name__=='__main__':
    db.create_all()
    db.session.add(User(username="Mayur2", email="mayursathe123@gmail.com", password=generate_password_hash('876543210')))
    db.session.commit()
