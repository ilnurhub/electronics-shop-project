from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        if not isinstance(number_of_sim, int):
            raise ValueError('Значение должно быть числом.')
        self.number_of_sim = number_of_sim

    def __repr__(self):
        """
        Oтображает информацию об объекте класса в режиме отладки
        Возвращает строку в формате "Название класса('название товара', цена товара, количество товара, количество симкарт)"
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if number_of_sim < 1:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.__number_of_sim = number_of_sim
