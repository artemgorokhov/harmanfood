from webserver.entities import User
from webserver.storage import Storage

u = User('artem.gorokhov')
Storage.load_to(u)

print("User: {}".format(u))
print(u.check_password(''))

