import pytest


@pytest.fixture(autouse=True)
def env_setup(monkeypatch):
    monkeypatch.setenv('MYSQL_PORT', '5306')
    monkeypatch.setenv('POSTGRES_PORT', '6432')
    monkeypatch.setenv('MONGO_PORT', '8017')


@pytest.fixture
def mysql_port_env_unset(monkeypatch):
    monkeypatch.delenv('MYSQL_PORT')


@pytest.fixture
def postgresql_port_env_unset(monkeypatch):
    monkeypatch.delenv('POSTGRES_PORT')


@pytest.fixture
def mongo_port_env_unset(monkeypatch):
    monkeypatch.delenv('MONGO_PORT')
