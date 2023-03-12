# Создание базы данных
import json
from config import Config
from dao.model.models import Movie, Director, Genre, User
from setup_db import db
from app import create_app

app = create_app(Config)
app.app_context().push()


def insert_data(model, input_data):
    """Загрузка данных в таблицы"""
    for row in input_data:
        db.session.add(model(**row))


def create_base():
    """Создание таблиц"""
    db.drop_all()
    db.create_all()
    try:
        with open("fixtures/movies.json", "r", encoding="utf-8") as file:
            insert_data(Movie, json.load(file))

        with open("fixtures/direcors.json", "r", encoding="utf-8") as file:
            insert_data(Director, json.load(file))

        with open("fixtures/genres.json", "r", encoding="utf-8") as file:
            insert_data(Genre, json.load(file))

        db.session.commit()
    except Exception:
        db.session.rollback()
        db.session.commit()


create_base()
