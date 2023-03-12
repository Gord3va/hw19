from flask_sqlalchemy import Model
from service.base_service import BaseService


class DirectorService(BaseService):

    def update(self, director_d: dict, did: int) -> Model:
        # Обновление режиссера
        director = self.get_one(did)
        director.name = director_d.get("name")
        return self.dao.update(director)
