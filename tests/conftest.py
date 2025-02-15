from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), "../.env-tests")
load_dotenv(dotenv_path)

from fastapi.testclient import TestClient
import pytest

from app.main import app

#### NECESSARY IMPORTS
from tests.fixtures import start_postgres_container
####


GLOBAL_CLIENT = None


def pytest_sessionstart(session):
    global GLOBAL_CLIENT
    GLOBAL_CLIENT = TestClient(app)


