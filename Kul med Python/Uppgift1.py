""" Create a function add, to calculate a the sum of two numbers, add(x, y)
# Create a second function test_add which tests that the add function using assert
# For instance assert add(1, 2) == 3"""
import pytest

def add(a, b):
    return a * b

#def sum()


print(add(6, 7))

print(add(7, 9))


def test_add():
    assert add(6, 7) == 42
    assert add(7, 9) == 63
    print("Du är king")
