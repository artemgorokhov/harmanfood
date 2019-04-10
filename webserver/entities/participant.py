from .order_state import get_state


class Participant:
    def __init__(self, username):
        self.username = username
        self.stage = get_state('')
        self.restaurant = None
        self.food = []
        self.price = 0

    def initialize(self, record):
        self.stage = get_state(record.get('stage', ''))
        self.restaurant = record.get('restaurant', None)
        self.food = record.get('food', [])
        self.price = 0

    def as_dict(self):
        return self.__dict__
