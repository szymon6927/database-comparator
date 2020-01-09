from src.core.entities.customer_entitiy import Customer
from src.core.repositories import CustomerRepository
from src.core.repositories import EventRepository
from src.core.repositories import OrderRepository
from src.mysql_dirver.impls.cqrs.queries import get_all_customers


class CustomerMySQLRepository(CustomerRepository):
    def get_all(self):
        customers = get_all_customers()

        customer_entities = []
        for customer in customers:
            customer_entity = Customer(
                id=customer.get('id'),
                name=customer.get('name'),
                age=customer.get('age'),
                company_name=customer.get('company_name'),
                created_at=customer.get('company_name'),
            )

            customer_entities.append(customer_entity)

        return customer_entities

    def get_by_id(self, customer_id):
        pass

    def add(self, customer):
        pass


class EventMySQLRepository(EventRepository):
    def get_all(self):
        pass

    def get_by_id(self, event_id):
        pass

    def add(self, event):
        pass


class OrderMySQLRepository(OrderRepository):
    def get_all(self):
        pass

    def get_by_id(self, order_id):
        pass

    def add(self, order):
        pass
