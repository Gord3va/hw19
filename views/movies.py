from flask import request, url_for
from flask_restx import Resource, Namespace
from helpers.decorators import auth_required, admin_required
from implemented import movie_service
from dao.model.schemas import MovieSchema
from helpers.parsers import movie_parser

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):

    @auth_required
    def get(self):
        """Возвращает все фильмы, фильмы по режиссеру, жанру и году."""
        req_json = request.args
        if req_json:
            try:
                int(list(req_json.to_dict().values())[0])
            except ValueError as e:
                raise ValueError(f"Не соответсвующее значение. {e}")
            return MovieSchema(many=True).dump(movie_service.get_by_request(req_json)), 200
        return MovieSchema(many=True).dump(movie_service.get_all()), 200

    @movie_ns.expect(movie_parser)
    @admin_required
    def post(self):
        """Добавляет фильм."""
        movie = movie_service.create(movie_parser.parse_args())
        return MovieSchema().dump(movie), 201, {'Location': f"{url_for('movies_movie_view', mid=movie.id)}"}


@movie_ns.route('/<int:mid>')
class MovieView(Resource):

    @auth_required
    def get(self, mid: int):
        """Возвращает фильм по его id."""
        return MovieSchema().dump(movie_service.get_one(mid)), 200

    @movie_ns.expect(movie_parser)
    @admin_required
    def put(self, mid: int):
        """Обновляет фильм."""
        movies = movie_service.update(movie_parser.parse_args(), mid=mid)
        return MovieSchema().dump(movies), 204

    @admin_required
    def delete(self, mid: int):
        """Удаляет фильм."""
        movie_service.delete(mid)
        return "", 204
