import json
import logging
import os

import redis

from onyx.util.StructMessage import StructMessage


class StorageEntity:
    def __init__(self, db=0):
        self.host = os.getenv('ONYX_REDIS_HOST', 'localhost')
        self.port = int(os.getenv('ONYX_REDIS_PORT', '6379'))
        self.db = db

    @staticmethod
    def exists(identifier):
        logging.info(StructMessage(message='Checking existence of identifier', identifier=identifier))

        storage = StorageEntity()
        return redis.Redis(decode_responses=True, host=storage.host, port=storage.port, db=storage.db).exists(identifier) == 1

    @staticmethod
    def load(identifier):
        logging.info(StructMessage(message='Fetching qr content', identifier=identifier))

        storage = StorageEntity()
        return json.loads(redis.Redis(decode_responses=True, host=storage.host, port=storage.port, db=storage.db).get(identifier))

    @staticmethod
    def save(identifier, value):
        logging.info(StructMessage(message='Saving qr content', identifier=identifier, value=value))

        storage = StorageEntity()
        return redis.Redis(host=storage.host, port=storage.port, db=storage.db).set(identifier, json.dumps(value))

    @staticmethod
    def delete(identifier):
        logging.info(StructMessage(message='Fetching qr content', identifier=identifier))

        storage = StorageEntity()
        return redis.Redis(host=storage.host, port=storage.port, db=storage.db).delete(identifier)
