from flask_restx import Resource, Namespace
from helpers.parsers import user_parser
from implemented import user_service
from dao.model.schemas import UserSchema

user_ns = Namespace("users")


@user_ns.route('/')
class UsersView(Resource):

    def get(self):
        """Возвращает всех пользователей."""
        return UserSchema(many=True).dump(user_service.get_all()), 200

    @user_ns.expect(user_parser)
    def post(self):
        """Создает нового пользователя."""
        return UserSchema().dump(user_service.create(user_parser.parse_args())), 201


@user_ns.route('/<int:uid>')
class UserView(Resource):

    def get(self, uid: int):
        """Возвращает пользователя по его id."""
        return UserSchema().dump(user_service.get_one(uid)), 200

    @user_ns.expect(user_parser)
    def put(self, uid: int):
        """Обновляет пользователя."""
        user = user_service.update(user_parser.parse_args(), uid)
        return UserSchema().dump(user), 204

    def delete(self, uid: int):
        """Удаляет пользователя"""
        user_service.delete(uid)
        return "", 204
