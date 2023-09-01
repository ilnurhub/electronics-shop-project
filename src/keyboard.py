from src.item import Item


class MixinLang:
    def __init__(self):
        self.__language = 'EN'

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self

    @property
    def language(self):
        return self.__language


class Keyboard(Item, MixinLang):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
