import pytest


def test1():

    a = 3
    b = 4
    assert a == b,"test failed"
    assert a**2 + b**2 == 25, "test failed, they are not equal"


def test2():
    name = "Selenium test"
    assert len(name) == 13 ,"length of the word does not match"

def test3() :
    a = 3
    b = 4
    c = 6
    assert a**2 + b**2 == c**2,"The tri-angle is not a Right triangle"


