from webserver.provider.burgerking_food_2019_04_19 import burgerking
from webserver.provider.irina_food_2019_04_19 import irina
from webserver.provider.osetinskie_food_2019_04_19 import osetinskie
from webserver.provider.sova_food_2019_04_19 import sova
from webserver.provider.tanuki_food_2019_04_19 import tanuki
from webserver.provider.woking_food_2019_04_19 import woking
from webserver.storage.storage import Storage
from webserver.entities.food import Food


delivery_food = {
    'Burger King': burgerking,
    'Кулинария Ирины Князевой': irina,
    'Осетинские пироги': osetinskie,
    'Еда с совой': sova,
    'Тануки': tanuki,
    'Woking': woking
}

delivery_provider = 'delivery'


def get_categories(rest):
    list_of_categories = []
    if rest not in delivery_food:
        return []
    for dish in delivery_food[rest]:
        category = dish['category']
        if category not in list_of_categories:
            list_of_categories.append(category)
    return list_of_categories


def update_menu(db, rest):
    print("Updating food for {}".format(rest))
    # First deleting all food for certain restaurant
    storage = Storage(db)
    storage.delete(Food, {"provider": delivery_provider, "restaurant": rest})
    # And now insert all food again
    for dish in delivery_food[rest]:
        dish['restaurant'] = rest
        dish['provider'] = delivery_provider
    storage.insert_many(Food, delivery_food[rest])


def update_all(db):
    for rest in delivery_food:
        update_menu(db, rest)
