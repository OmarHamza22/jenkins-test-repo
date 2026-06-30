from calculator import add, subtract, multiply

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(4, 5) == 20  # This will FAIL because of the bug
