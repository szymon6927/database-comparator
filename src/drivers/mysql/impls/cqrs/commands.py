from src.drivers.mysql.impls.cqrs.common import execute_insert_sql


def create_customer(uuid, name, age, company_name, created_at):
    sql = (
        f'insert into customers (id, name, age, company_name, created_at) '
        f'values ("{uuid}", "{name}", {age}, "{company_name}", "{created_at}")'
    )
    execute_insert_sql(sql)


def create_event(uuid, name, city, date):
    sql = f'insert into events (id, name, city, date) values ("{uuid}", "{name}", "{city}", "{date}")'
    execute_insert_sql(sql)


def create_order(uuid, amount):
    sql = f'insert into orders (id, amount) values ("{uuid}", {amount})'
    execute_insert_sql(sql)
