class User:
    def __init__(self):
        self.__name = None
        self.__favorite_restlan = None

    @property
    def name(self):
        return self.__name

    @property
    def favorite_restlan(self):
        return self.__favorite_restlan

    @name.setter
    def name(self, name: str):
        self.__name = name

    @favorite_restlan.setter
    def favorite_restlan(self, favorite_restlan: str):
        self.__favorite_restlan = favorite_restlan
