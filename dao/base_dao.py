from flask_sqlalchemy import Model


class BaseDAO:
    """Базовый DAO"""

    def __init__(self, session, model):
        self.session = session
        self.model = model

    def get_all(self) -> list[Model]:
        # Получить все
        return self.session.query(self.model).all()

    def get_one(self, gid: int) -> Model:
        # Получить по id
        return self.session.query(self.model).get(gid)

    def create(self, data: dict) -> Model:
        # Создать
        value = self.model(**data)
        self.session.add(value)
        self.session.commit()
        return value

    def update(self, value: Model) -> Model:
        # Обновить
        self.session.add(value)
        self.session.commit()
        return value

    def delete(self, value: Model) -> None:
        # Удалить
        self.session.delete(value)
        self.session.commit()

    def get_by_username(self, username: str) -> Model:
        pass

    def get_by_director_id(self, param):
        pass

    def get_by_genre_id(self, param):
        pass

    def get_by_year(self, param):
        pass
