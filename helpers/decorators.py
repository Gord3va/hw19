from functools import wraps
from typing import Callable
from flask import current_app
from flask import request, abort
import jwt


def auth_required(func: Callable) -> Callable:
    # Декоратор ограничения доступа на чтение
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)
        data = request.headers
        token = data.get("Authorization").split("Bearer ")[-1]
        try:
            jwt.decode(token, current_app.config.get('JWT_SECRET'),
                       algorithms=[current_app.config.get('JWT_ALGORITHM')])
        except Exception as e:
            print("JWT Decode Error", e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def admin_required(func: Callable) -> Callable:
    # Декоратор на редактирование
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        data = request.headers
        token = data.get("Authorization").split("Bearer ")[-1]
        role = None
        try:
            user = jwt.decode(token, current_app.config.get('JWT_SECRET'),
                              algorithms=[current_app.config.get('JWT_ALGORITHM')])
            role = user.get('role', 'user').lower()
        except Exception as e:
            print("JWT Decode Error")
            abort(401)
        if role != "admin":
            abort(403)
        return func(*args, **kwargs)

    return wrapper
