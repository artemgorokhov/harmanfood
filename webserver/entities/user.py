from webserver.storage import DBItem
from passlib.hash import pbkdf2_sha256


blank_user = {
    '_id': None,
    'username': '',
    'firstName': '',
    'lastName': '',
    'email': '',
    'pwdHash': '',
    'phone': '',
    'admin': False,
    'privilege': False,
    'pwdReset': False
}


class User(DBItem):

    collection = "eaters"

    def __init__(self, username):
        super().__init__(blank_user)
        self.username = username

    def keys(self):
        return tuple(self.__dict__)

    @property
    def unique_condition(self):
        return {"username": self.username}

    @property
    def full_name(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def initialize(self, record):
        if not record:
            return False
        for key in record:
            self.__dict__[key] = record[key]
        return True

    def __repr__(self):
        return str(self.__dict__)

    @classmethod
    def generate_password_hash(cls, password):
        return pbkdf2_sha256.encrypt(password, rounds=100, salt_size=16)

    @DBItem.is_initialized
    def verify_password(self, password):
        print("verifying the password {}".format(password))
        try:
            return pbkdf2_sha256.verify(password, self.pwdHash)
        except ValueError:
            return False

    @DBItem.is_initialized
    def password_to_be_reset(self, password):
        if self.pwdReset:
            self.pwdHash = self.generate_password_hash(password)
            self.pwdReset = False
            return True
        return False
