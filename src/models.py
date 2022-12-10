from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, default =0)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
   
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "Name": self.name,
            "email": self.email
            # do not serialize the password, its a security breach
        }

class Characters (db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80), nullable=False)
    gender=db.Column(db.String(80), nullable=True)
    image=db.Column(db.String(80))
    
    def serialize(self):
       return {
            "id": self.id,
            "Name": self.name,
            "image": self.image
           
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80), nullable=False)
    population=db.Column(db.Integer, default =0)
    climate= db.Column(db.String(200))
    image=db.Column(db.String(200), nullable=True)

    def serialize(self):
       return {
            "id": self.id,
            "Name": self.name,
            "image": self.image
           
        }


class Favorites_Characters(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     name=db.Column(db.String(80), nullable=False)
     image=db.Column(db.String(200), nullable=True)
     def serialize(self):
       return {
            "id": self.id,
            "Name": self.name,
            "image": self.image
           
        }
