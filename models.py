# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    hashed_password = db.Column(db.String(120), nullable=False)
    is_verified = db.Column(db.Boolean, nullable=False, default=False)
    class_of = db.Column(db.Integer, nullable=False)
    level = db.Column(db.String(120), nullable=False)
    bio = db.Column(db.String(120))
    image = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(120))
    github = db.Column(db.String(120))
    linkedin = db.Column(db.String(120))
    twitter = db.Column(db.String(120))
    website = db.Column(db.String(120))
    mastodon = db.Column(db.String(120))
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    
    def __repr__(self): 
        return f'<User {self.name}>'
