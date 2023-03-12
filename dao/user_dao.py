from dao.base_dao import BaseDAO
from dao.model.models import User


class UserDAO(BaseDAO):
    def __init__(self, session):
        super().__init__(session, User)

    def get_by_username(self, username: str) -> User:
        # Получаем по имени.
        user = self.session.query(User).filter(User.username == username).first()
        return user
