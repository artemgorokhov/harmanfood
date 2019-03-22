from webserver.storage import DBItem


blank_user = {
    '_id': None,
    'username': '',
    'firstName': '',
    'lastName': '',
    'pwdHash': '',
    'phone': '',
    'admin': False,
    'privilege': False,
    'pwdReset': False
}


class User(DBItem):

    def __init__(self, username):
        super().__init__(blank_user)
        self.username = username

    @DBItem.is_initialized
    def check_password(self, pwd):
        if self.pwdReset is True:
            print("I'll register you")
            return True
        print("Checking your password")
        return True

    def keys(self):
        return tuple(self.__dict__)

    @property
    def collection(self):
        return "eaters"

    @property
    def unique_condition(self):
        return {"username": self.username}

    def initialize(self, record):
        if not record:
            return False
        for key in record:
            self.__dict__[key] = record[key]
        return True

    def __repr__(self):
        return str(self.__dict__)
