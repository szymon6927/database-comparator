import pytest

from src.core.exceptions import IllegalArgumentError
from src.core.factory import MultipleDatabaseTypeFactory
from src.performance.mysql.mysql_performance_test import MySQLPerformanceTest
from src.performance.postgres.postgresql_performance_test import PostgreSQLPerformanceTest


def test_multiple_database_type_factory_mysql_ok():
    factory = MultipleDatabaseTypeFactory()
    db_test = factory.create_database_test('mysql', 10)

    assert isinstance(db_test, MySQLPerformanceTest)


def test_multiple_database_type_factory_postgresql_ok():
    factory = MultipleDatabaseTypeFactory()
    db_test = factory.create_database_test('postgresql', 10)

    assert isinstance(db_test, PostgreSQLPerformanceTest)


def test_multiple_database_type_factory_with_bad_argument():
    with pytest.raises(IllegalArgumentError):
        factory = MultipleDatabaseTypeFactory()
        factory.create_database_test('test', 10)
