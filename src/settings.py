import os
import logging

from sqlalchemy.engine.url import URL

class Config(object):
    # controls whether web interfance users are in Flask debug mode
    # (e.g. Werkzeug stack trace console, unminified assets)
    DEBUG = False

    # Encryption key used to sign Flask session cookies
    # Generate a random one using os.urandom(24)
    SECRET_KEY = os.environ.get('APP_KEY')

    # Loggging
    APP_LOG_LEVEL = logging.DEBUG
    SQLALCHEMY_LOG_LEVEL = logging.WARN
    STDERR_LOG_FORMAT = ('%(asctime)s %(levelname)s %(message)s', '%m/%d/%Y %I:%M:%S %p')

    # Useful directories
    SRC_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_DIR = os.path.join(SRC_DIR, 'static')

    SQLALCHEMY_DATABASE_URI = URL(drivername='sqlite', database='dev.db')

class DevelopmentConfig(Config):
    ENV = 'dev'

    # Enable the flask debugger
    DEBUG = True

class TestConfig(Config):
    ENV = 'test'

    # Dummy secret key for running tests
    SECRET_KEY = 'test'

    # Don't want to see info messages about managing posts
    APP_LOG_LEVEL = logging.WARN

class ProductionConfig(Config):
    ENV = 'prod'

    # Don't need to see debug messages in production
    APP_LOG_LEVEL = logging.INFO

config_dict = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig,
    'test': TestConfig,

    'default': DevelopmentConfig
}

app_config = config_dict[os.getenv('CONFIG_ENV') or 'default']
