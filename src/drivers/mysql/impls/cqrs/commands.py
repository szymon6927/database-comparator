from src.drivers.mysql.impls.cqrs.common import execute_insert_or_delete_sql


def create_customer(uuid, name, age, company_name, created_at):
    sql = (
        f'insert into customers (id, name, age, company_name, created_at) '
        f'values ("{uuid}", "{name}", {age}, "{company_name}", "{created_at}")'
    )
    execute_insert_or_delete_sql(sql)


def create_event(uuid, name, city, date):
    sql = f'insert into events (id, name, city, date) values ("{uuid}", "{name}", "{city}", "{date}")'
    execute_insert_or_delete_sql(sql)


def create_order(uuid, amount):
    sql = f'insert into orders (id, amount) values ("{uuid}", {amount})'
    execute_insert_or_delete_sql(sql)


def delete_customers_table_data():
    sql = 'truncate table customers; '
    execute_insert_or_delete_sql(sql)


def delete_events_table_data():
    sql = 'truncate table events; '
    execute_insert_or_delete_sql(sql)


def delete_orders_table_data():
    sql = 'truncate table orders; '
    execute_insert_or_delete_sql(sql)
