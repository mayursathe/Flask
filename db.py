from app import db

class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String, unique=True, nullable=False)
   email = db.Column(db.String, unique=True, nullable=False)
   password = db.Column(db.String, unique=False, nullable=False)

if __name__=='__main__':
    db.create_all()
    #db.session.add(User(username="select", email="select@gmail.com", password="876543210"))
    #db.session.commit()
