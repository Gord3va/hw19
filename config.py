# Файл конфигурации
class Config(object):
    DEBUG = False
    JWT_SECRET = '249y823r9v8238r9u'
    JWT_ALGORITHM = "HS256"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {"ensure_ascii": False}
