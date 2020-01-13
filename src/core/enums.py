from enum import Enum


class DBEnum(Enum):
    MYSQL = 'mysql'
    POSTGRESQL = 'postgresql'

    @staticmethod
    def list():
        return [e.value for e in DBEnum]
