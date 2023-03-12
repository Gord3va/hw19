
from marshmallow import Schema, fields


class BaseSchema(Schema):
    __abstract__ = True
    id = fields.Int()


class MovieSchema(BaseSchema):
    # Схема фильма
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()


class DirectorSchema(BaseSchema):
    # Схема режиссера
    name = fields.Str()


class GenreSchema(BaseSchema):
    # Схема жанра
    name = fields.Str()


class UserSchema(BaseSchema):
    # Схема пользователя
    username = fields.Str()
    password = fields.Str()
    role = fields.Str()
