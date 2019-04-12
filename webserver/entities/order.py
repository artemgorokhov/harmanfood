from webserver.storage import DBItem
from datetime import date
from .order_state import get_state, ClosedState
from .error import EntityError


blank_order = {
    '_id': None,
    'date': None,
    'participants': {},
    'patron': None,
    'state': None
}


class Order(DBItem):

    collection = "order"
    
    def __init__(self, when=date.today()):
        super().__init__(blank_order)
        self.date = when

    @property
    def unique_condition(self):
        return {"date": self.date}

    @property
    def total(self):
        _total = 0
        for _participant in self.participants:
            _total = _total + _participant.price
        return _total

    def initialize(self, record):
        if not record:
            return False
        for key in record:
            if key == 'state':
                self.state = get_state(record['state'])
            else:
                self.__dict__[key] = record[key]
        return True

    def on_event(self, event):
        if self.state is None:
            raise EntityError("Trying to change state of uninitialized order")
        self.state = self.state.on_event(event)

    def add_participant(self, user):
        username = user.username
        if username in self.participants:
            print("Participant already there")
            return self.participants[username]
        participant = {
            'name': user.full_name,
            'stage': get_state(''),
            'food': [],
            'restaurant': None
        }
        self.participants[username] = participant
        print("Returning participant {}".format(participant))
        return participant

    def get_participant(self, user):
        return self.participants.get(user.username, {})

    def remove_participant(self, user):
        username = user.username
        if username not in self.participants:
            return
        del self.participants[username]

    def is_done(self):
        return isinstance(self.state, ClosedState)

    def get_state(self):
        return None if self.state is None else str(self.state)

    def as_dict(self):
        d = {}
        for (key, value) in self.__dict__.items():
            if key == '_id':
                continue
            elif key == 'state':
                d[key] = self.get_state()
            else:
                d[key] = value
        return d
