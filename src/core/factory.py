import abc

from src.core.enums import DBEnum
from src.core.exceptions import IllegalArgumentError
from src.performance.mongo.mongo_performance_test import MongoPerformanceTest
from src.performance.mysql.mysql_performance_test import MySQLPerformanceTest
from src.performance.performance_test import BasePerformanceTest
from src.performance.postgres.postgresql_performance_test import PostgreSQLPerformanceTest


class DatabaseTestFactory(abc.ABC):
    @abc.abstractmethod
    def create_database_test(self, database_type: str, operations_number: int) -> BasePerformanceTest:
        pass


class MultipleDatabaseTypeFactory(DatabaseTestFactory):
    def create_database_test(self, database_type: str, operations_number: int) -> BasePerformanceTest:
        if database_type == DBEnum.MYSQL.value:
            return MySQLPerformanceTest(operations_number)

        if database_type == DBEnum.POSTGRESQL.value:
            return PostgreSQLPerformanceTest(operations_number)

        if database_type == DBEnum.MONGO.value:
            return MongoPerformanceTest(operations_number)

        raise IllegalArgumentError(
            f'Data required to create performance test needs to have one of this {DBEnum.list()}'
        )
