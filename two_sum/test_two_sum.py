import pytest
from two_sum_gy import (
    two_sum,
    two_sum_linear_time,
)


test_data = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([4, 2, 11, 7], 9, [1, 3]),
]


@pytest.mark.parametrize('nums, target, ans', test_data)
def test_two_sum(nums, target, ans):
    expected = ans
    actual = two_sum(nums, target)
    assert expected == actual


@pytest.mark.parametrize('nums, target, ans', test_data)
def test_two_sum_linear_time(nums, target, ans):
    expected = ans
    actual = two_sum_linear_time(nums, target)
    assert expected == actual
