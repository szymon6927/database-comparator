from dataclasses import asdict

from src.core.entities.customer_entitiy import Customer
from src.core.entities.event_entity import Event
from src.core.entities.order_entitiy import Order
from src.drivers.mongo.impls.cqrs.common import execute_delete_mongo
from src.drivers.mongo.impls.cqrs.common import execute_insert_mongo


def create_customer(customer: Customer):
    collection = 'customers'
    params = asdict(customer)

    execute_insert_mongo(collection, params)


def create_event(event: Event):
    collection = 'events'
    params = asdict(event)

    execute_insert_mongo(collection, params)


def create_order(order: Order):
    collection = 'orders'
    params = asdict(order)

    execute_insert_mongo(collection, params)


def delete_customers_collection_data():
    collection = 'customers'
    params = {}

    execute_delete_mongo(collection, params)


def delete_events_collection_data():
    collection = 'events'
    params = {}

    execute_delete_mongo(collection, params)


def delete_orders_collection_data():
    collection = 'orders'
    params = {}

    execute_delete_mongo(collection, params)
