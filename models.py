"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, 
                   primary_key=True,
                   autoincrement=True)

    first_name = db.Column(db.String(30),
                           nullable=False)

    last_name = db.Column(db.String(30),
                          nullable=False)

    image_url = db.Column(db.String, nullable=False, default='https://static.thenounproject.com/png/3539026-200.png')

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, 
                   primary_key=True,
                   autoincrement=True)

    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.Date, nullable=False, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    user = db.relationship('User', backref='posts')

    

    