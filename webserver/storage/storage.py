from .db_item import DBItem
from pymongo import ReturnDocument


class Storage:

    def __init__(self, db):
        self.db = db
        self.collections = {
            'eaters': db.eaters,
            'restaurants': db.restaurants,
            'orders': db.orders,
            'food': db.food
        }

    def insert(self, item):
        if not isinstance(item, DBItem):
            return None
        return 1

    def update(self, item, fields):
        """ Updates certain fields of item """
        collection = self.collections.get(item.collection, None)
        if not collection:
            return None
        itemset = {}
        for field in fields:
            if hasattr(item, field):
                itemset[field] = getattr(item, field)
        if not itemset:
            return None
        print('UPDATING: {}'.format(itemset))
        return collection.find_one_and_update(item.unique_condition,
                                              {"$set": itemset},
                                              return_document=ReturnDocument.AFTER)

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

    def delete(self, db_item_class, condition=None):
        collection = self.collections.get(db_item_class.collection, None)
        if not collection:
            return False
        if not condition:
            print("WARNING! Removing all documents from {}".format(db_item_class.collection))
            condition = {}
        x = collection.delete_many(condition)
        print("Deleted {} documents from {} collection".format(x.deleted_count, db_item_class.collection))

    def insert_many(self, db_item_class, items):
        collection = self.collections.get(db_item_class.collection, None)
        if not collection:
            return False
        if not items:
            print("No items to insert to {}".format(db_item_class.collection))
            return False
        result = collection.insert_many(items)
        print("Inserted {} items".format(len(result.inserted_ids)))
        return len(result.inserted_ids) > 0
