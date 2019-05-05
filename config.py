import os


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', b'\xf6X\xb7\x98\xe9P\xd0Pi\xb3m\xce\x07i0X')
    DB_URL = None


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DB_URL = "mongodb+srv://hfUser:hfPass@cluster0-q7hhg.gcp.mongodb.net/harmanfood?retryWrites=true"


class TestingConfig(Config):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
