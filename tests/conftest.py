"""
Configures pytest and fixtures for tests in this package
"""
import os

from flask_webtest import TestApp
import pytest

from src.settings import TestConfig
from src.app import create_app

# py.test uses these parameters under the hood
# pylint: disable=unused-argument
def pytest_cmdline_main(config):
    """
    Enforce test environment before loading fixtures and running tests
    This helps prevent accidents like creating/dropping the db in a stage/prod
    environment when running the test suite
    """
    if os.environ.get('CONFIG_ENV') != 'test':
        pytest.exit('Please set CONFIG_ENV=test before running test suite')

@pytest.fixture(scope='function')
def app(request):
    """
    Flask app instance fixture with an active request context.
    See: http://flask.pocoo.org/docs/0.10/reqcontext/
    """
    _app = create_app(TestConfig)
    request.instance.app = _app

    ctx = _app.test_request_context()
    ctx.push()

    request.addfinalizer(ctx.pop)
    return _app

@pytest.fixture(scope='function')
def client(app, request):
    """
    Flask-Webtest TestApp provides convenient methods for writing
    functional tests

    See:
    http://flask-webtest.readthedocs.org/en/latest/
    http://webtest.readthedocs.org/en/latest/
    """
    request.instance.client = TestApp(app)
