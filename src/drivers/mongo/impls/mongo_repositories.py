from src.core.entities.customer_entitiy import Customer
from src.core.entities.event_entity import Event
from src.core.entities.order_entitiy import Order
from src.core.exceptions import NotExists
from src.core.repositories import CustomerRepository
from src.core.repositories import EventRepository
from src.core.repositories import OrderRepository
from src.drivers.mongo.impls.cqrs.commands import create_customer
from src.drivers.mongo.impls.cqrs.commands import create_event
from src.drivers.mongo.impls.cqrs.commands import create_order
from src.drivers.mongo.impls.cqrs.commands import delete_customers_collection_data
from src.drivers.mongo.impls.cqrs.commands import delete_events_collection_data
from src.drivers.mongo.impls.cqrs.commands import delete_orders_collection_data
from src.drivers.mongo.impls.cqrs.queries import get_all_customers
from src.drivers.mongo.impls.cqrs.queries import get_all_events
from src.drivers.mongo.impls.cqrs.queries import get_all_orders
from src.drivers.mongo.impls.cqrs.queries import get_customer_by_id
from src.drivers.mongo.impls.cqrs.queries import get_event_by_id
from src.drivers.mongo.impls.cqrs.queries import get_order_by_id


class CustomerMongoRepository(CustomerRepository):
    def get_all(self):
        customers = get_all_customers()
        customer_entities = [Customer(**customer) for customer in customers]

        return customer_entities

    def get_by_id(self, customer_id):
        customer = get_customer_by_id(customer_id)

        if not customer:
            raise NotExists(f'Customer with {customer_id} id does not exist!')

        customer_entity = Customer(**customer)
        return customer_entity

    def add(self, customer: Customer):
        create_customer(customer)

    def delete_all(self):
        delete_customers_collection_data()


class EventMongoRepository(EventRepository):
    def get_all(self):
        events = get_all_events()
        event_entities = [Event(**event) for event in events]

        return event_entities

    def get_by_id(self, event_id):
        event = get_event_by_id(event_id)

        if not event:
            raise NotExists(f'Event with {event_id} id does not exist!')

        event_entity = Event(**event)
        return event_entity

    def add(self, event: Event):
        create_event(event)

    def delete_all(self):
        delete_events_collection_data()


class OrderMongoRepository(OrderRepository):
    def get_all(self):
        orders = get_all_orders()
        order_entities = [Order(**order) for order in orders]

        return order_entities

    def get_by_id(self, order_id):
        order = get_order_by_id(order_id)

        if not order:
            raise NotExists(f'Order with {order_id} id does not exist!')

        order_entity = Order(**order)
        return order_entity

    def add(self, order: Order):
        create_order(order)

    def delete_all(self):
        delete_orders_collection_data()
