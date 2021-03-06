
import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://josphat:nevergiveup@localhost/garage'
    

class ProdConfig(Config):
    DEBUG=True


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}