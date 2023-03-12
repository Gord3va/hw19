import calendar
import datetime
from typing import Union

import jwt
from service.user_service import UserService
from flask import abort, current_app


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, username: str, password: Union[str, int], is_refresh=False) -> dict[str, Union[str, int]]:
        # Генерируем access_token и refresh_token
        user = self.user_service.get_by_username(username)

        if user is None:
            raise abort(404)

        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                abort(400)

        data = {
            "username": user.username,
            "role": user.role
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, current_app.config.get('JWT_SECRET'),
                                  algorithm=current_app.config.get('JWT_ALGORITHM'))

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, current_app.config.get('JWT_SECRET'),
                                   algorithm=current_app.config.get('JWT_ALGORITHM'))

        tokens = {"access_token": access_token, "refresh_token": refresh_token}
        print(tokens)
        return tokens

    def approve_refresh_token(self, refresh_token: bytes) -> dict[str, Union[str, int]]:
        # Получаем новые access_token и refresh_token
        if not self.check_token(refresh_token):
            abort(400)
        data = jwt.decode(refresh_token, current_app.config.get('JWT_SECRET'),
                          algorithms=[current_app.config.get('JWT_ALGORITHM')])
        username = data.get('username')
        return self.generate_tokens(username, None, is_refresh=True)

    def check_token(self, token) -> bool:
        # Проверка токена на валидность
        try:
            jwt.decode(token, current_app.config.get('JWT_SECRET'),
                       algorithms=[current_app.config.get('JWT_ALGORITHM')])
            return True
        except Exception as e:
            return False
