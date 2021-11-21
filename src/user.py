class User:
    def __init__(self):
        self.__name = None
        self.__favorite_restaurant = None

    @property
    def name(self):
        return self.__name

    @property
    def favorite_restaurant(self):
        return self.__favorite_restaurant

    @name.setter
    def name(self, name: str):
        self.__name = name

    @favorite_restaurant.setter
    def favorite_restaurant(self, favorite_restaurant: str):
        self.__favorite_restaurant = favorite_restaurant
