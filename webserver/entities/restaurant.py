from webserver.storage import DBItem

blank_restaurant = {
    '_id': None,
    'title': '',
    'provider': '',
    'asset': '',
    'food_hash': '',
    'orders': 0
}


class Restaurant(DBItem):

    collection = "restaurants"

    def __init__(self, title, provider):
        super().__init__(blank_restaurant)
        self.title = title
        self.provider = provider
        

    @property
    def unique_condition(self):
        return {"title": self.title, "provider": self.provider}

    def initialize(self, record):
        if not record:
            return False
        for key in record:
            self.__dict__[key] = record[key]

    @classmethod
    def provider_condition(cls, provider):
        if provider is None:
            return None
        return {'provider': provider}
