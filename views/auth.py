from flask_restx import Resource, Namespace
from flask import request
from implemented import auth_service

auth_ns = Namespace("auth")


@auth_ns.route('/')
class AuthsView(Resource):

    def post(self):
        """Авторизация пользователя. Генерация access_token и refresh_token"""
        req = request.json
        username = req.get('username')
        password = req.get('password')
        if None in [username, password]:
            return "", 400
        tokens = auth_service.generate_tokens(username, password)
        return tokens, 201

    def put(self):
        """Получение новых access_token и refresh_token."""
        data = request.json
        refresh_token = data.get("refresh_token")
        if not refresh_token:
            return "", 401  # Не авторизован
        return auth_service.approve_refresh_token(refresh_token), 201
