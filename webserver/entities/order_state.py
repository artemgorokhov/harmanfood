from abc import abstractmethod


def get_state(state_id):
    for state_klass in OrderState.__subclasses__():
        if state_id == state_klass.state_id:
            return state_klass()
    return NotStartedState()


class OrderState:
    def __init__(self):
        """
        Base class for order states
        """
        print("Current state: {}".format(self))

    @property
    @abstractmethod
    def state_id(self):
        pass

    @abstractmethod
    def on_event(self, event):
        pass

    def __str__(self):
        return self.state_id

    def __repr__(self):
        return self.__str__()


class NotStartedState(OrderState):
    @property
    def state_id(self):
        return 'not started'

    def on_event(self, event):
        if event == 'start':
            return RestaurantState()
        return self


class RestaurantState(OrderState):
    @property
    def state_id(self):
        return 'choosing restaurant'

    def on_event(self, event):
        if event == 'restaurant_selected':
            return MenuState()
        return self


class MenuState(OrderState):
    @property
    def state_id(self):
        return 'choosing food'

    def on_event(self, event):
        if event == 'menu_selected':
            return DeliveryState()
        return self


class DeliveryState(OrderState):
    @property
    def state_id(self):
        return 'delivering'

    def on_event(self, event):
        if event == 'delivered':
            return PaymentState()
        return self


class PaymentState(OrderState):
    @property
    def state_id(self):
        return 'payment'

    def on_event(self, event):
        if event == 'paid':
            return ClosedState()
        return self


class ClosedState(OrderState):
    @property
    def state_id(self):
        return 'closed'

    def on_event(self, event):
        return self
