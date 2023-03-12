from flask_sqlalchemy import Model
from service.base_service import BaseService


class GenreService(BaseService):

    def update(self, genre_d: dict, gid: int) -> Model:
        # Обновление жанра
        genre = self.dao.get_one(gid)
        genre.name = genre_d.get("name")

        return self.dao.update(genre)
