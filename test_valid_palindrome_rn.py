#/bin/python3

import pytest
from valid_palindrome_rn import is_palindrome

testdata = [
    ("nayan", True),
    ("", True),
    ("a", True),
    ("Hello. This is not a palindrome.", False),
    ("A man, a plan, a canal: Panama", True)]


@pytest.mark.parametrize("input_str, expected", testdata)
def test_is_palindrome(input_str, expected):
  assert is_palindrome(input_str) == expected
