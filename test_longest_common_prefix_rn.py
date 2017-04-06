#!/bin/python3

import pytest
from longest_common_prefix_rn import longest_common_prefix

testdata = [
    ([], ""),
    (["abc"], "abc"),
    (["a", "aa", "aaa", "aaaaaaaa", "asdf", "abgfd"], "a"),
    (["abcd", "ab", "ablkjh"], "ab"),
    (["abcd", "dbca", "lkjh"], ""),
    (["abcdefgh", "abcde", "abcd", "abc", "ab", "a"], "a"),
    (["abcdefgh", "abcde", "abcdegfj", "abcdeklj", "abcderty", "abcdepoi"], "abcde") ]

@pytest.mark.parametrize("strs, expected", testdata)
def test_solution(strs, expected):
  assert longest_common_prefix(strs) == expected
