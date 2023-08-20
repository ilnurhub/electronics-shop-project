class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        if not isinstance(name, str):
            raise ValueError('Значение должно быть строкой.')
        self.__name = name

        if not isinstance(price, (float, int)):
            raise ValueError('Значение должно быть числом.')
        elif price < 0:
            raise ValueError('Число должно быть неотрицательным.')
        self.price = float(price)

        if not isinstance(quantity, (int, float)):
            raise ValueError('Значение должно быть числом.')
        elif quantity < 0:
            raise ValueError('Число должно быть неотрицательным.')

        self.quantity = int(quantity)
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate
