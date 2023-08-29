from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        if not isinstance(number_of_sim, int):
            raise ValueError('Значение должно быть числом.')
        elif number_of_sim < 1:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self.number_of_sim = number_of_sim
