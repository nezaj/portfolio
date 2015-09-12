from flask import Flask, redirect, url_for

from . import assets
from . import blog, gym, iphone, public
from .data.db import db
from .extensions import migrate
from .loggers import get_app_stderr_handler
from .template_filters import markdownize

def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    configure_loggers(app)
    initialize_app(app)
    register_extensions(app)
    register_blueprints(app)
    register_jinja_filters(app)
    return app

def configure_loggers(app):
    "Set up app.logger to emit messages according to configuration"
    app.logger.handlers = []
    app.logger.setLevel(app.config["APP_LOG_LEVEL"])
    app.logger.addHandler(get_app_stderr_handler())

def initialize_app(app):
    " Do any one-time initialization of the app prior to serving "
    app.static_folder = app.config['STATIC_DIR']
    register_error_handlers(app)

def register_extensions(app):
    assets.register_assets(app)
    migrate.init_app(app, db)

def register_blueprints(app):
    app.register_blueprint(blog.views.blueprint, url_prefix='/blog')
    app.register_blueprint(gym.views.blueprint, url_prefix='/gym')
    app.register_blueprint(iphone.views.blueprint, url_prefix='/iphone')
    app.register_blueprint(public.views.blueprint)

def register_jinja_filters(app):
    app.jinja_env.filters['markdownize'] = markdownize

def register_error_handlers(app):
    def handler(err):  # pylint: disable=unused-argument
        return redirect(url_for("public.welcome"))
    return app.errorhandler(404)(handler)
