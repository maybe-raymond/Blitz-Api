import os

class Config(object):
    SECRET_KEY =  os.environ("very_long_key")
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ("postgres_local")
    JSON_SORT_KEYS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    DEBUG = True


class Production(Config):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ("postgres_heroku")
