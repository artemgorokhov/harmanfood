from abc import abstractmethod


def get_state(state_id):
    for state_klass in OrderState.__subclasses__():
        print('Searching {} == {}'.format(state_id, state_klass.state_id))
        if state_id == state_klass.state_id:
            return state_klass()
    return NotStartedState()


class OrderState:
    def __init__(self):
        """
        Base class for order states
        """
        print("Current state: {}".format(self))

    @abstractmethod
    def on_event(self, event):
        pass

    def __str__(self):
        return self.state_id

    def __repr__(self):
        return self.__str__()


class NotStartedState(OrderState):
    state_id = 'not started'

    def on_event(self, event):
        if event == 'start':
            return RestaurantState()
        return self


class RestaurantState(OrderState):
    state_id = 'choosing restaurant'

    def on_event(self, event):
        if event == 'restaurant_selected':
            return MenuState()
        return self


class MenuState(OrderState):
    state_id = 'choosing food'

    def on_event(self, event):
        if event == 'menu_selected':
            return DeliveryState()
        return self


class DeliveryState(OrderState):
    state_id = 'delivering'

    def on_event(self, event):
        if event == 'delivered':
            return PaymentState()
        return self


class PaymentState(OrderState):
    state_id = 'payment'

    def on_event(self, event):
        if event == 'paid':
            return ClosedState()
        return self


class ClosedState(OrderState):
    state_id = 'closed'

    def on_event(self, event):
        return self
