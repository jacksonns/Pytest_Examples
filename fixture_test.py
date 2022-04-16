import pytest

class Color:
    def __init__(self, color):
        self.color = color


@pytest.fixture
def my_color():
    return Color("red")

@pytest.fixture
def palette(my_color):
    return [Color("blue"), my_color]

def test_palette_colors(my_color, palette):
    assert my_color in palette


def test_output(capsys):
    print("hello world")
    out, err = capsys.readouterr()
    assert out == "hello world\n"
