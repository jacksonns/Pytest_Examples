import pytest
from src.foo import *

class ClassTest:
    def test_one(self):
        x = "test"
        assert "s" in x

    def test_two(self):
        x = "check"
        assert x == "check"

class TestClass:
    def test_one(self):
        x = "test"
        assert "s" in x

    def test_two(self):
        x = "check"
        assert x == "check"