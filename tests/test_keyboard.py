import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_str(keyboard):
    assert str(keyboard) == 'Dark Project KD87A'


def test_language(keyboard):
    assert str(keyboard.language) == 'EN'
