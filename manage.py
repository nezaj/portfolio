#!/usr/bin/env python

"""
Usage: ./manage.py [submanager] <command>
Manage script for development. Type ./manage.py for more info
"""
import os
import subprocess

from flask_migrate import MigrateCommand as db_manager
from flask_script import Manager
from flask_script.commands import ShowUrls

from src.data.db import db, DatabaseConnection
from src.data.base import BaseModel
from src.settings import app_config
from src.util import invoke_process, parse_sqlalchemy_url, yes_no
from src.app import create_app

app = create_app(app_config)

manager = Manager(app)
manager.add_command("db", db_manager)
manager.add_command("routes", ShowUrls())

@manager.shell
def make_context_shell():
    """Starts a python shell with with app, db and models loaded"""
    # Loads all the models which inherit from Base
    models_map = {name: cls for name, cls in models.__dict__.items() if isinstance(cls, type(BaseModel))}
    return dict(app=app, db=db, **models_map)

@db_manager.option('--url', dest='url', default=app.config['SQLALCHEMY_DATABASE_URI'],
                   type=parse_sqlalchemy_url,
                   help="A RFC1738 URL to a PostgreSQL or SQLite database to use.")
def repl(url):
    """Launch a psql or sqlite3 repl connected to the database"""
    def build_named_arglist(arg_dict):
        for name, value in arg_dict.iteritems():
            yield "--{}".format(name)
            yield str(value)

    dialect = url.get_dialect()

    if dialect.name == "postgresql":
        env = os.environ.copy()
        env["PGPASSWORD"] = url.password
        proc_args = list(build_named_arglist({
            'host': url.host,
            'port': url.port,
            'username': url.username,
            'dbname': url.database
        }))
        return invoke_process("psql", proc_args, env=env)
    elif dialect.name == "sqlite":
        proc_args = [url.database] if url.database else []
        return invoke_process("sqlite3", proc_args)
    else:
        raise ValueError("Dialect {} is not supported.".format(dialect.name))

if __name__ == '__main__':
    manager.run()
