from pymongo import MongoClient
from .db_item import DBItem


class Storage:
    client = MongoClient()
    db = client.harmanfood

    # Collections
    collections = {
        'eaters': db.eaters
    }

    def __init__(self):
        print('Initializing Storage instance')

    @staticmethod
    def insert(item):
        if not isinstance(item, DBItem):
            return None
        return 1

    @staticmethod
    def update(item):
        if not isinstance(item, DBItem):
            return None
        return 1

    @classmethod
    def load_to(cls, item):
        collection = cls.collections.get(item.collection, None)
        if not collection:
            return False
        return item.initialize(collection.find_one(item.unique_condition))

    @classmethod
    def create_new(cls, item):
        collection = cls.collections.get(item.collection, None)
        if not collection:
            return False
        return collection.insert_one(item.as_dict()).inserted_id

    @classmethod
    def save(cls, item):
        collection = cls.collections.get(item.collection, None)
        if not collection:
            return False
        return collection.find_one_and_update(item.unique_condition, item.as_dict())
