from .db_item import DBItem


class Storage:

    def __init__(self, db):
        self.db = db
        self.collections = {
            'eaters': db.eaters,
            'restaurants': db.restaurants
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
            return False
        return item.initialize(collection.find_one(item.unique_condition))

    def create_new(self, item):
        collection = self.collections.get(item.collection, None)
        if not collection:
            return False
        return collection.insert_one(item.as_dict()).inserted_id

    def save(self, item):
        collection = self.collections.get(item.collection, None)
        if not collection:
            return False
        return collection.find_one_and_update(item.unique_condition,
                                              {"$set": item.as_dict()},
                                              upsert=(item.get_id() is None))

    def find(self, dbitemClass, condition=None):
        collection = self.collections.get(dbitemClass.collection, None)
        if not collection:
            return False
        cursor = collection.find(condition, projection={'_id': False})
        result = []
        for d in cursor:
            result.append(d)
        return result
