import pytest
from src.phone import Phone


@pytest.fixture
def samsung():
    return Phone('samsung', 900, 10, 2)

