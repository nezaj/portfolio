#!/usr/bin/env python

def import_env():
    import os
    if os.path.exists('.env'):
        print 'Importing environment from .env...'
        for line in open('.env'):
            var = line.strip().split('=', 1)
            if len(var) == 2:
                os.environ[var[0]] = var[1]

import_env()

from src.app import create_app
from src.config import app_config

flask_app = create_app(app_config)
