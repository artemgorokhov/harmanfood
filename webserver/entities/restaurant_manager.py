from .restaurant import Restaurant


class RestaurantManager:

    @classmethod
    def get_list(cls, provider=None):
        condition = Restaurant.provider_condition(provider)
