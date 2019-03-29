from webserver.storage import DBItem

blank_restaurant = {
    '_id': None,
    'title': '',
    'provider': '',
    'asset': ''
}


class Restaurant(DBItem):

    def __init__(self, title, provider):
        super().__init__(blank_restaurant)
        self.title = title
        self.provider = provider

    @property
    def collection(self):
        return "restaurants"

    @property
    def unique_condition(self):
        return {"title": self.title, "provider": self.provider}

    def initialize(self, record):
        if not record:
            return False
        for key in record:
            self.__dict__[key] = record[key]
