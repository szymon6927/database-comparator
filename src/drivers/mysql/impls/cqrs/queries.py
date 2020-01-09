from drivers.mysql.impls.cqrs.common import execute_sql


def get_all_customers():
    sql = 'select * from customers'
    return execute_sql(sql)


def get_customer_by_id(customer_id):
    sql = f'select * from customers where id="{customer_id}"'
    return execute_sql(sql, many=False)


def get_all_events():
    sql = "select * from events"
    return execute_sql(sql)


def get_event_by_id(event_id):
    sql = f'select * from events where id="{event_id}"'
    return execute_sql(sql, many=False)


def get_all_orders():
    sql = "select * from orders"
    return execute_sql(sql)


def get_order_by_id(order_id):
    sql = f'select * from orders where id="{order_id}"'
    return execute_sql(sql, many=False)
