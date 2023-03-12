import base64
import hashlib
import hmac
from flask_sqlalchemy import Model
from helpers.constants import PWD_HASH_ITERATIONS, PWD_HASH_SALT
from service.base_service import BaseService


class UserService(BaseService):

    def get_by_username(self, username: str) -> Model:
        # Получаем пользователя по его имени

        return self.dao.get_by_username(username)

    def create(self, data: dict) -> Model:
        # Создаем пользователя
        data['password'] = self.generate_hash(data['password'])

        return self.dao.create(data)

    def update(self, data: dict, uid: int) -> Model:
        # Обновляем пользователя
        data['password'] = self.generate_hash(data.get('password'))
        user = self.get_one(uid)
        user.username = data.get('username')
        user.password = data.get('password')
        user.role = data.get('role')

        return self.dao.update(user)

    def generate_hash(self, password: str) -> bytes:
        # Получаем хеш пароля
        hash_digest = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return base64.b64encode(hash_digest)

    def compare_passwords(self, hash_password, password) -> bool:
        # Проверка соответствия пароля из request паролю в БД
        decoded_digest = base64.b64decode(hash_password)  # Декодируем из хеш в бинарное представление
        hash_digest = base64.b64decode(self.generate_hash(password))  # Получаем бинарное представление второго пароля

        return hmac.compare_digest(decoded_digest, hash_digest)
