"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


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
