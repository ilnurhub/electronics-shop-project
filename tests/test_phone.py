import pytest
from src.phone import Phone
from src.item import Item


@pytest.fixture
def samsung():
    return Phone('samsung', 900, 10, 2)


@pytest.fixture
def iphone():
    return Item('iphone', 1000, 5)


def test_phone_number_of_sim(samsung):
    with pytest.raises(ValueError):
        Phone('samsung', 900, 10, 1.55)
        Phone('samsung', 900, 10, 0)
    assert samsung.number_of_sim == 2


def test_str(samsung):
    assert str(samsung) == 'samsung'


def test_repr(samsung):
    assert repr(samsung) == "Phone('samsung', 900, 10, 2)"


def test_change_number_of_sim(samsung):
    with pytest.raises(ValueError):
        samsung.number_of_sim = 0


def test_add_quantity(samsung, iphone):
    assert iphone + samsung == 15
    assert samsung + iphone == 15
    assert samsung + samsung == 20
    with pytest.raises(ValueError):
        assert samsung + 100 == 110
