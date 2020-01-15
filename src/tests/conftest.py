import pytest
from _pytest.monkeypatch import MonkeyPatch


@pytest.fixture(autouse=True, scope='session')
def env_setup():
    m_patch = MonkeyPatch()
    m_patch.setenv('MYSQL_PORT', '5306')
    m_patch.setenv('POSTGRES_PORT', '6432')
    m_patch.setenv('MONGO_PORT', '8017')

    yield m_patch

    m_patch.undo()


@pytest.fixture
def mysql_port_env_unset(monkeypatch):
    monkeypatch.delenv('MYSQL_PORT')


@pytest.fixture
def postgresql_port_env_unset(monkeypatch):
    monkeypatch.delenv('POSTGRES_PORT')


@pytest.fixture
def mongo_port_env_unset(monkeypatch):
    monkeypatch.delenv('MONGO_PORT')
