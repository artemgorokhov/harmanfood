from .order import Order
from .food import Food
from webserver import emit_order
import webserver.storage as storage_helper
from datetime import date


class OrderManager:

    @classmethod
    def get_order(cls, when=date.today()):
        order = Order(when)
        storage = storage_helper.get_storage()
        if not storage.load_to(order):
            order_id = storage.create_new(order)
            print("created new order, id = {}".format(order_id))
        return order

    @classmethod
    def add_participant(cls, user):
        # TODO: Need to make this operation atomic?
        storage = storage_helper.get_storage()
        order = cls.get_order()
        if order.is_done():
            return False
        participant = order.add_participant(user)
        # In case it was not started, it will be
        order.state_event('start')
        cls.calculate_patron(order)
        if not storage.save(order):
            return False
        emit_order(order.serialize())
        return participant

    @classmethod
    def remove_participant(cls, user):
        # TODO: atomic operation
        storage = storage_helper.get_storage()
        order = cls.get_order()
        if order.is_done():
            return False
        order.remove_participant(user)
        cls.calculate_patron(order)
        if not storage.save(order):
            return False
        emit_order(order.serialize())
        return True

    @classmethod
    def update_participant_dinner(cls, username, dinner):
        """
        username - (String) user login
        dinner - (Dict) list of titles, restaurant and provider
        """
        storage = storage_helper.get_storage()
        order = cls.get_order()
        if order.is_done():
            return None
        # dishes - list of dishes that contains full dish information, including price
        dishes = []
        if dinner['food_list']:
            food_query = Food.dinner_condition(dinner["food_list"], dinner["restaurant"],
                                               dinner["provider"])
            dishes = storage.find(Food, food_query)
        if not order.update_participant_dinner(username, dishes,
                                               dinner["restaurant"], dinner["provider"]):
            return None
        if not storage.save(order):
            return None
        emit_order(order.serialize())
        return dishes

    @classmethod
    def calculate_patron(cls, order):
        if not order.participants:
            print("No patron for order {}".format(order.date.isoformat()))
            return None
        order.patron = order.participants[next(iter(order.participants))]
        print("Patron for order {} is {}".format(order.date.isoformat(), order.patron['username']))
        return order.patron
