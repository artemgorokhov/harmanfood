from webserver.storage import DBItem
from datetime import date


blank_order = {
    '_id': None,
    'date': None,
    'participants': set(),
    'breadwinner': None,
    'done': False
}


class Order(DBItem):

    db_collection = "order"
    
    def __init__(self, when=date.today()):
        super().__init__(blank_order)
        self.date = when

    @property
    def unique_condition(self):
        return {"date": self.date}

    def initialize(self, record):
        if not record:
            return False
        for key in record:
            self.__dict__[key] = record[key]
        return True

    def add_participant(self, user):
        username = user.username
        self.participants.add(username)

    def remove_participant(self, user):
        username = user.username
        if username not in self.participants:
            return
        self.participants.remove(username)

    def is_done(self):
        return self.done or (self.date != date.today())
