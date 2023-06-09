# Основной файл
from typing import Type
from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.auth import auth_ns
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns
from views.users import user_ns


def create_app(config_object: Type[Config]) -> Flask:
    # Функция создания основного объекта app
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.url_map.strict_slashes = False
    register_extensions(app)
    app.app_context().push()
    db.create_all()
    return app


def register_extensions(app):
    # Функция подключения расширений
    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


app = create_app(Config)


@app.errorhandler(404)
def not_found(error):
    return "Not Found", 404


@app.errorhandler(500)
def iternal_error(error):
    return "Iternal Error Server", 500


if __name__ == '__main__':
    app.run(host="localhost", port=10001)
