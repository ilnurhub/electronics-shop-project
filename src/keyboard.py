from src.item import Item


class MixinLang:
    pass


class Keyboard(Item, MixinLang):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
