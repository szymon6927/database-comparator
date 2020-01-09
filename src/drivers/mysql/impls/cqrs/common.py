from mysql.connector import Error

from src.drivers.mysql.db import get_connection

db_session = get_connection()


def execute_sql(sql: str, many=True):
    try:
        cursor = db_session.cursor(dictionary=True)
        cursor.execute(sql)
        records = cursor.fetchall() if many else cursor.fetchone()

        return records
    except Error as e:
        print(f'Failed to get record from MySQL table - {e}')


def execute_insert_sql(sql: str):
    try:
        cursor = db_session.cursor()
        cursor.execute(sql)
        db_session.commit()
    except Error as e:
        print(f'Failed to insert record into table - {e}')