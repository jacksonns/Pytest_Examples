import pytest
from src.foo import *

# Wrong answer
def testanswer1():
    assert inc(3) == 5

# Right answer
def testanswer2():
    assert inc(4) == 5

