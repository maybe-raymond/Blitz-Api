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
    SQLALCHEMY_DATABASE_URI ='postgres://jsgtcavdpsaxvp:0a64640ae21b5d75f0ea8ad3ffd694054d818f0b3114b3869386860089c2c48f@ec2-52-23-86-208.compute-1.amazonaws.com:5432/d9a8g1lk1e6mi5'
