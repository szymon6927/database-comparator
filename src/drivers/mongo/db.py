import os

from pymongo import MongoClient
from pymongo.errors import PyMongoError

from src.core.exceptions import MissingEnvVariableError


def get_connection():
    host = os.environ.get('MONGO_HOST', 'localhost')
    port = os.environ.get('MONGO_PORT')
    database = os.environ.get('MONGO_INITDB_DATABASE')
    user = os.environ.get('MONGO_INITDB_ROOT_USERNAME')
    password = os.environ.get('MONGO_INITDB_ROOT_PASSWORD')

    if not all([host, port, database, user, password]):
        raise MissingEnvVariableError(
            'One of these envs not set '
            '[MONGO_HOST, MONGO_PORT, MONGO_INITDB_DATABASE, MONGO_INITDB_ROOT_USERNAME, MONGO_INITDB_ROOT_PASSWORD]'
        )

    try:
        client = MongoClient(host=host, port=int(port), username=user, password=password)
        connection = client[database]
        return connection
    except PyMongoError as e:
        print(f'Error while connecting to MongoDB - {e}')
