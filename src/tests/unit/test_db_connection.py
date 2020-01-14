import pytest

from src.core.exceptions import MissingEnvVariableError
from src.drivers.mongo.db import get_connection as mongo_get_connection
from src.drivers.mysql.db import get_connection as mysql_get_connection
from src.drivers.postgres.db import get_connection as postgresql_get_connection


def test_get_mysql_connection_when_missing_envs(mysql_port_env_unset):
    with pytest.raises(MissingEnvVariableError):
        mysql_get_connection()


def test_get_postgresql_connection_when_missing_envs(postgresql_port_env_unset):
    with pytest.raises(MissingEnvVariableError):
        postgresql_get_connection()


def test_get_mongo_connection_when_missing_envs(mongo_port_env_unset):
    with pytest.raises(MissingEnvVariableError):
        mongo_get_connection()
