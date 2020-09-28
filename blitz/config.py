class Config(object):
    SECRET_KEY = '\x00\x8c\xe1^\xa9\xfa\xb4\x80h\xf9o\xa8\xc3\xa5\xa3\x12'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:dogbatman10@localhost/blitzdatabase'
    JSON_SORT_KEYS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    DEBUG = True


class Production(Config):
    TESTING = False
