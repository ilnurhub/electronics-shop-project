"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def iphone():
    return Item('iphone', 1000, 5)


def test_item_name_not_str():
    with pytest.raises(ValueError):
        Item(12344, 15.0, 5)
        Item(12344.0, 15.0, 5)
        Item(['car', 'phone'], 15.0, 5)


def test_item_price():
    with pytest.raises(ValueError):
        Item('phone', 'abc', 5)
        Item('phone', [15], 5)


def test_item_price_negative():
    with pytest.raises(ValueError):
        Item('phone', -15.0, 5)


def test_item_quantity():
    with pytest.raises(ValueError):
        Item('phone', 1000.0, 'five')
        Item('phone', 1000.0, [5, 10])


def test_item_quantity_negative():
    with pytest.raises(ValueError):
        Item('phone', 1000.0, -5)


def test_item_calculate_total_price(iphone):
    assert iphone.calculate_total_price() == 5000.0


def test_item_apply_discount(iphone):
    iphone.apply_discount()
    assert iphone.price == 1000.0
    Item.pay_rate = 0.8
    iphone.apply_discount()
    assert iphone.price == 800.0


def test_getter_name(iphone):
    assert iphone.name == 'iphone'
