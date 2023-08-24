"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def iphone():
    return Item('iphone', 1000, 5)


def test_item_name_not_str():
    with pytest.raises(ValueError):
        Item(12344, 15, 5)
        Item(12344.0, 15, 5)
        Item(['car', 'phone'], 15, 5)


def test_item_price():
    with pytest.raises(ValueError):
        Item('phone', 'abc', 5)
        Item('phone', [15], 5)


def test_item_price_negative():
    with pytest.raises(ValueError):
        Item('phone', -15, 5)


def test_item_quantity():
    with pytest.raises(ValueError):
        Item('phone', 1000, 'five')
        Item('phone', 1000, [5, 10])


def test_item_quantity_negative():
    with pytest.raises(ValueError):
        Item('phone', 1000, -5)


def test_item_calculate_total_price(iphone):
    assert iphone.calculate_total_price() == 5000


def test_item_apply_discount(iphone):
    iphone.apply_discount()
    assert iphone.price == 1000.0
    Item.pay_rate = 0.8
    iphone.apply_discount()
    assert iphone.price == 800.0


def test_getter_name(iphone):
    assert iphone.name == 'iphone'


def test_setter_name_less_ten(iphone):
    iphone.name = 'Iphone'
    assert iphone.name == 'Iphone'


def test_setter_name_over_ten(iphone):
    iphone.name = 'Iphone_smartphone'
    assert iphone.name == 'Iphone_sma'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_repr(iphone):
    assert repr(iphone) == "Item('iphone', 1000, 5)"

