import pytest
from calculator import add, subtract, multiply


# ==========================================================
# Should always pass
# ==========================================================

def test_add():
    assert add(2, 3) == 5


# ==========================================================
# Should always pass
# ==========================================================

def test_subtract():
    assert subtract(5, 3) == 2


# ==========================================================
# Main multiplication test
# Used for Cases:
# 2
# 3
# 5
# 6
# 7
# ==========================================================

def test_multiply():
    assert multiply(4, 5) == 20


# ==========================================================
# Uncomment ONLY when testing CASE 4
# Runtime Exception
# ==========================================================

def test_runtime_error():
     with pytest.raises(ZeroDivisionError):
         multiply(4, 5)


# ==========================================================
# Uncomment ONLY when testing CASE 8
# Custom Exception
# ==========================================================

# def test_custom_exception():
#     with pytest.raises(ValueError):
#         multiply(4, 5)


# ==========================================================
# Uncomment ONLY when testing CASE 5
# Wrong return type
# ==========================================================

# def test_return_type():
#     assert isinstance(multiply(4, 5), int)


# ==========================================================
# Uncomment ONLY when testing CASE 6
# None value
# ==========================================================

# def test_not_none():
#     assert multiply(4, 5) is not None