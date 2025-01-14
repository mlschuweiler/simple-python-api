import pytest

from api import api
from db import db
from config import create_config, app
from tests.unit.load_data import db_create_example_data

@pytest.fixture(scope="session", autouse=True)
def test_app():
    app.app_context().push()
    custom_config = create_config()
    app.config.update(custom_config)
    app.config["TESTING"] = True
    app.config.update({"SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"})

    db_create_example_data()
    yield app
    db.drop_all()

@pytest.fixture(scope="session", autouse=True)
def client(test_app):
    return test_app.test_client()
