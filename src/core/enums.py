from enum import Enum


class DBEnum(Enum):
    MYSQL = 'mysql'
    POSTGRESQL = 'postgresql'
    MONGO = 'mongo'

    @staticmethod
    def list():
        return [e.value for e in DBEnum]
