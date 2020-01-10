import pytest

from src.core.exceptions import MissingEnvVariableError
from src.drivers.mysql.db import get_connection


def test_get_connection_when_missing_envs(mysql_port_env_unset):
    with pytest.raises(MissingEnvVariableError):
        get_connection()
