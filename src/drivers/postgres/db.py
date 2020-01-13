import os

import psycopg2

from src.core.exceptions import MissingEnvVariableError


def get_connection():
    host = os.environ.get('POSTGRES_HOST', 'localhost')
    port = os.environ.get('POSTGRES_PORT')
    database = os.environ.get('POSTGRES_DB')
    user = os.environ.get('POSTGRES_USER')
    password = os.environ.get('POSTGRES_PASSWORD')

    if not all([host, port, database, user, password]):
        raise MissingEnvVariableError(
            'One of these envs not set [POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD]'
        )

    try:
        connection = psycopg2.connect(host=host, user=user, password=password, database=database, port=port)
        return connection
    except psycopg2.DatabaseError as e:
        print(f'Error while connecting to PostgreSQL - {e}')
