from .order import Order
from webserver.storage import Storage
from datetime import date


class OrderManager:

    @classmethod
    def get_order(cls, when=date.today()):
        order = Order(when)
        if not Storage.load_to(order):
            Storage.create_new(order)
        return order

    @classmethod
    def add_participant(cls, user):
        # TODO: Need to make this operation atomic (with redis)!!!
        order = cls.get_order()
        if order.is_done():
            return False
        order.add_participant(user)
        cls.calculate_breadwinner(order)
        return Storage.save(order)

    @classmethod
    def remove_participant(cls, user):
        # TODO: atomic operation
        order = cls.get_order()
        if order.is_done():
            return False
        order.remove_participant(user)
        cls.calculate_breadwinner(order)
        return Storage.save(order)

    @classmethod
    def calculate_breadwinner(cls, order):
        print("Calculating breadwinner for order {}".format(order.date.isoformat()))
        return False
