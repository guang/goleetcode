import pytest
from n013_roman_to_integer_guang import n013_roman_to_integer


test_data = [
    ('III', 3),
    ('IV', 4),
    ('IX', 9),
    ('LVIII', 58),
    ('MCMXCIV', 1994),
]


@pytest.mark.parametrize('roman,num', test_data)
def test_n013_roman_to_integer_guang(roman, num):
    expected = num
    actual = n013_roman_to_integer(roman)
    assert expected == actual
