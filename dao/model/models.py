
from setup_db import db


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class Movie(BaseModel):
    # Модель фильма
    __tablename__ = 'movie'
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")


class Director(BaseModel):
    # Модель режиссера
    __tablename__ = 'director'
    name = db.Column(db.String(255))


class Genre(BaseModel):
    # Модель жанра
    __tablename__ = 'genre'
    name = db.Column(db.String(255))


class User(BaseModel):
    # Модель пользователя
    __tablename__ = "user"
    username = db.Column(db.String)
    password = db.Column(db.String)
    role = db.Column(db.String)
