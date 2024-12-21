from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from flask_sqlalchemy import SQLAlchemy
from config import db


class Book(db.Model, SerializerMixin):

    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    published_date = db.Column(db.Integer, nullable=False)

    users = db.relationship('User', secondary='reviews', back_populates='books')
    reviews = db.relationship('Review', back_populates='book', cascade='all, delete_orphan')


class User(db.Model, SerializerMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

    books = db.relationship('Book', secondary='reviews', back_populates='users')
    reviews = db.relationship('Review', back_populates='user', cascade='all, delete_orphan')

    
    


class Review(db.Model, SerializerMixin):

    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    book = db.relationship('Book', back_populates='reviews')
    user = db.relationship('User', back_populates='reviews')

    

















# from sqlalchemy_serializer import SerializerMixin
# from sqlalchemy.ext.associationproxy import association_proxy

# from config import db

# # Models go here!
