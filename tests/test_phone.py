import pytest
from src.phone import Phone


@pytest.fixture
def samsung():
    return Phone('samsung', 900, 10, 2)


def test_phone_number_of_sim(samsung):
    with pytest.raises(ValueError):
        Phone('samsung', 900, 10, 1.55)
        Phone('samsung', 900, 10, 0)
    assert samsung.number_of_sim == 2


def test_str(samsung):
    assert str(samsung) == 'samsung'


def test_repr(samsung):
    assert repr(samsung) == "Phone('samsung', 900, 10, 2)"
