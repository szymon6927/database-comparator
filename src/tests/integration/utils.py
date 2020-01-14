from faker import Faker

from src.core.common import uuid4
from src.core.entities.customer_entitiy import Customer
from src.core.entities.event_entity import Event
from src.core.entities.order_entitiy import Order

faker = Faker()


def _create_customer_entity() -> Customer:
    uuid = uuid4()
    customer = Customer(
        id=uuid,
        name=faker.name(),
        age=faker.random_int(25, 70),
        company_name='test',
        created_at=faker.date_time_this_month(),
    )

    return customer


def _create_event_entity() -> Event:
    uuid = uuid4()
    event = Event(
        id=uuid,
        name='test event',
        city=faker.word(),
        date=faker.date_time_this_month(),
        created_at=faker.date_time_this_year(),
    )

    return event


def _create_order_entity() -> Order:
    uuid = uuid4()
    order = Order(
        id=uuid,
        amount=float(faker.random_int()),
        updated_at=faker.date_time_this_month(),
        created_at=faker.date_time_this_year(),
    )

    return order
