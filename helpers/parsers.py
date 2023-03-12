# Парсеры для валидации данных.
from flask_restx.reqparse import RequestParser

movie_parser: RequestParser = RequestParser()
movie_parser.add_argument(name="id", type=int)
movie_parser.add_argument(name="title", type=str, required=False)
movie_parser.add_argument(name="description", type=str, required=False)
movie_parser.add_argument(name="trailer", type=str, required=False)
movie_parser.add_argument(name="year", type=int, required=False)
movie_parser.add_argument(name="rating", type=float, required=False)
movie_parser.add_argument(name="genre_id", type=int, required=False)
movie_parser.add_argument(name="director_id", type=int, required=False)

director_parser: RequestParser = RequestParser()
director_parser.add_argument(name="id", type=int)
director_parser.add_argument(name="name", type=str, required=False)

genre_parser: RequestParser = RequestParser()
director_parser.add_argument(name="id", type=int)
genre_parser.add_argument(name="name", type=str, required=False)

user_parser: RequestParser = RequestParser()
user_parser.add_argument(name="id", type=int)
user_parser.add_argument(name="username", type=str, required=False)
user_parser.add_argument(name="password", type=str, required=False)
user_parser.add_argument(name="role", type=str, required=False)
