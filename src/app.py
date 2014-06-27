from flask import Flask

from .loggers import get_app_stderr_handler
from . import assets
from . import errors

def register_blueprints(app):
    " Registers blueprint routes on app "
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

def initialize_app(app):
    " Do any one-time initialization of the app prior to serving "
    app.static_folder = app.config['STATIC_DIR']
    assets.register_assets(app)
    errors.register_error_handlers(app)

def configure_loggers(app):
    "Set up app.logger to emit messages according to configuration"
    app.logger.handlers = []
    app.logger.setLevel(app.config["APP_LOG_LEVEL"])
    app.logger.addHandler(get_app_stderr_handler())

def create_app(config_obj):
    " Factory for creating app "
    app = Flask(__name__)
    app.config.from_object(config_obj)
    configure_loggers(app)
    initialize_app(app)
    register_blueprints(app)

    return app
