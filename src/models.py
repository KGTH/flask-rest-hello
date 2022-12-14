from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id =db.Column( db.Integer, primary_key=True  )
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
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80), nullable=False)
    image=db.Column(db.String(80))
    def __repr__(self):
        return '<Characters %r>' % self.username

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
    image=db.Column(db.String(80))
    def __repr__(self):
        return '<Planets %r>' % self.username

    def serialize(self):
       return {
            "id": self.id,
            "Name": self.name,
            "image": self.image
           
        }
class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_users = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    id_Characters=db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=False)
    id_planets=db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=False)

    def serialize(self):
       return {
            "id": self.id,
            "Name": self.name,
            "image": self.image
           
        }

class FavoritesCharacters(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     id_Characters=db.Column(db.Integer, nullable=True)
     name=db.Column(db.String(80), nullable=False)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
     user = db.relationship('User', backref='favoriteCharacter', lazy=True) 
     
   
    
     def serialize(self):
       return {
            "id": self.id,
            "user":self.user_id,
            "idcharacter": self.id_Characters,
            "people": self.name,
             
           
        }
class FavoritesPlanets(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     id_planet=db.Column(db.Integer, nullable=True )
     planet=db.Column(db.String(80), nullable=False)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 
     user = db.relationship('User', backref='favoritePlanet', lazy=True) 
     
   
     def serialize(self):
       return {
            "id": self.id,
            "user":self.user_id,
            "id_Planet": self.id_planet,
            "planet": self.planet, 
            
            
        }
