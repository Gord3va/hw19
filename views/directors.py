from flask_restx import Resource, Namespace
from dao.model.schemas import DirectorSchema
from helpers.decorators import auth_required, admin_required
from helpers.parsers import director_parser
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        """Возвращает всех режиссеров."""
        return DirectorSchema(many=True).dump(director_service.get_all()), 200

    @director_ns.expect(director_parser)
    @admin_required
    def post(self):
        """Создает режиссера."""
        return DirectorSchema().dump(director_service.create(director_parser.parse_args())), 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    @auth_required
    def get(self, did):
        """Возвращает режиссера по его id."""
        return DirectorSchema().dump(director_service.get_one(did)), 200

    @director_ns.expect(director_parser)
    @admin_required
    def put(self, did: int):
        """Обновляет режиссера."""
        director = director_service.update(director_parser.parse_args(), did)
        return DirectorSchema().dump(director), 204

    @admin_required
    def delete(self, did: int):
        """Удаляет режиссера"""
        director_service.delete(did)
        return "", 204
