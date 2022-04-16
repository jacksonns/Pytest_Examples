import pytest
from src.foo import *

def exit_function():
    raise SystemExit(1)

def test_exit_function():
    with pytest.raises(SystemExit):
        exit_function()


def test_zero_division():
    with pytest.raises(ZeroDivisionError) :
        1/0

def myfunc():
    raise ValueError("Exception 123 raised")

def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()