from src.mysql_dirver.impls.cqrs.common import execute_sql


def get_all_customers():
    sql = "select * from customers"
    return execute_sql(sql)
