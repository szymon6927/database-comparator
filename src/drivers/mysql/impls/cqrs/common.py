from mysql.connector import Error

from src.drivers.mysql.db import get_connection


def execute_sql(sql: str, many=True):
    db_session = get_connection()

    try:
        cursor = db_session.cursor(dictionary=True)
        cursor.execute(sql)
        records = cursor.fetchall() if many else cursor.fetchone()

        return records
    except Error as e:
        print(f'Failed to get record from MySQL table - {e}')


def execute_insert_or_delete_sql(sql: str):
    db_session = get_connection()

    try:
        cursor = db_session.cursor()
        cursor.execute(sql)
        db_session.commit()
    except Error as e:
        print(f'Failed to insert record into table - {e}')
