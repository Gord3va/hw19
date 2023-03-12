from dao.base_dao import BaseDAO
from dao.model.models import Movie


class MovieDAO(BaseDAO):
    def __init__(self, session):
        super().__init__(session, Movie)

    def get_by_director_id(self, val: int) -> list[Movie]:
        # Получаем по id режиссера
        return self.session.query(Movie).filter(Movie.director_id == val).all()

    def get_by_genre_id(self, val: int) -> list[Movie]:
        # Получаем по id жанра
        return self.session.query(Movie).filter(Movie.genre_id == val).all()

    def get_by_year(self, val: int) -> list[Movie]:
        # Получаем по году
        return self.session.query(Movie).filter(Movie.year == val).all()
