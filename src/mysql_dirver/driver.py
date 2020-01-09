from src.mysql_dirver.impls.mysql_repositories import CustomerMySQLRepository


class MySQLDriver:
    def __init__(self):
        self.customer_repository = CustomerMySQLRepository()

    def test_get_all_customers(self):
        self.customer_repository.get_all()

    def run_tests(self):
        self.test_get_all_customers()
