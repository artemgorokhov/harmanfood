from .order_state import get_state


class Participant:
    def __init__(self, username):
        self.username = username
        self.stage = get_state('')
        self.restaurant = None

    def initialize(self, record):
        self.stage = get_state(record['stage'])
        self.restaurant = record['restaurant']
