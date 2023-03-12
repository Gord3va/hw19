from flask_restx import Resource, Namespace
from dao.model.schemas import GenreSchema
from helpers.decorators import auth_required, admin_required
from helpers.parsers import genre_parser
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):

    @auth_required
    def get(self):
        """Возвращает все жанры."""
        return GenreSchema(many=True).dump(genre_service.get_all()), 200

    @genre_ns.expect(genre_parser)
    @admin_required
    def post(self):
        """Создает жанр."""
        return GenreSchema().dump(genre_service.create(genre_parser.parse_args())), 201


@genre_ns.route('/<int:gid>')
class GenreView(Resource):

    @auth_required
    def get(self, gid):
        """Возвращает жанр по его id."""
        return GenreSchema().dump(genre_service.get_one(gid)), 200

    @genre_ns.expect(genre_parser)
    @admin_required
    def put(self, gid: int):
        """Обновляет жанр."""
        genre = genre_service.update(genre_parser.parse_args(), gid)
        return GenreSchema().dump(genre), 204

    @admin_required
    def delete(self, gid: int):
        """Удаляет жанр."""
        genre_service.delete(gid)
        return "", 204
