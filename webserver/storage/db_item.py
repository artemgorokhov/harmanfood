from abc import abstractmethod
from functools import wraps


class DBItem:

    def __init__(self, contract):
        self.__dict__.update(contract)

    def __setattr__(self, key, value):
        print("Set attr {}: {}".format(key, value))
        if key in self.__dict__:
            super().__setattr__(key, value)
        else:
            raise AttributeError('{} has no attribute {}'.format(self.__class__.__name__, key))

    @property
    @abstractmethod
    def collection(self):
        """Mongo collection that stores these items"""

    @property
    @abstractmethod
    def unique_condition(self):
        """Dictionary that can be used as a find_one condition to get from MongoDB"""

    @abstractmethod
    def initialize(self, record):
        """Each DBItem must be able to initialize itself by using a dict record from database"""

    def get_id(self):
        return self._id

    @staticmethod
    def is_initialized(func):
        @wraps(func)
        def wrapper(*args, **kwds):
            if not args[0].get_id():
                return None
            return func(*args, **kwds)

        return wrapper

    def as_dict(self):
        return {key: value for (key, value) in self.__dict__.items() if key != '_id'}
