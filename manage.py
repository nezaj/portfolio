#!/usr/bin/env python

from flask_script import Manager
from flask_script.commands import ShowUrls

def import_env():
    import os
    if os.path.exists('.env'):
        print 'Importing environment from .env...'
        for line in open('.env'):
            var = line.strip().split('=', 1)
            if len(var) == 2:
                os.environ[var[0]] = var[1]

if __name__ == '__main__':
    import_env()

    from src.app import create_app
    from src.config import app_config

    flask_app = create_app(app_config)
    manager = Manager(flask_app)
    manager.add_command("routes", ShowUrls())

    manager.run()
