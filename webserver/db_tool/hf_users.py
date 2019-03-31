from webserver.entities import User
from webserver.storage import Storage

user_records = {
    'Artem.Gorokhov': {
        'firstName': 'Артём',
        'lastName': 'Горохов',
        'phone': '+79519020046',
        'email': 'Artem.Gorokhov@harman.com',
        'admin': True,
    },
    'Dmitry.Loganov': {
        'firstName': 'Дмитрий',
        'lastName': 'Логанов',
        'phone': '+79875573518',
        'email': 'Dmitry.Loganov@harman.com'
    },
    'Alexey.Kanaev': {
        'firstName': 'Алексей',
        'lastName': 'Канаев',
        'phone': '+79506160525',
        'email': 'Alexey.Kanaev@harman.com'
    },
    'Oleg.Slepov': {
        'firstName': 'Олег',
        'lastName': 'Слепов',
        'phone': '+79875349408',
        'email': 'Oleg.Slepov@harman.com'
    },
    'Olga.Popova': {
        'firstName': 'Ольга',
        'lastName': 'Попова',
        'phone': '+79159351092',
        'email': 'Olga.Popova@harman.com'
    },
    'Igor.Reutov': {
        'firstName': 'Игорь',
        'lastName': 'Реутов',
        'phone': '+79601694625',
        'email': 'Igor.Reutov@harman.com'
    },
    'Galina.Shubina': {
        'firstName': 'Галина',
        'lastName': 'Шубина',
        'phone': '+79308088892',
        'email': 'Galina.Shubina@harman.com'
    }
}


def update():
    for username, record in user_records.items():
        user = User(username.lower())
        user.initialize(record)
        print(user.as_dict())
        print('{}: {}'.format(username, Storage.save(user)))
