from .order import Order
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
        cls.calculate_patron(order)
        # TODO: check if save succeed
        storage.save(order)
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
        return storage.save(order)

    @classmethod
    def calculate_patron(cls, order):
        print("Calculating patron for order {}".format(order.date.isoformat()))
        return False
