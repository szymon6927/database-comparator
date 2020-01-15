import abc
import time

from faker import Faker

from src.core.common import generate_uuid4
from src.core.entities.customer_entitiy import Customer
from src.core.entities.event_entity import Event
from src.core.entities.order_entitiy import Order
from src.core.entities.table_performance_entity import TablePerformance
from src.core.repositories import CustomerRepository
from src.core.repositories import EventRepository
from src.core.repositories import OrderRepository


class BasePerformanceTest(abc.ABC):
    def __init__(
        self,
        operations_number: int,
        customer_repository: CustomerRepository,
        event_repository: EventRepository,
        order_repository: OrderRepository,
    ):
        self.operations_number = operations_number
        self.customers_uuid_list = [uuid for uuid in generate_uuid4(operations_number)]
        self.events_uuid_list = [uuid for uuid in generate_uuid4(operations_number)]
        self.orders_uuid_list = [uuid for uuid in generate_uuid4(operations_number)]
        self.faker = Faker()
        self.customer_repository = customer_repository
        self.event_repository = event_repository
        self.order_repository = order_repository

    def _create_customers(self) -> float:
        start = time.time()

        for uuid in self.customers_uuid_list:
            customer = Customer(
                id=uuid,
                name=self.faker.name(),
                age=self.faker.random_int(25, 70),
                company_name="Netguru",
                created_at=self.faker.date_time_this_month(),
            )

            self.customer_repository.add(customer)

        end = time.time()

        return round(end - start, 3)

    def _get_customers_by_id(self) -> float:
        start = time.time()

        for uuid in self.customers_uuid_list:
            self.customer_repository.get_by_id(uuid)

        end = time.time()

        return round(end - start, 3)

    def _get_all_customers(self) -> float:
        start = time.time()

        self.customer_repository.get_all()

        end = time.time()

        return round(end - start, 3)

    def _create_events(self) -> float:
        start = time.time()

        for uuid in self.events_uuid_list:
            event = Event(
                id=uuid,
                name=' '.join(self.faker.words(4)),
                city=self.faker.word(),
                date=self.faker.date_time_this_month(),
                created_at=self.faker.date_time_this_month(),
            )

            self.event_repository.add(event)

        end = time.time()

        return round(end - start, 3)

    def _get_events_by_id(self) -> float:
        start = time.time()

        for uuid in self.events_uuid_list:
            self.event_repository.get_by_id(uuid)

        end = time.time()

        return round(end - start, 3)

    def _get_all_events(self) -> float:
        start = time.time()

        self.event_repository.get_all()

        end = time.time()

        return round(end - start, 3)

    def _create_orders(self) -> float:
        start = time.time()

        for uuid in self.orders_uuid_list:
            order = Order(
                id=uuid,
                amount=float(self.faker.random_int()),
                updated_at=self.faker.date_time_this_month(),
                created_at=self.faker.date_time_this_year(),
            )

            self.order_repository.add(order)

        end = time.time()

        return round(end - start, 3)

    def _get_orders_by_id(self) -> float:
        start = time.time()

        for uuid in self.orders_uuid_list:
            self.order_repository.get_by_id(uuid)

        end = time.time()

        return round(end - start, 3)

    def _get_all_orders(self) -> float:
        start = time.time()

        self.order_repository.get_all()

        end = time.time()

        return round(end - start, 3)

    def test_customers_table(self) -> TablePerformance:
        return TablePerformance(
            table_name='customers',
            insert_time=self._create_customers(),
            get_by_id_time=self._get_customers_by_id(),
            get_all_time=self._get_all_customers(),
        )

    def test_events_table(self) -> TablePerformance:
        return TablePerformance(
            table_name='events',
            insert_time=self._create_events(),
            get_by_id_time=self._get_events_by_id(),
            get_all_time=self._get_all_events(),
        )

    def test_orders_table(self) -> TablePerformance:
        return TablePerformance(
            table_name='orders',
            insert_time=self._create_orders(),
            get_by_id_time=self._get_orders_by_id(),
            get_all_time=self._get_all_orders(),
        )

    @abc.abstractmethod
    def present_results(self) -> None:
        pass
