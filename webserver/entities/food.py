from webserver.storage import DBItem

blank_food = {
    '_id': None,
    'title': '',
    'provider': '',
    'restaurant': '',
    'category': '',
    'price': 0,
    'pic': '',
    'description': '',
    'options': []
}


class Food(DBItem):

    collection = "food"

    def __init__(self, title, provider, restaurant):
        super().__init__(blank_food)
        self.title = title
        self.provider = provider
        self.restaurant = restaurant

    @property
    def unique_condition(self):
        return {"title": self.title, "provider": self.provider, "restaurant": self.restaurant}

    def initialize(self, record):
        if not record:
            return False
        for key in record:
            self.__dict__[key] = record[key]

    @classmethod
    def dinner_condition(cls, dinner, restaurant, provider):
        return {
            "$or": dinner,
            "restaurant": restaurant,
            "provider": provider
        }
