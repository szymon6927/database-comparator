from src.drivers.mongo.impls.cqrs.common import execute_mongo


def get_all_customers():
    collection = 'customers'
    params = {}

    return execute_mongo(collection, params)


def get_customer_by_id(customer_id):
    collection = 'customers'
    params = {'id': f'{customer_id}'}

    return execute_mongo(collection, params, many=False)


def get_all_events():
    collection = 'events'
    params = {}

    return execute_mongo(collection, params)


def get_event_by_id(event_id):
    collection = 'events'
    params = {'id': f'{event_id}'}

    return execute_mongo(collection, params, many=False)


def get_all_orders():
    collection = 'orders'
    params = {}

    return execute_mongo(collection, params)


def get_order_by_id(order_id):
    collection = 'orders'
    params = {'id': f'{order_id}'}

    return execute_mongo(collection, params, many=False)
