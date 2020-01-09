from mysql.connector import Error

from src.mysql_dirver.db import get_connection

db_session = get_connection()


def execute_sql(sql: str, many=True):
    try:
        cursor = db_session.cursor(dictionary=True)
        cursor.execute(sql)
        records = cursor.fetchall() if many else cursor.fetchone()

        return records
    except Error as e:
        print(f'Failed to get record from MySQL table - {e}')
