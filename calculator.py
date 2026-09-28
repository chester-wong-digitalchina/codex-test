# Addition operation

def add(x, y):
    return x + y


# Modulo operation

def modulo(x, y):
    if y == 0:
        raise ValueError("Cannot modulo by zero")
    return x % y
