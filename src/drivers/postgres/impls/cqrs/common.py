import psycopg2
import psycopg2.extras

from src.drivers.postgres.db import get_connection


def execute_sql(sql: str, params: tuple = None, many=True):
    db_session = get_connection()

    try:
        cursor = db_session.cursor(cursor_factory=psycopg2.extras.DictCursor)

        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)

        records = cursor.fetchall() if many else cursor.fetchone()

        return records
    except psycopg2.DatabaseError as e:
        print(f'Failed to get record from PostgreSQL table - {e}')


def execute_insert_sql(sql: str, params: tuple):
    db_session = get_connection()

    try:
        cursor = db_session.cursor()
        cursor.execute(sql, params)
        db_session.commit()
    except psycopg2.DatabaseError as e:
        print(f'Failed to insert record into table - {e}')
