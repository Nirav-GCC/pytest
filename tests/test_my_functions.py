import time

import pytest

import source.myFuctions as Mf


# This is the function based text
def test_add():
    results = Mf.add(5, 5)
    assert results == 10


def test_add_string():
    results = Mf.add("OOOO", "KKKK")
    assert results == "OOOOKKKK"


def test_divide():
    results = Mf.divide(10, 5)
    assert results == 2


# How to skip the error with error.
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Mf.divide(10, 0)


# To execute slow
@pytest.mark.slow
def test_very_slow():
    time.sleep(2)
    results = Mf.add(10, 20)
    assert results == 30


# To skip the test
@pytest.mark.skip(reason="Not implemented yet")
def test_add():
    assert Mf.add(2, 3) == 5


# To tell that this function going to fail
@pytest.mark.xfail(reason="Cannot divide by zero.")
def test_divide_zero():
    assert Mf.divide(10, 0)
