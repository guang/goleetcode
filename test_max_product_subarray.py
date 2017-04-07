#!/bin/python3

import pytest
from max_product_subarray import max_product_subarray

testdata = [
    ([], None),
    ([4,2,-1,3], 8),
    ([4,2,-1,-4,-3], 32),
    ([-1,-3,-4,-5], 60),
    ([-1,-3,-4], 12),
    ([-2], -2),
    ([2,4,-2,5,-3], 240)
  ]

@pytest.mark.parametrize("array, expected", testdata)
def test_max_product_subarray(array, expected):
  assert max_product_subarray(array) == expected
