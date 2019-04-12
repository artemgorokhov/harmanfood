from .db_item import DBItem
from pymongo import ReturnDocument


class Storage:

    def __init__(self, db):
        self.db = db
        self.collections = {
            'eaters': db.eaters,
            'restaurants': db.restaurants,
            'orders': db.orders
        }

    def insert(self, item):
        if not isinstance(item, DBItem):
            return None
        return 1

    def update(self, item):
        if not isinstance(item, DBItem):
            return None
        return 1

    def load_to(self, item):
        collection = self.collections.get(item.collection, None)
        if not collection:
            raise RuntimeError('No collection {}'.format(item.collection))
        return item.initialize(collection.find_one(item.unique_condition))

    def create_new(self, item):
        collection = self.collections.get(item.collection, None)
        if not collection:
            return None
        return collection.insert_one(item.as_dict()).inserted_id

    def save(self, item):
        collection = self.collections.get(item.collection, None)
        if not collection:
            return None
        print('SAVING: {}'.format(item.as_dict()))
        return collection.find_one_and_update(item.unique_condition,
                                              {"$set": item.as_dict()},
                                              upsert=(item.get_id() is None),
                                              return_document=ReturnDocument.AFTER)

    def find(self, db_item_class, condition=None):
        collection = self.collections.get(db_item_class.collection, None)
        if not collection:
            return False
        cursor = collection.find(condition, projection={'_id': False})
        result = []
        for d in cursor:
            result.append(d)
        return result
