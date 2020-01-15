from unittest.mock import patch

import pytest

from src.core.entities.event_entity import Event
from src.core.entities.order_entitiy import Order
from src.core.enums import DBEnum
from src.core.exceptions import NotExists
from src.core.factory import MultipleDatabaseTypeFactory
from src.drivers.mongo.impls.mongo_repositories import CustomerMongoRepository
from src.drivers.mongo.impls.mongo_repositories import EventMongoRepository
from src.drivers.mongo.impls.mongo_repositories import OrderMongoRepository
from src.tests.integration.utils import _create_customer_entity
from src.tests.integration.utils import _create_event_entity
from src.tests.integration.utils import _create_order_entity


@pytest.fixture(scope='module', autouse=True)
def remove_mongo_dummy_data():
    yield
    database_test_factory = MultipleDatabaseTypeFactory()
    database_test = database_test_factory.create_database_test(DBEnum.MONGO.value, 0)
    database_test.clear_tables()


@patch('src.drivers.mongo.impls.mongo_repositories.create_customer')
def test_mongo_customer_repository_add(mock_create_customer):
    customer = _create_customer_entity()

    customer_repo = CustomerMongoRepository()
    customer_repo.add(customer)

    mock_create_customer.assert_called_with(customer)


def test_mongo_customer_repository_get_by_id():
    customer = _create_customer_entity()

    customer_repo = CustomerMongoRepository()
    customer_repo.add(customer)

    assert customer == customer_repo.get_by_id(customer.id)


def test_mongo_customer_repository_get_by_id_when_id_not_exist():
    customer_repo = CustomerMongoRepository()

    with pytest.raises(NotExists):
        customer_repo.get_by_id('1235')


def test_mongo_customer_repository_get_all():
    customer_repo = CustomerMongoRepository()

    all_customers = customer_repo.get_all()

    assert isinstance(all_customers, list)
    assert all_customers[0].company_name == 'test'


@patch('src.drivers.mongo.impls.mongo_repositories.create_order')
def test_mongo_order_repository_add(mock_create_order):
    order = _create_order_entity()

    order_repo = OrderMongoRepository()
    order_repo.add(order)

    mock_create_order.assert_called_with(order)


def test_mongo_order_repository_get_by_id():
    order = _create_order_entity()

    order_repo = OrderMongoRepository()
    order_repo.add(order)

    db_order = order_repo.get_by_id(order.id)

    assert order.id == db_order.id
    assert order.amount == db_order.amount


def test_mongo_order_repository_get_by_id_when_id_not_exist():
    order_repo = OrderMongoRepository()

    with pytest.raises(NotExists):
        order_repo.get_by_id('1235')


def test_mongo_order_repository_get_all():
    order_repo = OrderMongoRepository()

    all_orders = order_repo.get_all()

    assert isinstance(all_orders, list)
    assert isinstance(all_orders[0], Order)


@patch('src.drivers.mongo.impls.mongo_repositories.create_event')
def test_mongo_event_repository_add(mock_create_event):
    event = _create_event_entity()

    event_repo = EventMongoRepository()
    event_repo.add(event)

    mock_create_event.assert_called_with(event)


def test_mongo_event_repository_get_by_id():
    event = _create_event_entity()

    event_repo = EventMongoRepository()
    event_repo.add(event)

    db_event = event_repo.get_by_id(event.id)

    assert event.id == db_event.id
    assert event.name == db_event.name
    assert event.city == db_event.city


def test_mongo_event_repository_get_by_id_when_id_not_exist():
    event_repo = EventMongoRepository()

    with pytest.raises(NotExists):
        event_repo.get_by_id('1235')


def test_mongo_event_repository_get_all():
    event_repo = EventMongoRepository()

    all_events = event_repo.get_all()

    assert isinstance(all_events, list)
    assert isinstance(all_events[0], Event)
    assert all_events[0].name == 'test event'
