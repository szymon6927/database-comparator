import abc

from src.cli import SUPPORTED_DATABASES_CLI_ARGS
from src.core.exceptions import IllegalArgumentError
from src.performance.mysql.mysql_performance_test import MySQLPerformanceTest
from src.performance.performance_test import BasePerformanceTest


class DatabaseTestFactory(abc.ABC):
    @abc.abstractmethod
    def create_database_test(self, database_type: str, operations_number: int) -> BasePerformanceTest:
        pass


class MultipleDatabaseTypeFactory(DatabaseTestFactory):
    def create_database_test(self, database_type: str, operations_number: int) -> BasePerformanceTest:
        if database_type == 'mysql':
            return MySQLPerformanceTest(operations_number)

        raise IllegalArgumentError(
            f'Data required to create performance test needs to have one of this {SUPPORTED_DATABASES_CLI_ARGS}'
        )
