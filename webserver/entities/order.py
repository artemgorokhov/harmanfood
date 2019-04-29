from webserver.storage import DBItem
import datetime
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

    collection = "orders"

    def __init__(self, when=datetime.date.today()):
        # Have to use date with time as pymongo does not accept date without time
        when = datetime.datetime.combine(when, datetime.time.min)
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
            'username': user.username,
            'fullName': user.full_name,
            'firstName': user.firstName,
            'lastName': user.lastName,
            'phone': user.phone,
            'phase': str(get_state('choosing restaurant')),
            'food': [],
            'restaurant': None,
            'provider': None,
            'total': 0
        }
        print("NEW PARTICIPANT: {}".format(participant))
        self.participants[username] = participant
        return participant

    def update_participant_dinner(self, username, dinner):
        p = self.get_participant(username)
        if not p:
            return False
        p['food'] = list(dinner["food_list"])
        p["restaurant"] = dinner["restaurant"]
        p["provider"] = dinner["provider"]
        return True

    def get_participant(self, username):
        return self.participants.get(username, {})

    def remove_participant(self, user):
        username = user.username
        if username not in self.participants:
            return
        del self.participants[username]

    def is_done(self):
        return isinstance(self.state, ClosedState)

    def state_event(self, event):
        self.state = self.state.on_event(event)

    def get_state(self):
        return None if self.state is None else str(self.state)

    def as_dict(self):
        d = {}
        for (key, value) in self.__dict__.items():
            if key == '_id':
                continue
            elif key == 'state':
                d[key] = str(self.get_state())
            else:
                d[key] = value
        return d

    def serialize(self, myusername=None):
        d = self.as_dict()
        d['date'] = d['date'].strftime('%d-%m-%Y')
        participant_list = []
        for username in self.participants:
            idx = len(participant_list)
            if myusername == username:
                idx = 0
            participant_list.insert(idx, self.participants[username])
        d['participants'] = participant_list
        if self.patron:
            d['patron'] = {
                'firstName': self.patron['firstName'],
                'lastName': self.patron['lastName'],
                'phone': self.patron['phone']
            }
            d['iampatron'] = True if myusername == self.patron['username'] else False
        else:
            d['patron'] = None
            d['iampatron'] = False
        return d
