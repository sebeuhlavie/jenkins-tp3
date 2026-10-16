import pytest

from app.calculator import add, subtract, multiply, divide

pytestmark = pytest.mark.unit


@pytest.mark.parametrize("a, b, attendu", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
    (2.5, 2.5, 5.0),
])
def test_add(a, b, attendu):
    assert add(a, b) == attendu


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 4) == 2.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)