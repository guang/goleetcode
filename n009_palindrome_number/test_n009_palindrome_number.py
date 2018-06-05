import pytest
from n009_palindrome_number_guang import n009_palindrome_number


test_data = [
    (12321, True),
    (12345, False),
    (2222, True),
    (-1332, False),
    (-11311, True),
]


@pytest.mark.parametrize('integer,is_pal', test_data)
def test_n009_palindrome_number(integer, is_pal):
    expected = is_pal
    actual = n009_palindrome_number(integer)
    assert expected == actual
