import pytest

from ..app import create_app
from ..app import create_app
from ..config import TestConfig
from ..extensions import db as _db


@pytest.yield_fixture(scope="function")
def app():
    """An application for the tests."""
    _app = create_app(TestConfig())

    with _app.app_context():
        _db.create_all()

    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.yield_fixture(scope="function")
def client(app):
    with app.test_client() as client:
        yield client


@pytest.yield_fixture(scope="function")
def db(app):
    """A database for the tests."""
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    # Explicitly close DB connection
    _db.session.close()
    _db.drop_all()