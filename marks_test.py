import pytest

def math_square(x):
    return x*x


@pytest.mark.parametrize('input, expected_output', [ (3, 9), (4, 15), (5, 25) ] )
def test_math_square(input, expected_output):
    result = math_square(input)
    assert result == expected_output