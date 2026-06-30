"""
calculator.py

Uncomment ONE bug at a time to generate different failure scenarios.
"""

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


# ==========================================================
# CASE 1 - Correct implementation (Pipeline should PASS)
# ==========================================================
def multiply(a, b):
    return a * b


# ==========================================================
# CASE 2 - Off-by-one bug
# Expected:
#   4 * 5 = 20
# Returns:
#   21
# AI should detect incorrect multiplication logic.
# ==========================================================

# def multiply(a, b):
#     return a * b + 1


# ==========================================================
# CASE 3 - Wrong operator
# AI should detect multiplication was replaced by addition.
# ==========================================================

# def multiply(a, b):
#     return a + b


# ==========================================================
# CASE 4 - Runtime exception
# AI should identify division by zero.
# ==========================================================

def multiply(a, b):
     return (a * b) / 0


# ==========================================================
# CASE 5 - Wrong return type
# AI should explain why returning a string breaks numeric tests.
# ==========================================================

# def multiply(a, b):
#     return str(a * b)


# ==========================================================
# CASE 6 - Returns None
# AI should explain downstream NoneType problems.
# ==========================================================

# def multiply(a, b):
#     return None


# ==========================================================
# CASE 7 - Logic bug
# Ignores second argument.
# ==========================================================

# def multiply(a, b):
#     return a * a


# ==========================================================
# CASE 8 - Raises custom exception
# ==========================================================

# def multiply(a, b):
#     raise ValueError("Multiplication disabled")

