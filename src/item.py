import os
import csv
from config import ROOT_PATH


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
        self.name = name

        if not isinstance(price, (float, int)):
            raise ValueError('Значение должно быть числом.')
        elif price < 0:
            raise ValueError('Число должно быть неотрицательным.')
        self.price = price

        if not isinstance(quantity, int):
            raise ValueError('Значение должно быть числом.')
        elif quantity < 0:
            raise ValueError('Число должно быть неотрицательным.')
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            print('Exception: Длина наименования товара превышает 10 символов')
            self.__name = name[:10]

    def __repr__(self):
        """
        Oтображает информацию об объекте класса в режиме отладки
        Возвращает строку в формате "Название класса('название товара', цена товара, количество товара)"
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Отображает информацию об объекте класса для пользователей
        Возвращает строку в формате 'название товара'
        """
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

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_
        """
        cls.all = []
        file_path = os.path.join(ROOT_PATH, 'src', 'items.csv')
        with open(file_path, newline='', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], cls.string_to_number(row['price']), cls.string_to_number(row['quantity']))

    @staticmethod
    def string_to_number(num_str) -> int:
        """
        Статический метод, возвращающий число из числа-строки
        """
        try:
            num = int(num_str)
        except ValueError:
            num = int(float(num_str))
        finally:
            return num
