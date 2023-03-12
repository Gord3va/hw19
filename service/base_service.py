from typing import Optional

from flask_sqlalchemy import Model
from flask import abort
from dao.base_dao import BaseDAO


class BaseService:
    """Базовый сервис"""

    def __init__(self, dao: BaseDAO):
        self.dao = dao

    def get_all(self) -> list[Model]:
        # Получить все
        return self.dao.get_all()

    def get_one(self, gid: int) -> Optional[Model]:
        # Получить по id
        value = self.dao.get_one(gid)
        if value is None:
            abort(404)
        return self.dao.get_one(gid)

    def create(self, data) -> Model:
        # Создать сущность
        return self.dao.create(data)

    def delete(self, received_id: int) -> None:
        # Удалить сущность
        value = self.get_one(received_id)
        if value is None:
            abort(404)
        self.dao.delete(value)
