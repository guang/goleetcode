#!/bin/pyton3

import pytest
from max_sum_subarray_rn import max_sum_subarray

testdata = [
    ([1,2,3,-10],6),
    ([3,2,-7,-1,10,-2,20],28),
    ([2,-1,3,0,-5],4),
    ([], None)]

@pytest.mark.parametrize("array, expected", testdata)
def test_max_sum_subarray(array, expected):
  assert max_sum_subarray(array) == expected
