import os

import mysql.connector
from mysql.connector import Error

from src.core.exceptions import MissingEnvVariableError


def get_connection():
    host = os.environ.get('MYSQL_HOST', 'localhost')
    port = os.environ.get('MYSQL_PORT', 4306)
    database = os.environ.get('MYSQL_DATABASE')
    user = os.environ.get('MYSQL_USER')
    password = os.environ.get('MYSQL_PASSWORD')

    if not all([host, database, user, password]):
        raise MissingEnvVariableError(
            'One of these env variables not set ' '[MYSQL_HOST, MYSQL_PORT, MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD]'
        )

    try:
        connection = mysql.connector.connect(host=host, port=port, database=database, user=user, password=password)
        return connection
    except Error as e:
        print(f'Error while connecting to MySQL - {e}')
