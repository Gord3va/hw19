from typing import Optional

from dao.model.models import Movie
from service.base_service import BaseService


class MovieService(BaseService):
    """Сервисы фильма"""

    def get_by_request(self, data: dict) -> Optional[list[Movie]]:
        # Получить фильмы по id режиссера, id жанра и году
        if "director_id" in data:
            return self.dao.get_by_director_id(data.get('director_id'))
        if "genre_id" in data:
            return self.dao.get_by_genre_id(data.get('genre_id'))
        if "year" in data:
            return self.dao.get_by_year(data.get('year'))
        return None

    def update(self, data: dict, mid: int) -> Optional[Movie]:
        # Обновление фильма
        try:
            movie = self.dao.get_one(mid)
            movie.title = data.get('title')
            movie.description = data.get('description')
            movie.trailer = data.get('trailer')
            movie.year = data.get('year')
            movie.rating = data.get('rating')
            movie.genre_id = data.get('genre_id')
            movie.director_id = data.get('director_id')
            return self.dao.update(movie)
        except Exception as e:
            return None
