from src.drivers.mysql.impls.mysql_repositories import CustomerMySQLRepository
from src.drivers.mysql.impls.mysql_repositories import EventMySQLRepository
from src.drivers.mysql.impls.mysql_repositories import OrderMySQLRepository
from src.performance.performance_test import BasePerformanceTest


class MySQLPerformanceTest(BasePerformanceTest):
    def __init__(self, operations_number: int):
        super().__init__(operations_number, CustomerMySQLRepository(), EventMySQLRepository(), OrderMySQLRepository())

    def present_results(self) -> None:
        pass
