from faker import Faker

from drivers.mysql.impls.mysql_repositories import CustomerMySQLRepository
from src.core.common import uuid4
from src.core.entities.customer_entitiy import Customer


class MySQLDriver:
    def __init__(self):
        self.customer_repository = CustomerMySQLRepository()
        self.faker = Faker()

    def test_get_all_customers(self):
        result = self.customer_repository.get_all()
        return result

    def test_get_customer_by_id(self):
        new_customer = self.test_create_customer()
        customer = self.customer_repository.get_by_id(new_customer.id)
        return customer

    def test_create_customer(self):
        customer = Customer(
            id=uuid4(),
            name=self.faker.name(),
            age=self.faker.random_int(25, 70),
            company_name="Netguru",
            created_at=self.faker.date_time_this_month(),
        )

        self.customer_repository.add(customer)
        return customer

    def run_tests(self):
        self.test_get_all_customers()
        self.test_get_customer_by_id()
        self.test_create_customer()
