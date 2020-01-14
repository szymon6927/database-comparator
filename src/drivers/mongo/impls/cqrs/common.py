from pymongo.errors import PyMongoError

from src.drivers.mongo.db import get_connection


def execute_mongo(collection_name: str, params: dict, many=True):
    db_session = get_connection()
    collection = db_session[collection_name]

    try:
        if many:
            records = list(collection.find(params))
            for record in records:
                del record['_id']
        else:
            records = collection.find_one(params)
            del records['_id']

        return records
    except PyMongoError as e:
        print(f'Failed to get record from MongoDB table - {e}')


def execute_insert_mongo(collection_name: str, params: dict):
    db_session = get_connection()
    collection = db_session[collection_name]

    try:
        collection.insert_one(params)
    except PyMongoError as e:
        print(f'Failed to insert record into table - {e}')
