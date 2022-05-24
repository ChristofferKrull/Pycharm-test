def sum(a, b):
    return a + b

def neg(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b


def test_sum():
    assert sum(3, 2) == 5
    assert sum(5, 5) == 10

def test_neg():
    assert neg(3, 2) == 1
    assert neg(5, 5) == 0

def test_mul():
    assert mul(3, 2) == 6
    assert mul(5, 5) == 25

def test_div():
        assert div(8, 2) == 4
        assert div(5, 2) == 2.5