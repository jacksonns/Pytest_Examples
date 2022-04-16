from tkinter import Y
import pytest
from src.foo import *

# Wrong answer
def test_answer1():
    assert inc(3) == 5

# Right answer
def test_answer2():
    assert inc(4) == 5

