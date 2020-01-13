from src.drivers.postgres.impls.cqrs.common import execute_sql


def get_all_customers():
    sql = 'select * from customers'
    return execute_sql(sql)


def get_customer_by_id(customer_id):
    sql = f"select * from customers where id=%s"
    params = (f'{customer_id}',)

    return execute_sql(sql, params=params, many=False)


def get_all_events():
    sql = "select * from events"
    return execute_sql(sql)


def get_event_by_id(event_id):
    sql = f"select * from events where id=%s"
    params = (f'{event_id}',)

    return execute_sql(sql, params=params, many=False)


def get_all_orders():
    sql = "select * from orders"
    return execute_sql(sql)


def get_order_by_id(order_id):
    sql = f"select * from orders where id=%s"
    params = (f'{order_id}',)

    return execute_sql(sql, params=params, many=False)
