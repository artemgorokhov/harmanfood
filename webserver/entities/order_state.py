from abc import abstractmethod


def change_state(state_id, event_name):
    state = get_state(state_id)
    state = state.on_event(event_name)
    return str(state)


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
        print("Current stage: {}".format(self))

    @abstractmethod
    def on_event(self, event):
        pass

    def is_immutable(self):
        return self.immutable

    def __str__(self):
        return self.state_id

    def __repr__(self):
        return self.__str__()


class NotStartedState(OrderState):
    state_id = 'NotStarted'
    immutable = False

    def on_event(self, event):
        if event == 'start':
            return RestaurantState()
        elif event == 'declined':
            return DeclinedState()
        return self


class RestaurantState(OrderState):
    state_id = 'ChoosingPlace'
    immutable = False

    def on_event(self, event):
        if event == 'restaurant_selected':
            return MenuState()
        elif event == 'declined':
            return DeclinedState()
        return self


class MenuState(OrderState):
    state_id = 'ComposingDinner'
    immutable = False

    def on_event(self, event):
        if event == 'menu_selected':
            return DeliveryState()
        elif event == 'menu_declined':
            return RestaurantState()
        elif event == 'declined':
            return DeclinedState()
        return self


class DeliveryState(OrderState):
    state_id = 'Delivery'
    immutable = True

    def on_event(self, event):
        if event == 'delivered':
            return PaymentState()
        elif event == 'declined':
            return DeclinedState()
        return self


class PaymentState(OrderState):
    state_id = 'payment'
    immutable = True

    def on_event(self, event):
        if event == 'paid':
            return ClosedState()
        return self


class ClosedState(OrderState):
    state_id = 'closed'
    immutable = True

    def on_event(self, event):
        return self


class DeclinedState(OrderState):
    state_id = 'Declined'
    immutable = True

    def on_event(self, event):
        return self
