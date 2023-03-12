# Создание DAO и сервисов чтобы импортировать их везде.
from dao.base_dao import BaseDAO
from dao.model.models import Director, Genre
from dao.movie_dao import MovieDAO
from dao.user_dao import UserDAO
from service.auth_service import AuthService
from service.director_service import DirectorService
from service.genre_service import GenreService
from service.movie_service import MovieService
from service.user_service import UserService
from setup_db import db

director_dao = BaseDAO(session=db.session, model=Director)
genre_dao = BaseDAO(session=db.session, model=Genre)
movie_dao = MovieDAO(session=db.session)
user_dao = UserDAO(session=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
user_service = UserService(dao=user_dao)
auth_service = AuthService(user_service=user_service)
