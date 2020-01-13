from src.drivers.postgres.impls.cqrs.common import execute_insert_sql


def create_customer(uuid, name, age, company_name, created_at):
    sql = f'insert into customers (id, name, age, company_name, created_at) ' f'values (%s, %s, %s, %s, %s)'
    params = (f'{uuid}', f'{name}', age, f'{company_name}', f'{created_at}')

    execute_insert_sql(sql, params)


def create_event(uuid, name, city, date):
    sql = f'insert into events (id, name, city, date) values (%s, %s, %s, %s)'
    params = (f'{uuid}', f'{name}', f'{city}', f'{date}')

    execute_insert_sql(sql, params)


def create_order(uuid, amount):
    sql = f'insert into orders (id, amount) values (%s, %s)'
    params = (f'{uuid}', amount)

    execute_insert_sql(sql, params)
