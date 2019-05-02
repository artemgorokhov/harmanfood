from functools import wraps
from webserver.storage import DBItem
import datetime
from .order_state import get_state, change_state, ClosedState
from .error import OrderError


blank_order = {
    '_id': None,
    'date': None,
    'participants': {},
    'patron': None,
    'stage': None
}


def order_in_progress(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if args[0].is_done():
            raise OrderError("Can't update finished order")
        stage = get_state(args[0].stage)
        if stage.is_immutable():
            raise OrderError("Can't update immutable order")
        return f(*args, **kwargs)
    return decorated


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
            self.__dict__[key] = record[key]
        return True

    @order_in_progress
    def add_participant(self, user):
        if self.is_done():
            raise OrderError("Can't update finished order")
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
            'stage': 'ChoosingPlace',
            'food': [],
            'restaurant': None,
            'provider': None,
            'total': 0
        }
        print("NEW PARTICIPANT: {}".format(participant))
        self.participants[username] = participant
        return participant

    @order_in_progress
    def update_participant_dinner(self, username, dishes, restaurant, provider):
        p = self.get_participant(username)
        if not p:
            return None
        p["food"] = list(dishes) if dishes else []
        event_name = 'restaurant_selected'
        if not p["food"]:
            event_name = 'menu_declined'
        p["stage"] = change_state(p["stage"], event_name)
        p["restaurant"] = restaurant
        p["provider"] = provider
        total = 0
        for dish in dishes:
            total += int(dish["price"])
        p["total"] = total
        return p

    def get_participant(self, username):
        return self.participants.get(username, {})

    @order_in_progress
    def remove_participant(self, user):
        if self.is_done():
            raise OrderError("Can't update finished order")
        username = user.username
        if username not in self.participants:
            return
        del self.participants[username]

    def is_done(self):
        return isinstance(self.stage, ClosedState)

    def state_event(self, event):
        self.stage = change_state(self.stage, event)

    def get_state(self):
        return None if self.stage is None else str(self.stage)

    def as_dict(self):
        d = {}
        for (key, value) in self.__dict__.items():
            if key == '_id':
                continue
            elif key == 'stage':
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
