import pytest


@pytest.fixture(autouse=True)
def env_setup(monkeypatch):
    monkeypatch.setenv('MYSQL_PORT', '5306')


@pytest.fixture
def mysql_port_env_unset(monkeypatch):
    monkeypatch.delenv('MYSQL_PORT')
